"""Tests for the models of the djangocms_text_redactor app."""
from django.test import TestCase

from . import factories


class DummyModelTestCase(TestCase):
    """Tests for the ``DummyModel`` model."""
    def test_model(self):
        obj = factories.RedactorTextFactory()
        self.assertTrue(obj.pk)
