from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    decription = models.TextField(max_length=300)
    date = models.DateField()