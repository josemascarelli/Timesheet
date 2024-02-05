from django.urls import path
from .views import EntryListView, EntryCreateView, EntryUpdateView, EntryDeleteView

urlpatterns = [
    path('', EntryListView.as_view(), name='list_view'),
    path('create', EntryCreateView.as_view(), name='create_view'),
    path('update/<uuid:pk>', EntryUpdateView.as_view(), name='update_view'),
    path('delete/<uuid:pk>', EntryDeleteView.as_view(), name='delete_view'),
]
