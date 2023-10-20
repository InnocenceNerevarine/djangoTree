from django.shortcuts import render
from .models import MenuItem


def my_view(request):
    current_url = request.path
    main_menu = MenuItem.objects.filter(menu_name='main_menu')
    return render(request, 'menus/base.html', {'main_menu': main_menu, 'current_url': current_url})
