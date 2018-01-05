# encoding:utf-8
from django import template
from django.utils.safestring import mark_safe
from django.template.base import resolve_variable, Node, TemplateSyntaxError

register = template.Library()

@register.filter
def eng_month(value):
    month = ['January','February','March','April','May','June','July','Aguest','September','October','November','December']
    return month[int(value) - 1]

