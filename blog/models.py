from django.db import models

# Create your models here.
class Post(models.Model): 
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return "{0}".format(self.name)
