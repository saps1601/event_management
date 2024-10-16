# Event Management API

This project is an Event Management API built with Django and Django REST Framework. It allows users to create events, RSVP, and leave reviews.

## Features

- User authentication with JWT
- Event creation, retrieval, update, and deletion
- RSVP management for events
- Review system for events
- Pagination and filtering for event listings
- Asynchronous email notifications using Celery

## Requirements

- Python 3.x
- Django 3.x
- Django REST Framework
- Redis (for Celery)
- Django Filters

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/event_management.git
   cd event_management



2. Create a virtual environment and activate it:

	python -m venv venv
	source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages

4. Set up the database:
	python manage.py migrate


5. Create a superuser
	python manage.py createsuperuser


6. Start Redis
	redis-server


7. Start the Django server:

	python manage.py runserver

8. Start the Celery worker:

	celery -A event_management worker --loglevel=info



API Endpoints
	

	Authentication

		POST /api/token/ - Obtain JWT token
		POST /api/token/refresh/ - Refresh JWT token
	

	Events

		POST /api/events/ - Create a new event (authenticated users only)
		GET /api/events/ - List all public events (with pagination)
		GET /api/events/{id}/ - Get details of a specific event
		PUT /api/events/{id}/ - Update an event (only the organizer can edit)
		DELETE /api/events/{id}/ - Delete an event (only the organizer)
	RSVP

		POST /api/events/{event_id}/rsvp/ - RSVP to an event
		PATCH /api/events/{event_id}/rsvp/{user_id}/ - Update RSVP status
	

	Reviews

		POST /api/events/{event_id}/reviews/ - Add a review for an event
		GET /api/events/{event_id}/reviews/ - List all reviews for an event



Testing
To run tests, use:
		python manage.py test api


