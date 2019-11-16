from django.contrib import admin
from . import models
# Register your models here.

class key_admin(admin.ModelAdmin):
    search_fields = ['user_created','site','key','text']
    list_filter = ['user_created','site','key']
    list_display = ['user_created','key','site','time']

admin.site.register(models.key,key_admin)