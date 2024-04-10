from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Goal, Category, Course

# Register your models here.
class GoalInline(admin.StackedInline):
    model = Goal
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [GoalInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Goal)