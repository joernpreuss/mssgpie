from django.db import models


class Message(models.Model):
    """Message model for storing and parsing messages."""
    text = models.TextField()
    sender = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.sender or 'Unknown'} at {self.created_at}"


class Category(models.Model):
    """Category model for message classification."""
    name = models.CharField(max_length=255, unique=True)
    patterns = models.JSONField(default=list)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
