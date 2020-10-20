from django.contrib import admin
from django.urls import path,include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('' , views.index , name='index'),
    path('developers',views.developers, name='developers'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('details/<int:evId>',views.details,name='details'),
    path('details/payment/<int:evId>',views.payment,name='payment'),
    path('sendQuery',views.sendQuery,name="sendQuery"),
    path('details/requestCA/<int:evId>',views.requestCA,name='requestCA'),
    path('details/userList/<int:evId>',views.userList,name='userList'),
]


