from django import forms
from .models import Rent,Teacher,Tution


class RentForm(forms.ModelForm):
    class Meta:
        model=Rent
        fields=('title','home_description','rent_price',
                'total_square_feet','total_washroom','total_bed','phone_number','division','district',
                'home_image_one','home_image_two', 'home_image_three','datetime','latitude','longitude')


class TeacherForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=('teacher_name','email','phone_number','division','district',
                'details_address','educations_details','teacher_image','datetime')




class TutionForm(forms.ModelForm):
    class Meta:
        model=Tution
        fields=('title','email','phone_number','division','district',
                'details_address','teacher_details','datetime')
