from django.contrib import admin
from .models import Course, Student,Enrollment

# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_date', 'end_date')
    search_fields = ('title',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'joined_date')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('joined_date',)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'enrollment_date')
    list_filter = ('enrollment_date','course')
    search_fields = ('student__first_name', 'student__last_name', 'course__title')