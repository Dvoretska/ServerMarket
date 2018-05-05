from django.contrib import admin

from applications.accounts.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

    fields = ('username', 'email', 'first_name', 'last_name', 'country', 'city', 'phone')
