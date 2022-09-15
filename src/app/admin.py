from django.contrib import admin
from django.utils.safestring import mark_safe

from app.models import *
# Register your models here.


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("image_view", "title", "date_add", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["status"]
    
    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    image_view.short_description = "Aperçu des images"



@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ("libele", "description", "date_add", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["status"]



@admin.register(Quality)
class QualityAdmin(admin.ModelAdmin):
    list_display = ("image_view", "title", "date_add", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["status"]
    
    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    image_view.short_description = "Aperçu des images"


@admin.register(AskService)
class AskServiceAdmin(admin.ModelAdmin):
    list_display = ("image_view", "title", "date_add", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["status"]
    
    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    image_view.short_description = "Aperçu des images"




@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("image_view", "title", "date_add", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["status"]
    
    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    image_view.short_description = "Aperçu des images"



@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("image_view", "name", "order", "date_add", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["status"]
    
    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    image_view.short_description = "Aperçu des images"
