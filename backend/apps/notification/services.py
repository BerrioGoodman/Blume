from .models import Notification
from django.contrib.auth.models import User

class NotificationService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NotificationService, cls).__new__(cls)
        return cls._instance

    def send_notification(self, user: User, message: str):
        """Send a notification to a user"""
        Notification.objects.create(user=user, message=message)
        # Here you could add email sending, push notifications, etc.

    def mark_as_read(self, notification_id: int, user: User):
        """Mark a notification as read"""
        notification = Notification.objects.get(id=notification_id, user=user)
        notification.is_read = True
        notification.save()

# Singleton instance
notification_service = NotificationService()