from django.contrib import admin
from .models import *
# Register your models here.

class LeadsAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'email']


admin.site.register(Lead, LeadsAdmin)

