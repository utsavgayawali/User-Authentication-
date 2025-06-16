from django.contrib import admin
from django.urls import path,include
from main import views


urlpatterns = [
    path('admin/', admin.site.urls),
     path('register/', views.register, name='register'),
     path('home/', views.home, name='home'),
    #  path('reset/<str:user_email>', views.reset, name='reset'),
     path('login_view/', views.login_view, name='login_view'),
     path('logout/', views.user_logout, name='logout'),
     path('email_view/', views.email_view, name='email_view'),
     path('otp_view/', views.otp_view, name='otp_view'),

    #   path('password_reset/',
    #      auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
    #      name='password_reset'),
    # path('password_reset/done/',
    #      auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
    #      name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
    #      name='password_reset_confirm'),
    # path('reset/done/',
    #      auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
    #      name='password_reset_complete'),

]