from django.contrib import admin

from applications.ads.my.models import SavedAd


@admin.register(SavedAd)
class SavedAdmin(admin.ModelAdmin):

    list_display = ('ad', 'user')
