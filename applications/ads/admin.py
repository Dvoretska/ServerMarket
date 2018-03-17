from django.contrib import admin

from applications.ads.models import Category, Ad


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    fields = ('name', )


@admin.register(Ad)
class CategoryAdmin(admin.ModelAdmin):

    fields = ('subject', 'message', 'location', 'category')

