from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.

# def current_user(request):
#     c_user=request.user
#     return c_user

class Poster(models.Model):
    poster_image_one=models.ImageField(upload_to="images/",verbose_name='poseter image one size-->width:1170 height:780')
    poster_image_two=models.ImageField(upload_to="images/")
    poster_image_three=models.ImageField(upload_to="images/")


class Rent(models.Model):
    title=models.CharField(max_length=1000)
    home_description=models.TextField()
    rent_price=models.IntegerField()
    total_square_feet=models.IntegerField()
    total_washroom=models.IntegerField()
    total_bed=models.IntegerField()
    phone_number=models.IntegerField()
    DHAKA = 'Dhaka'
    CHITTAGONG = 'Chittagong'
    DIVISION_CHOICES = (
        (DHAKA, 'Dhaka'),
        (CHITTAGONG, 'Chittagong')
    )

    division = models.CharField(choices=DIVISION_CHOICES, max_length=50)

    #Chittagong district
    GEC='Gec Moor'
    Chawkbazar='Chawkbazar'

    #Dhaka District
    Mirpur='mirpur'
    Gulshan='Gulshan'

    district_choices=(
        (GEC,'Gec Moor'),
        (Chawkbazar,'Chawkbazar'),
        (Mirpur,'Mirpur'),
        (Gulshan,'Gulshan'),
    )

    district=models.CharField(choices=district_choices,max_length=1000)

    home_image_one=models.ImageField(upload_to="images/")
    home_image_two=models.ImageField(upload_to="images/")
    home_image_three=models.ImageField(upload_to="images/")
    datetime=models.DateTimeField(default=now)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    flag=models.CharField(max_length=100,default="null")


    def __str__(self):
        return f"{self.id} {self.title}"
    


class Teacher(models.Model):
    teacher_name=models.CharField(max_length=1000)
    email=models.EmailField()
    phone_number=models.IntegerField()
    DHAKA = 'Dhaka'
    CHITTAGONG = 'Chittagong'
    DIVISION_CHOICES = (
        (DHAKA, 'Dhaka'),
        (CHITTAGONG, 'Chittagong')
    )

    division = models.CharField(choices=DIVISION_CHOICES, max_length=50)

    #Chittagong district
    GEC='Gec Moor'
    Chawkbazar='Chawkbazar'

    #Dhaka District
    Mirpur='mirpur'
    Gulshan='Gulshan'

    district_choices=(
        (GEC,'Gec Moor'),
        (Chawkbazar,'Chawkbazar'),
        (Mirpur,'Mirpur'),
        (Gulshan,'Gulshan'),
    )

    district=models.CharField(choices=district_choices,max_length=1000)
    details_address=models.TextField()
    educations_details=models.TextField()
    teacher_image=models.ImageField(upload_to="images/")
    datetime=models.DateTimeField(default=now)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rating=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id} {self.teacher_name}"



class Tution(models.Model):
    title=models.CharField(max_length=1000)
    email=models.EmailField()
    phone_number=models.IntegerField()
    DHAKA = 'Dhaka'
    CHITTAGONG = 'Chittagong'
    DIVISION_CHOICES = (
        (DHAKA, 'Dhaka'),
        (CHITTAGONG, 'Chittagong')
    )

    division = models.CharField(choices=DIVISION_CHOICES, max_length=50)

    #Chittagong district
    GEC='Gec Moor'
    Chawkbazar='Chawkbazar'

    #Dhaka District
    Mirpur='mirpur'
    Gulshan='Gulshan'

    district_choices=(
        (GEC,'Gec Moor'),
        (Chawkbazar,'Chawkbazar'),
        (Mirpur,'Mirpur'),
        (Gulshan,'Gulshan'),
    )

    district=models.CharField(choices=district_choices,max_length=1000)
    details_address=models.TextField()
    teacher_details=models.TextField()
    tution_image=models.ImageField(upload_to="images/")
    datetime=models.DateTimeField(default=now)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.id} {self.title}"



class Contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.IntegerField()
    message=models.TextField()


    def __str__(self):
        return f"id:{self.id} name:{self.name}"
    

class RentComment(models.Model):
    rent=models.ForeignKey(Rent, on_delete=models.CASCADE)
    comment=models.TextField()
    username=models.CharField(max_length=100)
    datetime=models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.username} {self.comment[0:20]}......"
    


class RentPayment(models.Model):
    name=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    division=models.CharField(max_length=200)
    district=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    zip_code=models.CharField(max_length=200)
    rent_price=models.CharField(max_length=200)
    payment=models.CharField(max_length=200,blank=True,default="Bikash")
    datetime=models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.name}"