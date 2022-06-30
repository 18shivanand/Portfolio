from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    date = models.DateField()

    def __str__(self) -> str:
        return self.title
