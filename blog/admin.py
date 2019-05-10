from django.contrib import admin
from .models import Post
from .forms import PostForm

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm
