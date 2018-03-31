from django.contrib import admin

from applications.ads.models import Ad


@admin.register(Ad)
class CategoryAdmin(admin.ModelAdmin):

    fields = ('subject', 'message', 'location', 'category', 'user', 'image')

