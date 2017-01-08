from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

class Trip(models.Model):
    scr_id = models.CharField(max_length=32)
    title = models.CharField(max_length=200)
    started = models.DateTimeField(default=None, blank=True, null=False)
    finished = models.DateTimeField(default=None, blank=True, null=True)
    jb = JSONField(default=None, blank=True, null=True)
    published_date = models.DateTimeField(default=None, blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
