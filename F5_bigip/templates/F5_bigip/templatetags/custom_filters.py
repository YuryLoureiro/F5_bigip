from django import template
from django.urls import reverse

register = template.Library()

@register.filter
def viewname(name):
    try:
        return reverse(name)
    except:
        return ''