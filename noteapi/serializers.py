from email.policy import default

from rest_framework import serializers

from noteapi.models import Note
from users.serializers import UserRegistrationSerializer


class NoteSerializer(serializers.ModelSerializer):
    author = UserRegistrationSerializer(default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = Note
        fields = ['id','author', 'title', 'slug', 'content', 'date']
