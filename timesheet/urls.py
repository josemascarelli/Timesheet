from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('entries/', views.get_entries, name='entries'),
    path('types/', views.get_types, name='types'),
    path('entry/<uuid:id>/', views.get_entry_by_id, name='entry'),
    path('type/<uuid:id>/', views.get_type_by_id, name='type'),
    ]