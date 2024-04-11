from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile, Category, Course, Note

# https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#extending-the-existing-user-model

# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
# https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#inlinemodeladmin-objects
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Category) 
admin.site.register(Course)
admin.site.register(Profile)
admin.site.register(Note)