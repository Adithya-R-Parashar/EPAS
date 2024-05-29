from django.contrib import admin

from .models import Employee, Metric

# Register your models here.
admin.site.register(Employee)
admin.site.register(Metric)