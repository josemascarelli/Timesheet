from django import forms
from timesheet.models import Entry


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
        error_messages = {

            'date': {
                'invalid': 'Por favor, insira uma data válida.',
            },
            'time': {
                'invalid': 'Por favor, insira um tempo válido.',
            },
            'type': {
                'invalid': 'Por favor, insira um tipo válido.',
            },
            'description': {
                'invalid': 'Por favor, insira uma descrição válida.',
            },
        }
        help_texts = {
            'date': 'Date of the timesheet entry.',
            'time': 'Time in minutes',
            'type': 'What type of work did you do?',
            'description': 'What did you do?',
        }
        widgets = {
            'date': forms.DateInput(format=('%d/%m/%Y')),
            'time': forms.TimeInput(format=('%H:%M')),
        }
