from django.shortcuts import render_to_response
from django.http import Http404
from django.template import RequestContext
from blog.models import Entry
import logging

logger = logging.getLogger(__name__)

def home(request):
  last_entry_list = Entry.objects.filter(state='P').order_by('-published')[:10]
  return render_to_response('blog/home.html', { 'entries': last_entry_list })

def entry(request, slug):
  logger.debug('slug: %s' % slug)

  try:
    entry = Entry.objects.get(slug=slug, state='P')
  except Entry.DoesNotExist:
    raise Http404

  return render_to_response('blog/entry.html', RequestContext(request, { 'entry': entry }))

