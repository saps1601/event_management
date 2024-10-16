from rest_framework import serializers
from .models import UserProfile, Event, RSVP, Review
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ['user', 'full_name', 'bio', 'location', 'profile_picture']


class EventSerializer(serializers.ModelSerializer):
    organizer = UserProfileSerializer(read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'organizer', 'location', 
                  'start_time', 'end_time', 'is_public', 'created_at', 'updated_at']


class RSVPSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = RSVP
        fields = ['id', 'event', 'user', 'status']


class ReviewSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'event', 'user', 'rating', 'comment']
