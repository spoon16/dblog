# simple gravatar template tag

import hashlib
import urllib
from django import template

register = template.Library()

@register.simple_tag
def gravatar_href(email, size=48):
  return 'http://www.gravatar.com/avatar/%s.jpg' % hashlib.md5(email.strip().lower()).hexdigest()
