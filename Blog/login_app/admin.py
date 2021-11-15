from django.contrib import admin

# Register your models here.
from login_app.models import User_profile,Follow
admin.site.register(User_profile)
admin.site.register(Follow)