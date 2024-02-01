from django.shortcuts import HttpResponse, render
from .models import Entry, Type
from timesheet.forms import EntryForm


def home(request):
    return render(request, 'timesheet/home.html')

def new(request):
    return render(request, 'timesheet/new.html', {'forms': EntryForm})

def get_entries(request):
    entries = Entry.objects.all()
    return render(request, 'timesheet/entries.html', {'entries': entries})

def get_entry_by_id(request, id):
    entry = Entry.objects.get(id=id)
    return HttpResponse(entry)

def get_types(request):
    types = Type.objects.all()
    return HttpResponse(types)

def get_type_by_id(request, id):
    type = Type.objects.get(id=id)
    return HttpResponse(type)