from django.urls import  path

from  demo import views

urlpatterns = [

    path('', views.show_subjects, name='show_subjects')
]