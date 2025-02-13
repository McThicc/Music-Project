from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("", views.SignUpView.as_view(), name="signup"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("<int:pk>/profile/", views.ProfileView.as_view(), name="profile"),
    path("delete_account/", views.DeleteAccountView.as_view(), name="delete_account"),
]