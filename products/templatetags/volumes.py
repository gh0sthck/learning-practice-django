from django import template

register = template.Library()

@register.filter()
def get_value_from_dict(dict, key):
    return dict.get(key)
