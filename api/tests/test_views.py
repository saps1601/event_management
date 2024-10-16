from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import UserProfile, Event
from django.contrib.auth.models import User

class EventTests(APITestCase):
    
    def setUp(self):
        # Create a user and profile
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.profile = UserProfile.objects.create(user=self.user, full_name='Test User')
        self.client.login(username='testuser', password='testpass')

    def test_create_event(self):
        url = reverse('event-list')
        data = {
            'title': 'Test Event',
            'description': 'Test description',
            'location': 'Test Location',
            'start_time': '2024-10-20T10:00:00Z',
            'end_time': '2024-10-20T16:00:00Z',
            'is_public': True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 1)
        self.assertEqual(Event.objects.get().title, 'Test Event')

    def test_get_event_list(self):
        url = reverse('event-list')
        Event.objects.create(title='Test Event 1', description='Test description 1', 
                             organizer=self.profile, location='Test Location 1', 
                             start_time='2024-10-20T10:00:00Z', end_time='2024-10-20T16:00:00Z', 
                             is_public=True)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_update_event(self):
        event = Event.objects.create(title='Test Event', description='Test description', 
                                      organizer=self.profile, location='Test Location', 
                                      start_time='2024-10-20T10:00:00Z', end_time='2024-10-20T16:00:00Z', 
                                      is_public=True)
        url = reverse('event-detail', args=[event.id])
        data = {
            'title': 'Updated Event'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        event.refresh_from_db()
        self.assertEqual(event.title, 'Updated Event')

    def test_delete_event(self):
        event = Event.objects.create(title='Test Event', description='Test description', 
                                      organizer=self.profile, location='Test Location', 
                                      start_time='2024-10-20T10:00:00Z', end_time='2024-10-20T16:00:00Z', 
                                      is_public=True)
        url = reverse('event-detail', args=[event.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Event.objects.count(), 0)
