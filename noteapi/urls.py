from django.urls import path

from . import views

app_name = "notes"

urlpatterns = [
    path('', views.NotesListView.as_view(), name="notes"),
    path('<str:pk>/', views.NoteDetailView.as_view(), name="note-detail"),
]