from django.db import models
from django.contrib.auth import get_user_model


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(       
        get_user_model(),
        on_delete = models.CASCADE
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.URLField(max_length=200,default='https://picsum.photos/600')
