from django.shortcuts import render_to_response
from django.http import Http404
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Entry
import logging

logger = logging.getLogger(__name__)

def home(request):
  entries = Entry.objects.filter(state='P').order_by('-published')
  p = Paginator(entries, 2)

  try:
    current_page = int(request.GET.get('page'))
  except TypeError:
    current_page = 1
  except ValueError:
    current_page = 1

  try:
    entry_page = p.page(current_page)
  except EmptyPage:
    current_page = p.num_pages
    entry_page = p.page(current_page)

  return render_to_response('blog/home.html', RequestContext(request, { 'page_range': p.page_range, 'current_page': current_page, 'entry_page': entry_page }))

def entry(request, slug):
  logger.debug('slug: %s' % slug)

  try:
    entry = Entry.objects.get(slug=slug, state='P')
  except Entry.DoesNotExist:
    raise Http404

  return render_to_response('blog/entry.html', RequestContext(request, { 'entry': entry, 'detail': True }))

