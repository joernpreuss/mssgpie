from django.contrib import admin
from .models import Message, Category


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'date', 'created_at', 'text_preview')
    list_filter = ('sender', 'date', 'created_at')
    search_fields = ('text', 'sender')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Message Details', {
            'fields': ('text', 'sender', 'date')
        }),
        ('Metadata', {
            'fields': ('metadata', 'created_at'),
            'classes': ('collapse',)
        }),
    )

    def text_preview(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_preview.short_description = 'Text Preview'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'pattern_count')
    search_fields = ('name',)

    def pattern_count(self, obj):
        return len(obj.patterns)
    pattern_count.short_description = 'Number of Patterns'
