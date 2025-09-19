from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    message = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        db_table = "notification"

    def __str__(self):
        return f"Notif → {self.user.username} ({'Leída' if self.is_read else 'No leída'})"
