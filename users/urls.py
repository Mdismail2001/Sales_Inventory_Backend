from django.urls import path
from .views import(
    UserRegistrationView,
    UserLoginView, 
    SendOtpViews,
    VarifyOtpViwes
)



urlpatterns = [
    path("/user-registration", UserRegistrationView.as_view(), name="user-registration"),
    path("/user-login", UserLoginView.as_view(), name="user-login"),
    path("/send-otp", SendOtpViews.as_view(), name="send-otp"),
    path("/verify-otp", VarifyOtpViwes.as_view(), name="verify-otp"),


]
