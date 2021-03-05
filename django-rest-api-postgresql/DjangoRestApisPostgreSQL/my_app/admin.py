from django.contrib import admin
from .models import User, Tutorial, Group

# Register your models here.

admin.site.register(User)
admin.site.register(Tutorial)
admin.site.register(Group)
