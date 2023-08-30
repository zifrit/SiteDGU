from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.core.exceptions import ValidationError
# from ..MainPartSiteDGU.settings import AUTH_USER_MODEL
from .models import *
import re


class FormBaseRegisterStudent(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Имя', label='Имя',
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия', label='Фамилия',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    middle_name = forms.CharField(max_length=30, required=False, help_text='Отчество', label='Отчество',
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = ProfileStudent
        fields = ('first_name', 'last_name', 'middle_name', 'direction', 'course', 'photo_student',)
        widgets = {
            'direction': forms.Select(attrs={'class': 'form-select'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'photo_student': forms.FileInput(attrs={'class': 'custom-file-input'}),
        }


class FormAdvancedRegisterStudent(FormBaseRegisterStudent):
    class Meta:
        model = ProfileStudent
        # fields = '__all__'
        fields = ('first_name', 'last_name', 'middle_name', 'direction', 'course', 'student_status', 'photo_student',
                  'photo_social_reference', 'start_social_reference', 'end_social_reference')
        widgets = {
            'direction': forms.Select(attrs={'class': 'form-select'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'student_status': forms.Select(attrs={'class': 'form-select'}),
            'photo_student': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'photo_social_reference': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'start_social_reference': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ГГГГ-ММ-ДД'}),
            'end_social_reference': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ГГГГ-ММ-ДД'}),

        }


class FormFullRegisterStudent(FormBaseRegisterStudent):
    class Meta:
        model = ProfileStudent
        fields = ('first_name', 'last_name', 'middle_name', 'direction', 'course', 'student_status', 'photo_student',
                  'photo_social_reference', 'start_social_reference', 'end_social_reference', 'organization',
                  'organization_sector',)
        widgets = {
            'direction': forms.Select(attrs={'class': 'form-select'}),
            'course': forms.Select(attrs={'class': 'form-select', 'readonly': 'readonly'}, ),
            'student_status': forms.Select(attrs={'class': 'form-select'}),
            'organization': forms.Select(attrs={'class': 'form-select'}),
            'organization_sector': forms.Select(attrs={'class': 'form-select'}),
            'photo_student': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'photo_social_reference': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'start_social_reference': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ГГГГ-ММ-ДД'}),
            'end_social_reference': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ГГГГ-ММ-ДД'}),
        }


class FormLogin_s(AuthenticationForm):
    username = UsernameField(label='Логин', widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form_input'}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form_input'}),
    )


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control form-input'}))
    password2 = forms.CharField(label='Повтор пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control form-input'}))

    # is_active = forms.CharField()

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2',)
