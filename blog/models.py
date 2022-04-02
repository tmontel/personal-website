from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    teaser = models.TextField(default='', max_length=300)
    description = models.TextField(default='')
    date = models.DateField()
