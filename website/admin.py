from django.contrib import admin

# Register your models here.

from .models import Record 

# We need to register on the admin size
admin.site.register(Record)

