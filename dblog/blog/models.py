from django.db import models

class Post(models.Model):
  slug = models.SlugField()
  date = models.DateTimeField(auto_now=True)
  title = models.CharField(max_length=511)
  body = models.TextField()

  def __unicode__(self):
    return '\nDate: %s\nSlug: %s\nTitle: %s\nBody: %s' % (self.date, self.slug, self.title, self.body)

class Comment(models.Model):
  date = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=255, verbose_name="Full Name")
  email = models.EmailField(verbose_name="Email Address")
  ip = models.IPAddressField(editable=False, verbose_name="IP Address")
  body = models.TextField()
  post = models.ForeignKey(Post)

  def __unicode__(self):
    return '\nDate: %s\nName: %s\nEmail: %s\nIP: %s\nBody: %s' % (self.date, self.name, self.email, self.ip, self.body)
