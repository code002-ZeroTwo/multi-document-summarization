# models .py file

from django.db import models

# Create your models here.

# create model to save news from news_data api

class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null = True, blank = True)
    url = models.URLField(null=True, blank=True)
    publishedAt = models.DateTimeField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=100,null=True, blank=True)