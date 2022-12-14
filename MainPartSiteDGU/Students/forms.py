from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
# from ..MainPartSiteDGU.settings import AUTH_USER_MODEL
from .models import *
import re


class FormBaseRegisterStudent(forms.ModelForm):
    class Meta:
        model = InfoStudent
        # fields = '__all__'
        fields = ('surname', 'name', 'middle_name', 'direction', 'course', 'photo_student',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'direction': forms.Select(attrs={'class': 'form-select'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'photo_student': forms.FileInput(attrs={'class': 'custom-file-input'}),
        }


class FormAdvancedRegisterStudent(forms.ModelForm):
    class Meta:
        model = InfoStudent
        # fields = '__all__'
        fields = ('surname', 'name', 'middle_name', 'direction', 'course', 'student_status', 'photo_student',
                  'photo_social_reference', 'start_social_reference', 'end_social_reference')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'direction': forms.Select(attrs={'class': 'form-select'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'student_status': forms.Select(attrs={'class': 'form-select'}),
            'photo_student': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'photo_social_reference': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'start_social_reference': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ДД.ММ.ГГГГ'}),
            'end_social_reference': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ДД.ММ.ГГГГ'}),

        }

    def clean_start_social_reference(self):
        date = self.cleaned_data['start_social_reference']
        s = re.match(r'\d{2}.\d{2}.\d{4}', date)
        if s == None:
            raise ValidationError('введенная дата не соответствует шаблону')
        return date

    def clean_end_social_reference(self):
        date = self.cleaned_data['end_social_reference']
        s = re.match(r'\d{2}.\d{2}.\d{4}', date)
        if s == None:
            raise ValidationError('введенная дата не соответствует шаблону')
        return date


class FormFullRegisterStudent(forms.ModelForm):
    class Meta:
        model = InfoStudent
        fields = ('surname', 'name', 'middle_name', 'direction', 'course', 'student_status', 'photo_student',
                  'photo_social_reference', 'start_social_reference', 'end_social_reference', 'organization',
                  'organization_sector',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'direction': forms.Select(attrs={'class': 'form-select'}),
            'course': forms.Select(attrs={'class': 'form-select', 'readonly': 'readonly'}, ),
            'student_status': forms.Select(attrs={'class': 'form-select'}),
            'organization': forms.Select(attrs={'class': 'form-select'}),
            'organization_sector': forms.Select(attrs={'class': 'form-select'}),
            'photo_student': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'photo_social_reference': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'start_social_reference': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ДД.ММ.ГГГГ'}),
            'end_social_reference': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ДД.ММ.ГГГГ'}),
        }

    def clean_start_social_reference(self):
        date = self.cleaned_data['start_social_reference']
        s = re.match(r'\d{2}.\d{2}.\d{4}', date)
        if s == None:
            raise ValidationError('введенная дата не соответствует шаблону')
        return date

    def clean_end_social_reference(self):
        date = self.cleaned_data['end_social_reference']
        s = re.match(r'\d{2}.\d{2}.\d{4}', date)
        if s == None:
            raise ValidationError('введенная дата не соответствует шаблону')
        return date


class FormLogin_s(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control form-input'}))
    password2 = forms.CharField(label='Повтор пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control form-input'}))

    # is_active = forms.CharField()

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2',)


class DataInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = "time"


class FormCreateEvents(forms.ModelForm):
    class Meta:
        model = Events
        # fields = '__all__'
        fields = ['name', 'text', 'photo', 'date', 'time']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'date': DataInput(),
            'time': TimeInput(),
            'photo': forms.FileInput(attrs={'class': 'custom-file-input'}),
        }

    def clean_date(self):
        date = self.cleaned_data['date']
        return date
