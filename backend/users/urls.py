from django.urls import path
from django.contrib.auth.views import (LoginView, LogoutView,
PasswordChangeDoneView,
PasswordChangeView,
PasswordResetCompleteView,
PasswordResetConfirmView,
PasswordResetDoneView,
PasswordResetView)
from . import views



urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('password_change/',
        PasswordChangeView.as_view(
        template_name='registration/password_change_form.html'),
        name='password_change_form'),
    path('password_change/done/',
        PasswordChangeDoneView.as_view(
        template_name='registration/password_change_done.html'),
        name='password_change_done'),
    path('reset/done/',
        PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'),
        name='reset_complete'),
    path('reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('password_reset/done/',
        PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'),
        name='password_reset_done'),
    path('password_reset/',
        PasswordResetView.as_view(
            template_name='registration/password_reset_form.html'),
        name='password_reset_form'),
]

