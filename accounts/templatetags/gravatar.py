import hashlib
from django import template

register = template.Library()

@register.filter
def makemd5(email):
    return hashlib.md5(email.encode('utf-8').lower().strip()).hexdigest()