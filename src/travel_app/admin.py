from django.contrib import admin
from .models import User, Memory, Comment

admin.site.register(User)
admin.site.register(Memory)
admin.site.register(Comment)