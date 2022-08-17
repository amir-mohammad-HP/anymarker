from django.contrib import admin
from models import models
from django.utils.html import format_html

class ImageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="200px" />'.format(obj.image.url))

    image_tag.short_description = 'Image Preview'
    readonly_fields = ['image_tag']

admin.site.register(models.Collection)
admin.site.register(models.Mark)
admin.site.register(models.URL)
admin.site.register(models.NOTE)
admin.site.register(models.IMAGE, ImageAdmin)