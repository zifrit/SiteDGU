from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddNewStudent(forms.ModelForm):
    class Meta:
        model = InfoStudent
        fields = '__all__'

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        if data == 'a':
            raise ValidationError('ошибка')