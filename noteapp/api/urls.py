from django.urls import path
from .views import *

urlpatterns = [
    path('Notes/', NotesList.as_view()),
    path('Notes/<int:pk>/', NotesDetail.as_view()),
]
