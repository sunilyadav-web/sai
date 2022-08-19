from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from student.models import *
from .models import *
# Create your views here.
def home(request):
    context={}
    try:
        x2=ResultStyleHideUnHide.objects.get(id=1)
        ec=ExamControl.objects.latest('id')
    except Exception as e:
        print('Exam Home Exception : ',e)
    return render(request,'exam/exam.html',{'x2':x2,'ec':ec})

def examStart(request):
    context={}
    ec=ExamControl.objects.latest('id')
    if ec.start_exam:
        x2=ResultStyleHideUnHide.objects.get(id=1)
        context['x2']=x2
        if request.method == 'POST':
            enrollment_no=request.POST['enrollment_no']
            try:
                exam_obj=ConductExam.objects.get(enrollment_no=enrollment_no)
                if exam_obj:
                    start_time=exam_obj.start_date_time
                    end_time=exam_obj.end_date_time
                    time=end_time-start_time
                    context['exam_obj']=exam_obj
                    context['time']=time
            except:
                messages.error(request,'Enrollment Not found')
                
        return render(request,'exam/start_exam.html',context)
    else:
        messages.warning(request,'exam will start soon!')
    return redirect('exam:home')

def examSubmission(request):
    context={}
    try:
        x2=ResultStyleHideUnHide.objects.get(id=1)
        context['x2']=x2
        ec=ExamControl.objects.latest('id')
        context['ec']=ec
        
        if ec.start_submission:
            
            if request.method == 'POST':
                enrollment_no=request.POST['enrollment_no']
                exam_code=request.POST['exam_code']
                stundent_name=request.POST['student_name']
                answer_file=request.FILES['answer']

                if enrollment_no and exam_code and stundent_name and answer_file != '':
                    en=CollectExam.objects.filter(enrollment_no=enrollment_no)
                    if en:
                        messages.warning(request,'You have already submitted Exam Paper!')
                    else:
                        e=CollectExam.objects.create(enrollment_no=enrollment_no,student_name=stundent_name,answer=answer_file,code=exam_code)
                        messages.success(request,'Your Exam Paper submitted successfuly!')
                    return redirect('exam:home')      
                
            return render(request,'exam/exam_submission.html',context)
        elif ec.end_exam:
            messages.warning(request,"Exam submission time has been over You can't submit Now!")
            return redirect('/')
        else:
            messages.warning(request,'Examination Submission will start soon!')
            return render(request,'exam/exam_submission.html',context)
    except Exception as e:
        print('exam Submission Exception : ',e)
        messages.warning(request,'Something went wrong!')
    return redirect('exam:home')
