"""Views for the djangocms_text_redactor app."""
from django.views.generic import View
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

from . import models


class RedactorSaveView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff and not request.user.is_superuser:
            return HttpResponseForbidden()
        if not request.POST:
            return HttpResponseForbidden()
        plugin = models.RedactorText.objects.get(pk=request.POST.get(
            'plugin_instance_pk'))
        plugin.content = request.POST.get('redactor_content')
        plugin.save()
        return redirect(request.POST.get('next'))
