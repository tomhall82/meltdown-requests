from django.urls import path
from . import views

urlpatterns = [
    path('request_form/', views.request_form, name='request_form'),
    path('request_list/', views.request_list, name='request_list'),
    path('delete-request/<int:request_id>/', views.delete_request, name='delete_request'),  # URL for deleting individual requests
    path('delete-all/', views.delete_all_requests, name='delete_all_requests'),
]
