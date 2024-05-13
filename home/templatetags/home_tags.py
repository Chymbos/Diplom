from django import template
import home.views as views

from home.utils import menu

register = template.Library()

@register.simple_tag
def get_menu():
    return menu