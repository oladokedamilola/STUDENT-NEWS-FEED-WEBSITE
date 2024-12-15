# models.py
from django.db import models
from django.conf import settings

class CreatorApplication(models.Model):
    title = models.CharField(max_length=200)
    main_content = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reviewed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviewed_applications', null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.user.username}"
