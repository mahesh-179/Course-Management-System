from django.contrib import admin
from .models import Student,Course,Enrollment
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','phone','age','address']
admin.site.register(Student,StudentAdmin)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','course_name','description','duration','fee','is_available']
admin.site.register(Course,CourseAdmin)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['id','student_name','course_name','student_email','course_duration','course_fee']

    def student_name(self,obj):
        return obj.student.name

    def course_name(self,obj):
        return obj.course.course_name

    def student_email(self,obj):
        return obj.student.email

    def course_duration(self,obj):
        return obj.course.duration

    def course_fee(self,obj):
        return obj.course.fee
admin.site.register(Enrollment,EnrollmentAdmin)


