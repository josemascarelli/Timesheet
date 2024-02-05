from django.db import models
from datetime import datetime
from uuid import uuid4 as uuid


class Entry(models.Model):
    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'
        ordering = ['-date']

    id = models.UUIDField(
        verbose_name='ID',
        primary_key=True,
        default=uuid,
        editable=False,
    )
    date_added = models.DateTimeField(
        verbose_name='DATE ADDED',
        default=datetime.now,
        editable=False,
    )
    date = models.DateField(
        verbose_name='DATE',
        default=datetime.now,
    )
    time = models.DurationField(
        verbose_name='TIME',
    )
    type = models.ForeignKey(
        verbose_name='TYPE',
        to='Type',
        on_delete=models.PROTECT,
    )
    description = models.TextField(
        verbose_name='DESCRIPTION',
    )

    def __str__(self):
        return f'Entry(id={self.id}, \
                       date_added={self.date_added}, \
                       date={self.date}, \
                       time={self.time}, \
                       type={self.type}, \
                       description={self.description})'


class Type(models.Model):
    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'
        ordering = ['name']

    id = models.UUIDField(
        primary_key=True,
        verbose_name='ID',
        default=uuid,
        editable=False,
    )
    date_added = models.DateTimeField(
        verbose_name='DATE ADDED',
        default=datetime.now,
        editable=False,
    )
    name = models.CharField(
        verbose_name='NAME',
        max_length=100,
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Type(id={self.id}, \
                      date_added={self.date_added}, \
                      name={self.name})'