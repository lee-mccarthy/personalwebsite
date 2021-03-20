import os

from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def get_upload_path(instance, filename):
        return os.path.join(
            'games',
            instance.title,
            filename
        )

    data = models.FileField(upload_to=get_upload_path)
    framework = models.FileField(upload_to=get_upload_path)
    loader = models.FileField(upload_to=get_upload_path)
    wasm = models.FileField(upload_to=get_upload_path)

    def __str__(self):
        return self.title
