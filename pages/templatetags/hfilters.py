from django.template import Library

register = Library()


@register.filter
def return_a(val):
    return f'{val}'.replace('a', 'b')
