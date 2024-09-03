from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_feedback, name='submit_feedback'),  # This sets the root URL to the feedback form
    path('success/', views.success_page, name='success_page'),  # URL for the success page after form submission
]
