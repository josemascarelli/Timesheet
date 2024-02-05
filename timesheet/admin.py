from django.contrib import admin
from timesheet.models import Entry, Type

# Register your models here.
admin.site.register(Entry)
admin.site.register(Type)
