from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('', include('feedback_form.urls')),  # Make feedback_form URLs appear at the root URL
]
