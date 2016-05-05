from django.db import models
from django.utils import timezone

# Create your models here.


class Article(models.Model):
    title_en = models.CharField(max_length=250)
    text_en = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title_en
