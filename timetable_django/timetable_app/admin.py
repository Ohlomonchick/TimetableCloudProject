from django.contrib import admin

from .models import Event, Category, CommonGroup
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
admin.site.register(Event)
admin.site.register(Category)
admin.site.register(CommonGroup)
