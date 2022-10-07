from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

from .models import *


class FormBaseRegisterStudent(forms.ModelForm):
    class Meta:
        model = InfoStudent
        # fields = '__all__'
        fields = ('name', 'middle_name', 'last_name', 'direction', 'course', 'photo_student',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'direction': forms.Select(attrs={'class': 'form-select'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'photo_student': forms.FileInput(attrs={'class': 'custom-file-input'}),
        }


class FormAdvancedRegisterStudent(forms.ModelForm):
    class Meta:
        model = InfoStudent
        # fields = '__all__'
        fields = ('name', 'middle_name', 'last_name', 'direction', 'course', 'student_status', 'photo_student',
                  'photo_social_reference', 'start_social_reference', 'end_social_reference')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'direction': forms.Select(attrs={'class': 'form-select'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'student_status': forms.Select(attrs={'class': 'form-select'}),
            'photo_student': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'photo_social_reference': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'start_social_reference': forms.TextInput(attrs={'class': 'form-control'}),
            'end_social_reference': forms.TextInput(attrs={'class': 'form-control'}),

        }


class FormFullRegisterStudent(forms.ModelForm):
    class Meta:
        model = InfoStudent
        fields = '__all__'
        widgets = {
            # 'name': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'direction': forms.Select(attrs={'class': 'form-select'}),
            'course': forms.Select(attrs={'class': 'form-select', 'readonly': 'readonly'}, ),
            'student_status': forms.Select(attrs={'class': 'form-select'}),
            'organization': forms.Select(attrs={'class': 'form-select'}),
            'organization_sector': forms.Select(attrs={'class': 'form-select'}),
            'photo_student': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'photo_social_reference': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'start_social_reference': forms.TextInput(attrs={'class': 'form-control'}),
            'end_social_reference': forms.TextInput(attrs={'class': 'form-control'}),
        }

        # def clean_first_name(self):
        #     data = self.cleaned_data['first_name']
        #     if data == 'a':
        #         raise ValidationError('ошибка')


class FormLogin_s(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
