"""
API models configuration.
"""

from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title