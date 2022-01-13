from django.contrib import admin
from .models import Index

class IndexAdmin(admin.ModelAdmin):
    list_display=('id','username','password')
    list_display_link=('')
admin.site.register(Index, IndexAdmin)