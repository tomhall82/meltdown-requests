from django.urls import path
from . import views

urlpatterns = [
    path('request_form/', views.request_form, name='request_form'),
    path('request_list/', views.request_list, name='request_list'),
    path('delete-all/', views.delete_all_requests, name='delete_all_requests'),
]
