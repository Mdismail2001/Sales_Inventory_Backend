from django.contrib import admin
from django.urls import path, include

api_urlspatterns = [
    path('',include("users.urls")),
    path('',include("categories.urls")),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', include(api_urlspatterns)),
    
]
