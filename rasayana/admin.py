from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Appointment
# Unregister default User admin
admin.site.unregister(User)

# Create custom UserAdmin
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Columns shown in Users list
    list_display = (
        'username',
        'email',
        'is_superuser',
        'is_staff',
        'is_active',
    )

    # Optional: make columns clickable
    list_display_links = ('username', 'email')

    # Remove first_name & last_name from list view
    ordering = ('username',)

from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
        'submitted_at',
    )
    list_filter = ('submitted_at',)
    search_fields = ('name', 'email', 'phone')
    ordering = ('-submitted_at',)

    @admin.register(Appointment)
    class AppointmentAdmin(admin.ModelAdmin):
        list_display = (
            'patient_name',
            'age',
            'specialist',
            'preferred_date',
            'phone',
            'created_at',
        )
        list_filter = ('specialist', 'preferred_date')
        search_fields = ('patient_name', 'phone')