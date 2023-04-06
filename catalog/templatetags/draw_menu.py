from django.shortcuts import get_object_or_404
from django import template
from ..models import Menu

register = template.Library()
@register.inclusion_tag('catalog/menu.html')
def draw_menu(menu_name):
    if menu_name is None:
        return None
    current_menu = get_object_or_404(Menu, name=menu_name)
    content = {
        'current_menu': menu_name,
        'parents': []
    }
    childs = Menu.objects.filter(parent=current_menu.id)
    if childs.count() > 0:
        grand_childs = Menu.objects.filter(parent=childs[0].id)
        if grand_childs is not None:
            content['grand_childs'] = grand_childs
        content['childs'] = childs

    while current_menu.parent is not None:
        parent_menu = Menu.objects.filter(parent=current_menu.parent)
        current_menu = get_object_or_404(Menu, pk=current_menu.parent.id)
        content['parents'].append(parent_menu)
    content['parents'].reverse()
    return {
        'content': content
    }