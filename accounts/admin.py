from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username", "age", "is_staff"]
    add_fieldsets = UserAdmin.add_fieldsets + (         # add fields to new user form
        (None, {'fields': ('age',)}),
    )
    fieldsets = UserAdmin.fieldsets + (         # add fields to edit user form
        (None, {'fields': ('age', )}),
    )

admin.site.register(CustomUser, CustomUserAdmin)