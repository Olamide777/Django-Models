from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.

class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, )
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()
