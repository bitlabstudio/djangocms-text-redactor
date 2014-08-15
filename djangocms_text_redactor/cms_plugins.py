"""CMS plugins for the djangocms_text_redactor app."""
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models


class RedactorPlugin(CMSPluginBase):
    model = models.RedactorText
    name = _("Redactor Plugin")
    render_template = "djangocms_text_redactor/redactor_plugin.html"

    def render(self, context, instance, placeholder):
        image_upload_url = getattr(
            settings, 'DJANGOCMS_TEXT_REDACTOR_IMAGE_UPLOAD_URL', '')
        if image_upload_url:
            image_upload_url = reverse(image_upload_url)
        image_get_json_url = getattr(
            settings, 'DJANGOCMS_TEXT_REDACTOR_IMAGE_GET_JSON_URL', '')
        if image_get_json_url:
            image_get_json_url = reverse(image_get_json_url)
        context.update({
            'instance': instance,
            'image_upload_url': image_upload_url,
            'image_get_json_url': image_get_json_url,
        })
        return context


plugin_pool.register_plugin(RedactorPlugin)
