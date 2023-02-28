from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Q

# from django.contrib.auth.models import User

User = settings.AUTH_USER_MODEL
# Create your models here.

class Note(models.Model):
    user=models.ForeignKey(User,default=1, null=True, on_delete=models.CASCADE)
    title=models.CharField(max_length=120, blank=False, null=False)
    content = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk', '-updated', '-publish_date',  '-timestamp']

    @property
    def number_of_notes(self):
        return Note.objects.filter(post=self).count()

    def get_absolute_url(self):
        return f'/notes/{self.id}'