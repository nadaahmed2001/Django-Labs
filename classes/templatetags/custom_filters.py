from django import template

register = template.Library()

@register.filter(name="multiply")
def multiply(value, arg):
    return value * arg



@register.filter(name='short_description')
def short_description(value):
    if len(value) > 500:
        return value[:500]
    return value