from django.db import models
from django.utils import timezone
from django.utils.dateparse import parse_datetime


class Rodada(models.Model):
    title = models.CharField(max_length=256)
    date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    drive = models.URLField(null=True, blank=True)
    presentation = models.URLField(null=True, blank=True)
    recording = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.date}"
