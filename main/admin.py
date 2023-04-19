from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Tag, Task


class TaskManagerAdminSite(admin.AdminSite):
    pass


task_manager_admin_site = TaskManagerAdminSite(name="Task manager admin")


@admin.register(Tag, site=task_manager_admin_site)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(Task, site=task_manager_admin_site)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "creation_date",
        "modification_date",
        "due_date",
        "status",
        "author",
        "performer",
        "priority",
    )
    list_editable = (
        "status",
        "priority",
        "performer",
    )


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ["username", "email", "first_name", "last_name", "role"]
    list_filter = ["role"]
    add_fieldsets = (*UserAdmin.add_fieldsets, ("Custom fields", {"fields": ("role",)}))
    fieldsets = (*UserAdmin.fieldsets, ("Custom field", {"fields": ("role",)}))
    list_editable = ("role",)


task_manager_admin_site.register(User, CustomUserAdmin)
