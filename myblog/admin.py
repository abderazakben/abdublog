from django.contrib import admin
from .models import Post,Category , Profile , Comment,Admin

# Register your models here.

admin.site.register([Admin,Post , Category , Profile , Comment])
