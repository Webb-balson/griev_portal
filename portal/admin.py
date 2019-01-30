from django.contrib import admin
from .models import Student
from .models import Parent
from .models import Staff

# Register your models here.

admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Staff)



