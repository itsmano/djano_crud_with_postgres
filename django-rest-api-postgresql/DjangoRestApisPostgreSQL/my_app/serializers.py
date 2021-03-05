from rest_framework import serializers
from my_app.models import Tutorial, User


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'password',
                  'active')


