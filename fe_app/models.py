from django.db import models

# Create your models here.

class Thread(models.Model):
    """A thread where users can discuss a topic."""
    text = models.CharField(max_length=200)                 # can add more fields here later! check Django Model Field Ref
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns string of model."""
        return self.text

class Post(models.Model):
    """User post about a thread."""
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)  # connects post to thread, deletes entire thread
    text = models.TextField()   # no char limit for posts
    date_added = models.DateTimeField(auto_now_add=True)    # shows timestamp for post 

    """ May not need this!
    class Meta:
        # Extra information for managing Post model.
    """

    def __str__(self):
        """Return a string of the model. Preview is limited to first 50 chars of post."""
        return f"{self.text[:50]}..." if len(self.text) > 50 else f"{self.text}"    # only shows ellipsis if post > 50 chars