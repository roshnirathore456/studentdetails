from django.contrib import admin
from .models import Details, TeacherSignUp, StudentSignup, TeacherLogin, StudentLogin

# Register your models here.
admin.site.register(Details)
admin.site.register(TeacherSignUp)
admin.site.register(TeacherLogin)
admin.site.register(StudentSignup)
admin.site.register(StudentLogin)
