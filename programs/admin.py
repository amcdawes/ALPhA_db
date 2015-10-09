from django.contrib import admin

# Register your models here.

from .models import Institution, Instructor, Course, GradRate

class InstructorInline(admin.TabularInline):
    model = Instructor
    extra = 3

class CourseInline(admin.TabularInline):
    model = Course
    extra = 3

class GradRateInline(admin.TabularInline):
    model = GradRate
    extra = 2

class InstitutionAdmin(admin.ModelAdmin):
    inlines = [InstructorInline,GradRateInline]

class InstructorAdmin(admin.ModelAdmin):
    inlines = [CourseInline]

admin.site.register(Institution, InstitutionAdmin)
#admin.site.register(Institution)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Course)
