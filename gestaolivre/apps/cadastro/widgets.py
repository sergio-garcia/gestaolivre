# -*- coding: utf-8 -*-
from django.forms import widgets
from django.utils.html import format_html
from django.utils.encoding import force_text
from django.forms.utils import flatatt


class DatePicker(widgets.TextInput):

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_text(self._format_value(value))
        return format_html('<paper-datepicker {}></paper-datepicker>', flatatt(attrs))
