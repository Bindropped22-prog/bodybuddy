from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('planner.urls')),  # Make sure this is pointing to the planner app URLs
]
