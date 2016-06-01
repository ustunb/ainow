"""ainow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from .views import HomeView, RSVPView, PrivacyView
from conference.views import ScheduleView, SpeakerListView, PresentationView

admin.autodiscover()

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^rsvp$', RSVPView.as_view(), name='rsvp'),
    url(r'^privacy$', PrivacyView.as_view(), name='privacy'),
    url(r'^schedule/(?P<slug>[-\w]+)$', ScheduleView.as_view(), name='schedule'),
    url(r'^presentation/(?P<slug>[-\w]+)$', PresentationView.as_view(), name='presentation'),
    url(r'^speakers$', SpeakerListView.as_view(), name='speakers'),
    url(r'^admin/', admin.site.urls),
    url(r'^markitup/', include('markitup.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
