from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import  Account

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'email', 'username', 'date_joined', 'is_active',)
    list_display_links = ('email', 'first_name', 'last_name',)
    readonly_fields = ("date_joined",)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)