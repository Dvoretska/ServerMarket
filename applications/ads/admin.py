from django.contrib import admin

from applications.ads.models import Category


@admin.register(Category)
class UserProfileAdmin(admin.ModelAdmin):

    fields = ('name', )
