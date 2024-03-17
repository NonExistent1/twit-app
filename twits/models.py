from django.conf import settings
from django.db import models
from django.urls import reverse

class Twit(models.Model):
    """Twit Post"""

    body = models.TextField()
    image_url = models.URLField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name = "twits"
    )

    def __str__(self):
        """String Method"""
        return self.body
    
    def get_absolute_url(self):
        return reverse("twit_list")
    
    class Meta:
        ordering = ['-updated']

class Comment(models.Model):
    """Comment Model"""

    twit = models.ForeignKey(Twit, on_delete=models.CASCADE)
    body = models.CharField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        """Convert to string"""
        return self.body
    
    def get_absolute_url(self):
        return reverse("twit_list")
    
    class Meta:
        ordering = ['-updated']
