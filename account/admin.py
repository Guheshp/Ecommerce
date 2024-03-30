from django.contrib import admin
from . models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class CustomAccountAdmin(UserAdmin):
    # Customize how the user model is displayed in the admin interface
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_admin', 'is_superadmin')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','phone_number', 'password1', 'password2'),
        }),
    )

    filter_horizontal = ()
    list_filter = ('is_staff', 'is_active')
    ordering = ['email']

# Register the custom user model with the custom admin class
admin.site.register(Account, CustomAccountAdmin)
