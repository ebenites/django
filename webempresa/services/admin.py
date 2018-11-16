from django.contrib import admin

# Register your models here.
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
        readonly_fields = ('created', 'updated')
        list_display = ('title', 'subtitle', 'image', 'created', 'updated')

admin.site.register(Service, ServiceAdmin)
