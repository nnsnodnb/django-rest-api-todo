from django.contrib import admin
from .models import ApiTask

@admin.register(ApiTask)
class ApiTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'schedule_date', 'finish_date', 'rank', 'finish_check')
    list_display_link = ('id', 'title')
