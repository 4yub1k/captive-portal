from django.contrib import admin
from .models import LoginData

class IndexAdmin(admin.ModelAdmin):
    list_display=('id','username','password')
    list_display_link=('')
admin.site.register(LoginData, IndexAdmin)