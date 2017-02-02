from rest_framework import serializers
from logbook.models import Climb
from django.contrib.auth.models import User

class ClimbSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    #centre = serializers.ReadOnlyField(source='

    class Meta:
        model = Climb
        fields = ('id', 'colour', 'grade', 'centre', 'created', 'owner')

class UserSerializer(serializers.ModelSerializer):
    climbs = serializers.PrimaryKeyRelatedField(many=True, queryset = Climb.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'climbs')