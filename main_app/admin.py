from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Goal, Category, Course, Note

# https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#extending-the-existing-user-model

# Register your models here.
class GoalInline(admin.StackedInline):
    model = Goal
    can_delete = False

class UserAdmin(BaseUserAdmin):
# https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#inlinemodeladmin-objects
    inlines = [GoalInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Category) 
admin.site.register(Course)
admin.site.register(Goal)
admin.site.register(Note)