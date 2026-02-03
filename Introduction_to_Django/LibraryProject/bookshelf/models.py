from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, blank=True)
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=20, blank=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} — {self.author}" if self.author else self.title
