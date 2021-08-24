from django.db import models

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.TextField()
    img_url = models.URLField(default='http://placekitten.com/g/200/300')