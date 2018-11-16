from django.contrib import admin

# Register your models here.
from .models import Link

class LinkAdmin(admin.ModelAdmin):
        readonly_fields = ('created', 'updated')
        list_display = ('key', 'name', 'url', 'created', 'updated')
        ordering = ('-created', )

        # Sobreescribir readonly_fields
        def get_readonly_fields(self, request, obj=None):
                if request.user.groups.filter(name="Personal").exists():
                        return ('key', 'name')
                else:
                        return  ('created', 'updated')

admin.site.register(Link, LinkAdmin)
