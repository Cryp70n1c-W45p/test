from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Image

# Register your models here.
@admin.register(Image)
class ImageAdmin(ModelAdmin):
    list_display = ['id', 'photo', 'date']