from django.contrib import admin
from student.models import *


admin.site.register(Certificate)
admin.site.register(IdCard)

admin.site.register(ResultHideUnHide)
admin.site.register(ResultStyleHideUnHide)
admin.site.register(SiteDown)

# from import_export.admin import ImportExportModelAdmin


# Register your models here.

admin.site.register(Contact)
admin.site.register(Apply)
admin.site.register(Course_desc)
admin.site.register(UserEnrollment)
admin.site.register(ExamAndAccountHide)


class Sem1Admin(admin.TabularInline):
    model = Semester

class admitexam(admin.TabularInline):
    model = AdmitcardExmDetail

class AdmitCardAdmin(admin.ModelAdmin):
    inlines = [admitexam]
    list_display = ['enrollment_no','name']

admin.site.register(AdmitCard,AdmitCardAdmin)



class ProfileAdmin(admin.ModelAdmin):
    # inlines = [Sem1Admin,Sem2Admin,Sem3Admin,Sem4Admin,Sem5Admin,Sem6Admin]
    inlines = [Sem1Admin]
    list_display = ['enrollment_no','name','father_name','course','specialization','academic_year','year_of_passing','created_at','updated_at']

admin.site.register(Profile,ProfileAdmin)


