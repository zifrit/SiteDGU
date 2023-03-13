from django import forms
from .models import *


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
