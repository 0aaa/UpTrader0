from django.shortcuts import get_object_or_404
from django.urls import reverse
from ..models import Menu
from django import template

register = template.Library()
@register.inclusion_tag('catalog/menu.html')
def draw_menu(menu_name='test1'):
    current_menu = get_object_or_404(Menu, name=menu_name)
    parents = []
    childs = Menu.objects.filter(parent=current_menu.id)
    if childs.count() > 0:
        grandChilds = Menu.objects.filter(parent=childs[0].id)
    else:
        grandChilds = []

    parent_menu = current_menu
    while parent_menu.parent is not None:
        parent_menu = get_object_or_404(Menu, pk=parent_menu.parent.id)
        parents.insert(0, parent_menu)
    return {
        'parents': parents,
        'current_menu': current_menu,
        'childs': childs,
        'grandChilds': grandChilds
    }