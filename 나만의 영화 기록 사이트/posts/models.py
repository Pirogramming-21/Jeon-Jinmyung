from django.conf import settings
from django.db import models
from django.utils import timezone


class Review(models.Model):
    title = models.CharField(max_length=200)
    director = models.TextField(default='')
    actors = models.TextField(default='')
    release_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    rating = models.IntegerField()
    runtime = models.TextField(default='')
    content = models.TextField(default='')  # 기본값으로 빈 문자열 설정

    def __str__(self):
        return self.title