from django.views.generic import DetailView, ListView
from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.views.generic.edit import ModelFormMixin, ProcessFormView
from django.shortcuts import get_object_or_404, redirect
from django.utils.http import is_safe_url
from django.core.urlresolvers import reverse
from django import forms
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.forms import modelform_factory
from django.db.models import Q

import sorl

from account.mixins import LoginRequiredMixin

from .models import Schedule, Speaker, OrganiserType, Presentation, Attendee, StandingCommittee
from .forms import AttendeeForm
from blocks.models import Block


class ScheduleMixin(object):
    """
    A view mixin to retrieve the related schedule for other views,
    force logins for private schedules and objects related to
    private schedules, and automatically filter objects to those
    related to the given schedule.
    """

    # Override this if your url uses a different kwarg name for
    # the schedule's slug
    schedule_slug_kwarg = 'schedule_slug'

    def dispatch(self, request, *args, **kwargs):
        """
        Overridden dispatch so that self.schedule is available
        throughout the whole method chain of any view.
        """
        self.schedule = get_object_or_404(
            Schedule,
            slug=kwargs.get(self.schedule_slug_kwarg)
        )
        if self.schedule.private and not request.user.is_authenticated():
            return redirect('%s?next=%s' % (reverse('account_login'), request.path))
        return super(ScheduleMixin, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        """
        Overridden get_queryset to filter the models down to those
        that are related to this schedule.
        """
        return super(ScheduleMixin, self).get_queryset().filter(schedule=self.schedule)

    def get_context_data(self, **kwargs):
        context = super(ScheduleMixin, self).get_context_data(**kwargs)
        context['schedule'] = self.schedule
        return context


class ScheduleView(DetailView):
    model = Schedule
    context_object_name = 'schedule'

    def get(self, request, *args, **kwargs):
        """
        Overridden get from BaseDetailView in order to check the
        schedule access before rendering the view.
        """
        self.object = self.get_object()

        if self.object.private and not request.user.is_authenticated():
            return redirect('%s?next=%s' % (reverse('account_login'), request.path))

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(ScheduleView, self).get_context_data(**kwargs)
        context['slots'] = context['schedule'].slots.order_by('start')
        sidebar_block = Block.objects.get(slug="{}-sidebar".format(context['schedule'].slug))
        context['sidebar_block'] = sidebar_block.content
        try:
            footer_block = Block.objects.get(slug="{}-footer".format(context['schedule'].slug))
            context['footer_block'] = footer_block.content
        except Block.DoesNotExist:
            context['footer_block'] = None
        return context


class SpeakerListView(ScheduleMixin, ListView):
    model = Speaker
    context_object_name = 'speakers'

    def get_queryset(self):
        """
        Speakers are linked to a schedule by their presentation(s) slot(s).
        """

        return Speaker.objects.filter(
            Q(presentations__slot__schedule=self.schedule) |
            Q(additional_presentations__slot__schedule=self.schedule)
        ).distinct()


class SpeakerView(ScheduleMixin, DetailView):
    model = Speaker
    context_object_name = 'speaker'

    def get_queryset(self):
        """
        Speakers are linked to a schedule by their presentation(s) slot(s).
        """
        return Speaker.objects.filter(
            Q(presentations__schedule=self.schedule) |
            Q(additional_presentations__schedule=self.schedule) |
            Q(presentations__slot__schedule=self.schedule) |
            Q(additional_presentations__slot__schedule=self.schedule)
        ).distinct()


class OrganiserTypeListView(ScheduleMixin, ListView):
    model = OrganiserType
    context_object_name = 'organiser_types'

    def get_queryset(self):
        return OrganiserType.objects.all()


class StandingCommitteeListView(ListView):
    model = StandingCommittee
    context_object_name = 'standing_committee'


class PresentationView(ScheduleMixin, DetailView):
    model = Presentation
    context_object_name = 'presentation'

    def get_queryset(self):
        """
        Presentations are linked to a schedule by their slot.
        """
        return Presentation.objects.filter(
            Q(schedule=self.schedule) |
            Q(slot__schedule=self.schedule)
        ).distinct()


class PresentationListView(ListView):
    model = Presentation
    context_object_name = 'presentations'

    def get_context_data(self, **kwargs):
        context = super(PresentationListView, self).get_context_data(**kwargs)
        context['schedule'] = Schedule.objects.get(slug='conference')
        # This is very hacky, but we want to show both sets of talks, and
        # they're not easily differentiated at this stage
        workshop_slugs = [
            'ai-now-overview-and-introduction',
            'time-different-opportunities-and-challenges-artifi',
            'great-decoupling',
            'uncovering-machine-bias',
            'labor-makes-ai-magic',
            'time-different-race-labor-and-ai',
            'symbiotic-human-robot-interaction',
            'bending-gig-economy-toward-equity',
            'who-gets-think-about-ai',
            'machining-ethics',
            'elevating-human-condition-through-new-partnership',
            'machine-learning-and-healthcare-risks-and-rewards',
            'sites-deliberation',
            'complementary-vs-substitutive-automation-healthcar',
            'we-classified'
        ]
        symposium_slugs = [
            'welcome-ai-now',
            'introductions-ed-felten',
            'conversation-white-house-past-and-present',
            'three-questions-three-tech-leaders',
            'plenary-panel-inequality-labor-health-and-ethics-a'
        ]
        context['workshop_presentations'] = []
        for slug in workshop_slugs:
            context['workshop_presentations'].append(Presentation.objects.get(slug=slug))

        context['symposium_presentations'] = []
        for slug in symposium_slugs:
            context['symposium_presentations'].append(Presentation.objects.get(slug=slug))

        return context


class AttendeeListView(ScheduleMixin, ListView):
    model = Attendee
    context_object_name = 'attendees'


class AttendeeView(ScheduleMixin, DetailView):
    model = Attendee
    context_object_name = 'attendee'


class AttendeeCreateUpdateView(LoginRequiredMixin,
                               SingleObjectTemplateResponseMixin,
                               ModelFormMixin,
                               ProcessFormView):
    """A combined create and update view for Attendees"""
    # Taken from http://stackoverflow.com/a/30948175
    model = Attendee
    context_object_name = 'attendee'
    template_name = 'conference/attendee_profile_form.html'
    form_class = AttendeeForm
    success_url = '/profile/'  # Come back to this page

    def dispatch(self, request, *args, **kwargs):
        self.schedule = Schedule.objects.get(slug='workshop')
        return super(AttendeeCreateUpdateView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        try:
            return self.request.user.conference_attendee_profile
        except AttributeError:
            return None

    def get_initial(self):
        initial = super(AttendeeCreateUpdateView, self).get_initial()
        initial['user'] = self.request.user
        initial['schedule'] = self.schedule
        return initial

    def get_form_kwargs(self):
        # Force the submitted user to be request.user and the schedule to be
        # our chosen Schedule
        kwargs = super(AttendeeCreateUpdateView, self).get_form_kwargs()
        if self.request.method in ('POST', 'PUT'):
            kwargs['data']['user'] = self.request.user.id
            kwargs['data']['schedule'] = self.schedule.id
        return kwargs

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(AttendeeCreateUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(AttendeeCreateUpdateView, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AttendeeCreateUpdateView, self).get_context_data(**kwargs)
        context['schedule'] = self.schedule
        back_url = reverse('home')
        user_supplied_back_url = self.request.GET.get('back')
        if user_supplied_back_url and is_safe_url(user_supplied_back_url):
            back_url = user_supplied_back_url
        context['back_url'] = back_url
        return context


@login_required
def delete_photo(request):
    """
    A view specifically for deleting the photo attached to a profile so that
    we can do that via ajax and a nicer UI, rather than using Django's
    clearable file input (which is a bit clunky).
    """
    if request.method == 'POST' and request.is_ajax():
        # Delete the photo
        attendee = request.user.conference_attendee_profile
        sorl.thumbnail.delete(attendee.photo, delete_file=False)
        attendee.photo.delete()  # Saves the model automatically

        # Build a new form
        form_class = modelform_factory(Attendee, fields=['photo'])
        form = form_class(instance=attendee)
        form.fields['photo'].widget = forms.FileInput()

        # Render a response with the form and updated attendee
        html = render_to_string(
            'conference/_profile_photo.html',
            {'attendee': attendee, 'form': form}
        )
        return HttpResponse(html)
    else:
        return HttpResponseBadRequest("This endpoint is only available to AJAX POST requests")
