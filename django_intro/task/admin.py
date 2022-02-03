from django.contrib import admin

from django_intro.task.models import Task


# admin.register(Task)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('title',)
    sortable_by = ('title',)
