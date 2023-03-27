from django.urls import path
from . import views

urlpatterns=[
    path('',views.html_1,name="html_1"),
    path('home.html',views.html_1,name="html_1"),
    path('predict.html',views.html_2,name="html_2"),
    path('predict2.html',views.read,name="read"),

]