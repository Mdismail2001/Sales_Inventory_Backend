from django.urls import path
from .views import(
    UserRegistrationView,
    UserLoginView, 
    SendOtpViews,
    VarifyOtpViwes,
    ResetPasswordViews,
    UserProfileViews,
    UpdateUserProfileViews
)



urlpatterns = [
    path("/user-registration", UserRegistrationView.as_view(), name="user-registration"),
    path("/user-login", UserLoginView.as_view(), name="user-login"),
    path("/send-otp", SendOtpViews.as_view(), name="send-otp"),
    path("/verify-otp", VarifyOtpViwes.as_view(), name="verify-otp"),
    path("/reset-password", ResetPasswordViews.as_view(), name="reset-password"),
    path("/user-profile", UserProfileViews.as_view(), name="user-profile"),
    path("/user-update", UpdateUserProfileViews.as_view(), name="user-update"),

]
