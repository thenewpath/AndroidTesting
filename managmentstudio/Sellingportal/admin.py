from django.contrib import admin

# Register your models here.
from Sellingportal.models import Student, Degree

admin.site.register(Student)
admin.site.register(Degree)