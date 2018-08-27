"""Models file to define schemas."""
from django.db import models


class LookUp(models.Model):
    """Model class for Lookup instance."""

    url = models.URLField(max_length=500)
    safe_or_not = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url
