from django.contrib import admin

from .models import Item


from mptt.admin import MPTTModelAdmin
from home.models import MenuItem

class MenuItemMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20

admin.site.register(MenuItem, MenuItemMPTTModelAdmin)
admin.site.register(Item)