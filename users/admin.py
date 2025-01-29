from django.contrib import admin
from .models import CustomUser, UserMemories


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'profile_image', 'ssc_batch', 'designation', 'phone_number', 'address', 'age')
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserMemories)

# Register your models here.
