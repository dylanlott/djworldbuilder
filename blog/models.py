from django.db import models
from django.contrib.auth.models import User

class Post(models.Model): 
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    updated_by=models.ForeignKey(User, related_name='updated_by_user')
    created_by=models.ForeignKey(User, related_name='created_by_user')

    def __str__(self):
        return "{0}".format(self.name)
