from django.contrib import admin

# Register your models here.

from .models import Institution, Course, GradRate


class CourseInline(admin.TabularInline):
    model = Course
    extra = 3

class GradRateInline(admin.TabularInline):
    model = GradRate
    extra = 2

class InstitutionAdmin(admin.ModelAdmin):
    inlines = [CourseInline,GradRateInline]

admin.site.register(Institution, InstitutionAdmin)
