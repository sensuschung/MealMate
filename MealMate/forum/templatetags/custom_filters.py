from django import template
from django.utils.timesince import timesince

register = template.Library()

@register.filter
def time_ago(value):
    time_difference = timesince(value)
    units = {
        'days': 'd',
        'hours': 'h',
        'minutes': 'min',
        'seconds': 's'
    }
    for long_unit, short_unit in units.items():
        if long_unit in time_difference:
            number = time_difference.split()[0]
            return f"{number}{short_unit} ago"
    return "just now"
