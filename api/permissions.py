from rest_framework.permissions import BasePermission

class IsOrganizerOrReadOnly(BasePermission):
    """
    Custom permission to allow only event organizers to edit or delete an event.
    """

    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Write permissions are only allowed to the event organizer
        return obj.organizer.user == request.user
