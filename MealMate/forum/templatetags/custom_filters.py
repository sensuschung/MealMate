from django import template
from django.utils.timesince import timesince
import random

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

@register.filter
def random_avatar(_):
    """随机选择一个默认头像文件名"""
    avatars_cat = [f'cat{i}.png' for i in range(1, 15)]
    avatars = avatars_cat
    return random.choice(avatars)
