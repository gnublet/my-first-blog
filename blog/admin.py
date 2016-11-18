from django.contrib import admin
from .models import Post #import Post object from models

# Register your models here.
admin.site.register(Post)#register to make visible on the admin page