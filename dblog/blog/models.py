from django.db import models
from django.contrib.auth.models import User


class Document(models.Model):
  STATE_CHOICES = (
      ('P', 'Published'),
      # ('W', 'Pending'),
      ('D', 'Draft'),
      # ('T', 'Trashed'),
    )
  slug = models.SlugField()
  created = models.DateTimeField(auto_now=True)
  last_updated = models.DateTimeField(auto_now=True, verbose_name="Last Updated")
  author = models.ForeignKey(User)
  body = models.TextField()
  state = models.CharField(max_length=1, choices=STATE_CHOICES)

  class Meta:
    abstract = True

class Entry(Document):
  title = models.CharField(max_length=511)
  published = models.DateTimeField(auto_now=True)

