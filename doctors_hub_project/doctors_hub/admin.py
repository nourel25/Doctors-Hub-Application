from django.contrib import admin
from .models import Specialization, Area, Doctor

# Register your models here.
admin.site.register(Specialization)
admin.site.register(Area)
admin.site.register(Doctor)