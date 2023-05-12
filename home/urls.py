from django.urls import path
from .views import index,about,contact,teacher,tution,rent,rent_details,teacher_details,tution_details,take_rent


urlpatterns=[
    path("",index,name="index"),
    path("about",about,name="about"),
    path("contact",contact,name="contact"),
    path("teacher",teacher,name="teacher"),
    path("teacher_details/<int:id>",teacher_details,name="teacher_details"),
    path("tution",tution,name="tution"),
    path("tution_details/<int:id>",tution_details,name="tution_details"),
    path("rent",rent,name="rent"),
    path("rent_details/<int:id>",rent_details,name="rent_details"),
    path("take_rent/<int:owner_id>",take_rent,name="take_rent")
]