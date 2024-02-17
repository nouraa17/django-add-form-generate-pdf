from django.urls import path,include
from . import views

app_name='digizilla'

urlpatterns = [
    path('', views.digizilla_list, name='digizilla_list'),
    path('detail/<int:pk>/', views.digizilla_detail, name='digizilla_detail'),
    path('form/', views.digizilla_form, name='digizilla_form'),
    path('generate-pdf/', views.generate_pdf_report, name='generate_pdf'),
    
]