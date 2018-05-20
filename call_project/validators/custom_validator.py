"""
This is a custom packet valitations
"""

from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from rest_framework.exceptions import ValidationError
from rest_framework.compat import unicode_to_repr
from rest_framework.utils.representation import smart_repr


class RequiredIf(object):
    """
    Class to validate if field is Required
    """
    missing_message = _('This field is required')

    def __init__(self, fields, condition):
        self.fields = fields
        self.condition = condition

    def enforce_required_fields(self, attrs):
        # TODO: Validate others conditions like < > !=
        missing = []
        if self.condition[1] is False:
            missing = dict([(field_name, self.missing_message)
                            for field_name in self.fields
                            if field_name not in dict(attrs)
                            ])
        elif attrs[self.condition[0]] == self.condition[1]:
            missing = dict([(field_name, self.missing_message)
                            for field_name in self.fields
                            if field_name not in dict(attrs)
                            ])

        if missing:
            raise ValidationError(missing)

    def __call__(self, attrs):
        self.enforce_required_fields(attrs)

    def __repr__(self):
        return unicode_to_repr('<%s(fields=%s)>' % (
            self.__class__.__name__,
            smart_repr(self.fields)
        ))
