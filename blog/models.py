from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
"""
from django.utils import timezone

class Post(models.model):    #means that the Post is a Django Model, so Django knows that it should be saved in the database.
    author = models.ForeignKey('auth.User') # this is a link to another model
    title = models.CharField(max_length=200) # this is how you define text with a limited number of characters
    text = models.TextField() # this is for long text without a limit. Sounds ideal for blog post content, right?
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)  #this is a date and time.

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):   #we will get a text (string) with a Post title
        return self.title

"""