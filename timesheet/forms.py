from django import forms
from timesheet.models import Entry, Type

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['date', 'time', 'type', 'description']
        labels = {
            'date': 'Date',
            'time': 'Time',
            'type': 'Type',
            'description': 'Description',
        }
        widgets = {
            'date': forms.DateInput(format=('%d/%m/%Y')) 
        }
