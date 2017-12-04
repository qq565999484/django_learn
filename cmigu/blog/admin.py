from django.contrib import admin

# Register your models here.
from .models import Post
#在admin中注册对应的模型 #密码 admin123456
admin.site.register(Post)