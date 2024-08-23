from django.contrib import admin
from django.utils.html import format_html
from .models import *  # Make sure to import your Image model
# from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# admin.site.unregister(User)  # Unregister the default User admin to customize
# admin.site.register(User, BaseUserAdmin)  # Register the User model again




class ImageAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" width="100" height="100">', obj.image.url)

    image_tag.short_description = 'Image'
    list_display = ['name', 'image_tag']

admin.site.register(Image, ImageAdmin)
admin.site.register(House)
admin.site.register(Service)
