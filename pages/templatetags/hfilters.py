from django.template import Library
from html import unescape

register = Library()


@register.filter
def return_a(val):
    a = unescape('&#x1d504;')
    return f'{val}'.replace('a', a)
