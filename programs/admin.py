from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin



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


class InstitutionResource(resources.ModelResource):
    class Meta:
        model = Institution

class InstitutionAdmin(ImportExportModelAdmin):
    inlines = [CourseInline,InstructorInline,GradRateInline]
    resource_class = InstitutionResource



admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Course)
admin.site.register(Instructor)
