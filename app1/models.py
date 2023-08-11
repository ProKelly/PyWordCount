from django.db import models

class UserText(models.Model):
    username = models.CharField(max_length=200)
    message = models.TextField(max_length=1000000000000000000000000000000000000000000000)
    date_written = models.DateTimeField(auto_now_add=True)

class UserFile(models.Model):
    username = models.CharField(max_length=200)
    file = models.FileField(upload_to='uploads/')
    date_uploaded = models.DateTimeField(auto_now_add=True)