from django.urls import path
from .views import *
app_name='exam'
urlpatterns = [
    path('',home,name='home'),
    path('start/',examStart,name="exam-start"),
    path('submission',examSubmission,name='exam-submission'),
]
