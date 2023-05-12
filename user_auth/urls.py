from django.urls import path
from .views import *

urlpatterns=[
    path("user_login",user_login,name="user_login"),
    path("forget_password",forget_password,name="forget_password"),
    path("user_signup",user_signup,name="user_signup"),
    path("user_dashboard",user_dashboard,name="user_dashboard"),
    path("user_logout",user_logout,name="user_logout"),
    path("house_rent_post",house_rent_post,name="house_rent_post"),
    path("teacher_post",teacher_post,name="teacher_post"),
    path("tution_post",tution_post,name="tution_post"),
    path("my_rent",my_rent,name="my_rent"),
    path("bill/<int:id>",bill,name="bill"),

]