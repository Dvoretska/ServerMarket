from django.contrib import admin

from applications.ads.models import Ad


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):

    fields = ('subject', 'message', 'location', 'category', 'user', 'image')
    list_display = ('subject', 'message', 'location', 'category', 'user', 'image')


