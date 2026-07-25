from django.contrib import admin
from .models import Bookmark,Collection,Tag

class BookmarkAdmin(admin.ModelAdmin):
    list_display=["title","owner","visibility","created_at"]
    list_filter=["visibility","created_at"]
    ordering=["-created_at"]
    search_fields=["title","url"]

class CollectionAdmin(admin.ModelAdmin):
    list_display=["name","owner","created_at"]
    list_filter=["created_at"]
    ordering=["-created_at"]
    search_fields=["name"]

class TagAdmin(admin.ModelAdmin):
    list_display=["name","owner","created_at"]
    list_filter=["created_at"]
    ordering=["-created_at"]
    search_fields=["name"]

admin.site.register(Bookmark,BookmarkAdmin)
admin.site.register(Collection,CollectionAdmin)
admin.site.register(Tag,TagAdmin)

