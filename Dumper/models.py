from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    """ Below attributes will be saved within the DB. """
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=128)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """ Published Date & Time is saved in the post. """
        self.published_date.now()
        self.save()

    def approve_comments(self):
        """ User can filter to see the approved comments on his post.  """
        return self.comments.filter(approved_comments=True)

    def get_absolute_url(self):
        """
            :var 'pk' is a primary key.
            :var - 'post_detail' is the view in view.py file which will be redirected too.
            :returns - Will be redirected to 'post_detail' page once post is created.
        """
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        """ Title will be returned when calling the 'Class'. """
        return self.title


class Comments(models.Model):
    """ Below attributes will be saved within the DB. """
    post = models.ForeignKey('Dumper.Post', related_name='comments', on_delete=models.DO_NOTHING)
    author = models.CharField(max_length=128)
    text = models.TextField(max_length=500)
    create_date = models.DateTimeField(default=timezone.now())
    approved_comments = models.BooleanField(default=False)

    def approve(self):
        """ This method will approve the comment of 'Post' from the user. """
        self.approved_comments = True

    def get_absolute_url(self):
        """ Returning to the homepage of the website which is 'post_list' view """
        return reverse('post_list')

    def __str__(self):
        """ Comment will be returned when calling the 'Class'. """
        return self.text
