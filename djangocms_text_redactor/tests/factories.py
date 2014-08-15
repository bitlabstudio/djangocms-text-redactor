"""Factories for the djangocms_text_redactor app."""
import factory

from .. import models


class RedactorTextFactory(factory.DjangoModelFactory):
    """Factory for the ``RedactorText`` model."""
    FACTORY_FOR = models.RedactorText
