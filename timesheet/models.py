from django.db import models
from datetime import datetime
from uuid import uuid4 as uuid

class Entry(models.Model):
    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'
        ordering = ['-date']
    
    '''A timesheet entry.'''
    id = models.UUIDField(primary_key=True, default=uuid, editable=False)
    date_added = models.DateTimeField(default=datetime.now, editable=False ,verbose_name='DATE ADDED')
    date = models.DateField(verbose_name='DATE', help_text='Date of the entry', default=datetime.now)
    time = models.IntegerField(verbose_name='TIME', default=10, help_text='Time in minutes')
    type = models.ForeignKey('Type', on_delete=models.PROTECT, verbose_name='TYPE', help_text='What type of work did you do?')
    description = models.TextField(verbose_name='DESCRIPTION', help_text='What did you do?')

    def __str__(self):
        return f'{self.id} - {self.type} - {self.date} - {self.time}'
    


class Type(models.Model):
    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'
        ordering = ['name']

    '''A type of timesheet entry.'''
    id = models.UUIDField(primary_key=True, default=uuid, editable=False)
    date_added = models.DateTimeField(default=datetime.now, editable=False ,verbose_name='DATE ADDED')
    name = models.CharField(max_length=100, verbose_name='NAME', help_text='Name of the type')

    def __str__(self):
        return f'{self.id} - {self.name}'