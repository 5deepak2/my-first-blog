from django.conf.urls import url
from .import views

# Create your views here.

urlpatterns=[ url(r'^',views.job_list,name='job_list'),
              ]