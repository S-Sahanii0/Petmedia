from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name= "account"
urlpatterns = [
   
    path("register/", views.register, name= "register"),
    path("logout/", views.logout_view, name= "logout"),
    path("login/", views.login_view, name= "login"),
    path("profile/", views.displayProfile, name= "profile"),
    path("updateProfile/", views.updateProfile, name= "updateProfile"),
    path("reset_password/", auth_views.PasswordResetView.as_view(template_name="account/password_reset.html"), name="reset_password"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="account/sent.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="account/reset_pw.html"), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="account/complete.html"), name="passwprd_reset_complete"),
    path("password_change/", auth_views.PasswordChangeView.as_view(template_name = "account/pw_change.html"), name = "password_change"),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(template_name = "account/pw_done.html"), name = "password_change_done"),

]