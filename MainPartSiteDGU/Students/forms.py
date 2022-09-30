from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddNewStudent(forms.ModelForm):
    class Meta:
        model = InfoStudent
        fields = '__all__'
        # fields = ('last_name', 'middle_name', 'direction', 'course', 'student_status', 'photo_student',
        #           'social_status',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'direction': forms.Select(attrs={'class': 'form-select'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'student_status': forms.Select(attrs={'class': 'form-select'}),
            'photo_student': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'social_status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    # def clean_first_name(self):
    #     data = self.cleaned_data['first_name']
    #     if data == 'a':
    #         raise ValidationError('ошибка')


# class TestForm(forms.ModelForm):
#     class Meta:
#         model = Test
#         fields = '__all__'
