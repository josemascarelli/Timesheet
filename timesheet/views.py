from timesheet.models import Entry
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from timesheet.forms import EntryForm


class EntryListView(ListView):
    model = Entry
    reverse_lazy('list_view')
    ordering = ['-date_added']


class EntryCreateView(CreateView):
    model = Entry
    form_class = EntryForm
    success_url = reverse_lazy('list_view')

class EntryUpdateView(UpdateView):
    model = Entry
    form_class = EntryForm
    success_url = reverse_lazy('list_view')

class EntryDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy('list_view')