from django.db import models
from datetime import datetime
from uuid import uuid4 as uuid

class Timesheet(models.Model):
    '''A timesheet entry.'''
    id = models.UUIDField(primary_key=True, default=uuid, editable=False)
    date_added = models.DateTimeField(default=datetime.now, editable=False ,verbose_name='DATE ADDED')
    date = models.DateField(verbose_name='DATE', help_text='Date of the entry', default=datetime.now)
    time = models.IntegerField(verbose_name='TIME', default=10, help_text='Time in minutes')
    description = models.TextField(verbose_name='DESCRIPTION', help_text='What did you do?')
