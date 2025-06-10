from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, StudentProfile

class CustomUserAdmin(UserAdmin):
    # Remove username from add/edit forms
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone')}),
        ('Permissions', {
            'fields': ('user_type', 'is_verified', 'is_active', 'is_staff', 'is_superuser'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'user_type'),
        }),
    )
    
    # Display fields in list view
    list_display = ('email', 'first_name', 'last_name', 'user_type', 'is_staff')
    list_filter = ('user_type', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()

class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'date_of_birth')
    search_fields = ('user__email', 'full_name')
    raw_id_fields = ('user',)

admin.site.register(User, CustomUserAdmin)
admin.site.register(StudentProfile, StudentProfileAdmin)