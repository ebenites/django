from django.contrib import admin

# Register your models here.
from .models import Page

class PageAdmin(admin.ModelAdmin):
        readonly_fields = ('created', 'updated')
        list_display = ('title', 'order', 'created', 'updated')
        ordering = ('-created', )

admin.site.register(Page, PageAdmin)