from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Event, RSVP, Review, UserProfile
from .serializers import EventSerializer, RSVPSerializer, ReviewSerializer, UserProfileSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsOrganizerOrReadOnly  # Custom permission we’ll create soon

# Event ViewSet
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOrganizerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'location', 'organizer__user__username']  # Filtering fields

    def perform_create(self, serializer):
        user_profile = UserProfile.objects.get(user=self.request.user)
        serializer.save(organizer=user_profile)

# RSVP ViewSet
class RSVPViewSet(viewsets.ModelViewSet):
    queryset = RSVP.objects.all()
    serializer_class = RSVPSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        data['user'] = UserProfile.objects.get(user=request.user).id
        data['event'] = kwargs['event_id']
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# Review ViewSet
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        data['user'] = UserProfile.objects.get(user=request.user).id
        data['event'] = kwargs['event_id']
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
