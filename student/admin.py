from django.contrib import admin
from student.models import *


admin.site.register(Certificate)
admin.site.register(IdCard)
admin.site.register(AdmitCard)
admin.site.register(ResultHideUnHide)
admin.site.register(ResultStyleHideUnHide)
admin.site.register(SiteDown)

# from import_export.admin import ImportExportModelAdmin


# Register your models here.

admin.site.register(Contact)
admin.site.register(Apply)
admin.site.register(Course_desc)
admin.site.register(UserEnrollment)


class Sem1Admin(admin.TabularInline):
    model = Semester
        
# class Sem2Admin(admin.TabularInline):
#     model = Semester_2

# class Sem3Admin(admin.TabularInline):
#     model = Semester_3

# class Sem4Admin(admin.TabularInline):
#     model = Semester_4

# class Sem5Admin(admin.TabularInline):
#     model = Semester_5

# class Sem6Admin(admin.TabularInline):
#     model = Semester_6

class ProfileAdmin(admin.ModelAdmin):
    # inlines = [Sem1Admin,Sem2Admin,Sem3Admin,Sem4Admin,Sem5Admin,Sem6Admin]
    inlines = [Sem1Admin]
    list_display = ['enrollment_no','name','father_name','course','specialization','academic_year','year_of_passing']

admin.site.register(Profile,ProfileAdmin)



# @admin.register(Profile)
# class ProfileAdmin(ImportExportModelAdmin):
#     list_display = ['enrollment_no','name','father_name']
#     pass    