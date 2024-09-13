from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'date_joined', 'is_superuser')
    search_fields = ('name',  'address', 'email')
    readonly_fields = ('date_joined',)
    ordering = ('name',)
