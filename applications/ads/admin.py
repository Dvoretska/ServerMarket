from django.contrib import admin

from applications.ads.models import Ad, AdImageModel


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):

    fields = ('subject', 'message', 'location', 'category', 'user', 'price', 'is_vip')
    list_display = ('subject', 'message', 'location', 'category', 'user', 'get_images', 'slug', 'is_vip')

    def get_images(self, obj):
        return [image for image in obj.images.all()]


@admin.register(AdImageModel)
class AdImageAdmin(admin.ModelAdmin):

    fields = ('image', 'ad')
    list_display = ('pk', 'image', 'ad')
    list_filter = ('ad',)

