"""URLs for the djangocms_text_redactor app."""
from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^$',
        views.RedactorSaveView.as_view(),
        name='djangocms_text_redactor_save'),
)
