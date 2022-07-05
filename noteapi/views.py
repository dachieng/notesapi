from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import (SAFE_METHODS, BasePermission,
                                        IsAuthenticated)

from noteapi.models import Note
from noteapi.serializers import NoteSerializer


# custom permision, the author must be the logged in user in order to edit/delete/update post
class UserWriteNote(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user 


class NotesListView(ListCreateAPIView, UserWriteNote):
    permission_classes = [IsAuthenticated, UserWriteNote]

    serializer_class = NoteSerializer

    def get_queryset(self):
        return Note.objects.filter(author = self.request.user)

    # set the user to the current logged in user
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class NoteDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, UserWriteNote]
    serializer_class = NoteSerializer

    def get_queryset(self):
        return Note.objects.filter(author = self.request.user)
    

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Note, slug=item)
    
    def perform_update(self, serializer):
        serializer.save(author=self.request.user)