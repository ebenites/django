from django.contrib import admin

# Register your models here.
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
        readonly_fields = ('created', 'updated')
        list_display = ('name', 'created', 'updated')

admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
        readonly_fields = ('created', 'updated')
        list_display = ('title', 'author', 'published', 'image', 'post_categories', 'created', 'updated')
        ordering = ('-created', )
        search_fields = ('title', 'content', 'author__username', 'categories__name')
        date_hierarchy = 'published'
        list_filter = ('author__username', 'categories__name')

        # Columna personalizada
        def post_categories(self, obj):
            return ", ".join([c.name for c in obj.categories.all().order_by("name")])
            
        post_categories.short_description = "Categorías"
        
admin.site.register(Post, PostAdmin)
