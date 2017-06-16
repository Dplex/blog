from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField, 

# Create your models here.

class Post(models.Model):
    def generate_backgroundimageName(self, filename):
        url = "{1}/{0}".format(filename, self.author)
        return url

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    backgroundimage = models.FileField(upload_to=generate_backgroundimageName, null=True)
    htmltext = RichTextField(('Content Of Post'))

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
