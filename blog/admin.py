from django.contrib import admin

# Register your models here.
from blog.models import Tag, Post, Comment
admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('title',)}
  # exclude = ['content']
  list_display = ['title', 'created_at', 'published_at', 'slug']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)