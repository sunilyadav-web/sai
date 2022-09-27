
from django.core.mail import send_mail
from django.conf import settings
def contactusMail(name,email,contact_no,subject,message):
    print("Contact us Mail")
    print(subject)
    print(email)
    print(contact_no)
    print(name)
    from_email=settings.EMAIL_HOST_USER
    recipient='administrator@saiu-edu.in'
    recipient_list=[recipient]
    print('type',type(recipient))
    message="Name :"+str(name)+"\n Contact No. : "+str(contact_no)+"\n Email : "+str(email)+"\n Message : "+str(message)
    send_mail(subject,message,from_email,recipient_list,fail_silently=True)
    return 'success'



def applyMail(name,email,contact_no,subject,course,query):
    print(subject)
    print(email)
    print(contact_no)
    print(name)
    from_email=settings.EMAIL_HOST_USER
    recipient='administrator@saiu-edu.in'
    recipient_list=[recipient]
    print('type',type(recipient))
    message="Name :"+str(name)+"\n Contact No. : "+str(contact_no)+"\n Email : "+str(email)+"\n Course : "+str(course)+"\n Query : "+str(query)
    send_mail(subject,message,from_email,recipient_list,fail_silently=True)
    return 'success'