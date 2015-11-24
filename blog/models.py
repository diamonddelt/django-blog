from django.db import models
from django.utils import timezone

# Create your models here.

# Model representing a 'Blog Post'
# A class in Python is just an object
# By passing in 'models.Model', we tell this to use the Django model
# definition and save it in the Django database
class Post(models.Model):
    author = models.ForeignKey('auth.User')

    # The following are methods from the Django 'models' class
    # models.CharField() defines a text with limited characters
    title = models.CharField(max_length=200)

    # models.TextField() defines a text with no limits
    text = models.TextField()

    # models.DateTimeField() defines a DateTime value
    created_date = models.DateTimeField(
        default = timezone.now
    )
    published_date = models.DateTimeField(
        blank = True,
        null = True
    )

    # Publish method which updates the pushlished_date var with the current
    # DateTime value and saves the Post object
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # 'Dunder' method - aka 'Double-Underscore'
    def __str__(self):
        return self.title
