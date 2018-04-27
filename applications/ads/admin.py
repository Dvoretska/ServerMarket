from django.contrib import admin

from applications.ads.models import Ad


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):

    fields = ('subject', 'message', 'location', 'category', 'user')
    list_display = ('subject', 'message', 'location', 'category', 'user', 'get_images')

    def get_images(self, obj):
        return [image for image in obj.images.all()]
