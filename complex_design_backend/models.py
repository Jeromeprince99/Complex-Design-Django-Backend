from django.db import models
from datetime import datetime    

class Post(models.Model):
    content = models.TextField()
    time = models.DateTimeField(blank=True, default=datetime.now )
    image =  models.ImageField(upload_to="./images/", blank=True)
    video = models.TextField(blank=True)
    