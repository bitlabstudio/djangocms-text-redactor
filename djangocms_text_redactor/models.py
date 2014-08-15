"""Models for the djangocms_text_redactor app."""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin


class RedactorText(CMSPlugin):
    redactor_settings = models.TextField(
        verbose_name=_('Redactor settings'),
        default=(
            "{\n"
            "    buttons: ['formatting',  'bold', 'italic', 'deleted',\n"
            "        'unorderedlist', 'orderedlist', 'outdent', 'indent',\n"
            "        'image', 'video', 'file', 'table', 'link', 'alignment',\n"
            "        'horizontalrule'],\n"
            "    toolbarFixed: true,\n"
            "    toolbarFixedBox: true,\n"
            "    toolbarExternal: '[data-id=\"redactor-toolbar\"]',\n"
            "    imageUpload: image_upload_url,\n"
            "    imageGetJson: image_get_json_url\n"
            "}"
        ),
    )
    content = models.TextField(blank=True)
