from django.contrib import admin
from .models import Khoj
# Register your models here.
@admin.register(Khoj)
class KhojAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'input_values', 'timestamp']