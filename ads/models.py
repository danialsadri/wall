from django.db import models
from django.conf import settings
from django.utils.timezone import now


class Ad(models.Model):
    publisher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ads', blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='ad_images/')
    created = models.DateTimeField(default=now)
    is_public = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created']
        indexes = [models.Index(fields=['-created'])]
        get_latest_by = 'created'

    def __str__(self):
        return self.title
