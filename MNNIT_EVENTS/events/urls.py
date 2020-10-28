from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('' , views.index , name='index'),
    path('developers',views.developers, name='developers'),
    path('profile',views.profile, name = 'profile'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('details/<int:evId>',views.details,name='details'),
    path('details/payment/<int:evId>',views.payment,name='payment'),
    path('sendQuery',views.sendQuery,name="sendQuery"),
    path('details/requestCA/<int:evId>',views.requestCA,name='requestCA'),
    path('details/userList/<int:evId>',views.userList,name='userList'),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="reset_password.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="new_password_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_done.html"), 
        name="password_reset_complete"),

    path('details/userList/sendRequest/<int:user_id>/<int:evId>',views.sendRequest,name='sendRequest'),
    path('details/userList/sendReminder/<int:user_id>/<int:evId>',views.sendReminder,name='sendReminder'),
]


