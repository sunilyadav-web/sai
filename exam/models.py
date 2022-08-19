from django.db import models

class ConductExam(models.Model):
    enrollment_no=models.CharField(max_length=40,unique=True)
    student_name=models.CharField(max_length=40)
    exam_title=models.CharField(max_length=40)
    paper=models.FileField()
    code=models.CharField(max_length=30)
    note=models.TextField(max_length=500,default='Instruction')
    start_date_time=models.DateTimeField()
    end_date_time=models.DateTimeField()

class CollectExam(models.Model):
    enrollment_no=models.CharField(max_length=40,unique=True)
    student_name=models.CharField(max_length=40)
    answer=models.FileField()
    code=models.CharField(max_length=30)
    submission_time=models.DateTimeField(auto_now_add=True)

class ExamControl(models.Model):
    start_exam=models.BooleanField(default=False)
    start_submission=models.BooleanField(default=False)
    end_exam=models.BooleanField(default=False)
    
    