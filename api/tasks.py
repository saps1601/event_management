from celery import shared_task

@shared_task
def send_event_update(email, event_title):
    # Logic to send an email (you can integrate with Django's email system)
    print(f'Sent update about {event_title} to {email}')
