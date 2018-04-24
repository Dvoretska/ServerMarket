from django.contrib import admin

from .models import Category
from mptt.admin import MPTTModelAdmin


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):

    fields = ('name_ru', 'name_en', 'parent')
    list_display = ('name_ru', 'name_en', 'slug', 'parent')
