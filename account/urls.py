from django.urls import path
from account.views import register, login_view, logout_view, home_view

urlpatterns=[
    path('',home_view,name="dashboard"),
    path('register/',register,name="register"),
    path('login/',login_view, name = "login"),
    path('logout/', logout_view, name = "logout"),
]