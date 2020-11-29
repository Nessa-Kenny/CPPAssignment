from django.contrib import admin

# Register your models here.
from .models import Add_Recipe,Entry
admin.site.register(Add_Recipe)
admin.site.register(Entry)