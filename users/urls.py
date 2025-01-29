from django.urls import path
from .views import UserRegistrationView

urlpatterns = [
    path("/user-registration", UserRegistrationView.as_view(), name="user-registration"),
]
