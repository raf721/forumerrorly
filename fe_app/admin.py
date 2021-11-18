from django.contrib import admin
from .models import Thread, Post, Comment

# Register your models here.

admin.site.register(Thread)
admin.site.register(Post)
admin.site.register(Comment)