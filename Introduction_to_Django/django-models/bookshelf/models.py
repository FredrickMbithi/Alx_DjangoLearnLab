from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} — {self.author} ({self.publication_year})"
