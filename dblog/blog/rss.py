from django.contrib.syndication.views import Feed
from blog.models import Entry
from markdown import markdown

class EntriesFeed(Feed):
  title = "RSS"
  link = "/feed/"
  description = "extra credit?"

  def items(self):
    return Entry.objects.filter(state='P').order_by('-created')

  def item_title(self, item):
    return item.title

  def item_link(self, item):
    return '/%s' % item.slug

  def item_description(self, item):
    return markdown(item.body)

  def item_author_name(self, item):
    return '%s %s' % (item.author.first_name, item.author.last_name)

  def item_author_email(self, item):
    return item.author.email

  def item_pubdate(self, item):
    return item.created
