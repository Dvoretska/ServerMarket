from django.contrib import admin

from .models import Category
from mptt.admin import MPTTModelAdmin


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):

    fields = ('name', 'parent')
    list_display = ('name', 'slug', 'parent')
