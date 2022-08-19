from django.urls import path
from student import views

urlpatterns = [
    path('result/', views.result,name='result'),
    path('faith/', views.faith,name='faith'),
    path('about/', views.about,name='about'),
    path('md_message/', views.md_message,name='md_message'),
    path('courses', views.courses,name='courses'),
    path('health_science_courses/', views.health_science_courses,name='health_science_courses'),
    path('engineering_courses/', views.engineering_courses,name='engineering_courses'),
    path('management_courses/', views.management_courses,name='management_courses'),
    path('certified_courses/', views.certified_courses,name='certified_courses'),
    path('alumini/', views.alumini,name='alumini'),
    path('academics/', views.academics,name='academics'),
    path('library/', views.library,name='library'),
    path('research/', views.research,name='research'),
    path('global_option/', views.global_option,name='global_option'),
    path('student_life/', views.student_life,name='student_life'),
    path('contact_us/', views.contact_us,name='contact_us'),
    path('apply/', views.apply,name='apply'),
    path('', views.home2,name='home2'),
    path('export/', views.export,name='export'),
    path('import/', views.import_data,name='import'),

    path('certificate/',views.certificate,name='certificate'),
    path('certification-pdf/<str:en_no>/',views.certificate_render_pdf_view,name='certification-pdf-view'),
    
    path('admitcard/',views.admitcard,name='admitcard'),
    path('admit-pdf/<str:en_no>/',views.admit_render_pdf_view,name='admit-pdf-view'),

    path('idcard/',views.idcard,name='idcard'),
    path('idcard-pdf/<str:en_no>/',views.idcard_render_pdf_view,name='idcard-pdf-view'),

]
