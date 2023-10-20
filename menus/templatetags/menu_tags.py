from django import template
from ..models import MenuItem

register = template.Library()

def get_menu(menu_name):
    return MenuItem.objects.filter(menu_name=menu_name)

@register.inclusion_tag('menus/menu_template.html')
def draw_menu(menu_name, current_url, parent_id=None):
    menu_items = get_menu(menu_name).filter(parent_id=parent_id)
    for item in menu_items:
        item.has_active_child = item.url == current_url or draw_menu(menu_name, current_url, parent_id=item.id)
    return {'menu_items': menu_items, 'current_url': current_url}