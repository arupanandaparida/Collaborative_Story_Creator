from django.contrib import admin
from .models import Story

class StoryAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'created_at', 'snippet')
    search_fields = ('title', 'content')
    readonly_fields = ('created_at', 'snippet')

    def snippet(self, obj):
        return obj.snippet

    snippet.short_description = 'Content Snippet'

admin.site.register(Story, StoryAdmin)

