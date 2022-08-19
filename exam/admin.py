from django.contrib import admin
from .models import *

class ConductExamAdmin(admin.ModelAdmin):
      list_display = ['enrollment_no','student_name','exam_title','start_date_time']
admin.site.register(ConductExam, ConductExamAdmin)

class CollectExamAdmin(admin.ModelAdmin):
      list_display = ['enrollment_no','student_name','code','submission_time']
admin.site.register(CollectExam, CollectExamAdmin)

class ExamControlAdmin(admin.ModelAdmin):
      list_display = ['start_exam','start_submission','end_exam']
admin.site.register(ExamControl, ExamControlAdmin)




