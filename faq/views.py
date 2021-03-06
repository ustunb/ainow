from django.views.generic import DetailView

from conference.views import ScheduleMixin

from .models import FAQPage


class FAQPageView(ScheduleMixin, DetailView):
    model = FAQPage
    context_object_name = 'page'

    def get_context_data(self, **kwargs):
        context = super(FAQPageView, self).get_context_data(**kwargs)
        context['questions'] = context['page'].questions.all().order_by('link_to_page')
        return context
