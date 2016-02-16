from django.contrib import admin
from blog.models import Category, BlogEntry


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
    }

    list_display = ('name', 'slug')


class BlogEntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',),
    }

    list_display = ('created_at', 'published_at', 'title', 'draft')
    list_display_links = ('title',)
    list_filter = ('created_at', 'published_at', 'draft')
    date_hierarchy = 'created_at'
    search_fields = ('title', 'tease', 'body')

    exclude = ('created_at',)
    fieldsets = (
        (None, {'fields': ('slug', 'title', 'tease', 'body', 'image')}),
        ('Properties', {'fields': ('draft', 'published_at', 'category')}),
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogEntry, BlogEntryAdmin)
