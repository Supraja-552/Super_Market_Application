from django.contrib import admin

# Register your models here.
from app.models import *
admin.site.register(UserProfile)
admin.site.register(Product)
admin.site.register(Employee)