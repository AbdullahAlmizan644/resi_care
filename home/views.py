from django.shortcuts import render,HttpResponse,redirect
from user_auth.models import Rent,Teacher,Tution,Poster,RentComment
from user_auth.models import Contact
from .models import RentPurchaserDetails
from django.contrib import messages

# Create your views here.
def index(request):
    all_rent_post=Rent.objects.all()[0:7]
    all_teacher_post=Teacher.objects.all()[0:7]
    all_poster=Poster.objects.last()

    if request.method=="POST":
        city=request.POST['city']
        location=request.POST['location']
        pType=request.POST['pType']
        pStatus=request.POST['pStatus']
        bedrooms=request.POST['bedrooms']
        bathrooms=request.POST['bathrooms']
        roomSize=request.POST['roomSize']
        priceRange=request.POST['priceRange']

        searchResult=Rent.objects.filter(division=city,district=location,total_bed=bedrooms,
                                         total_washroom=bathrooms,rent_price=priceRange,total_square_feet=roomSize).all()
        
        print(searchResult)

        print(city,location,pType,pStatus,bedrooms,bathrooms,roomSize,priceRange)
        number_of_result=len(searchResult)
        print(all_poster)


        return render(request,"main/rentSearch.html",{
            "search_rent_post":searchResult,
            "number_of_result":number_of_result
        })


    return render(request, "main/index.html",{
        "all_rent_post":all_rent_post,
        "all_teacher_post":all_teacher_post,
        "all_poster":all_poster,
        }
    )


def rent(request):
    all_rent_post=Rent.objects.all()
    return render(request, "main/rent.html",{
        "all_rent_post":all_rent_post,
    })


def rent_details(request,id):
    post=Rent.objects.filter(id=id).first()
    all_comments=RentComment.objects.filter(rent=id).all()
    total_comments=len(all_comments)

    if request.method=="POST":
        comment=request.POST["comment"]

        obj=RentComment(rent=post,comment=comment,username=request.user)
        obj.save()
        return redirect(request.path)

    print(all_comments)

    return render(request, "main/rent_details.html",{
        "post":post,
        "all_comments":all_comments,
        "total_comments":total_comments
    })


def about(request):
    return render(request, "main/about.html")


def contact(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        message=request.POST["message"]
        obj=Contact(name=name,email=email,phone=phone,message=message)
        obj.save()
        messages.success(request, "Sent message successfully!")
        return redirect(request.path)
    return render(request, "main/contact.html")


def teacher(request):
    all_teacher_post=Teacher.objects.all()
    print(all_teacher_post)
    return render(request, "main/teacher.html",{
        "all_teacher_post":all_teacher_post,
    })


def teacher_details(request,id):
    post=Teacher.objects.filter(id=id).first()

    if request.method=="POST":
        rating=request.POST.get("rating")
        teacher = Teacher.objects.get(id=id)
        teacher.rating=float(rating)
        teacher.save()
        print(teacher.rating)
        messages.success(request, "rating add successfully!")
        return redirect(request.path)
    
    return render(request, "main/teacher_details.html",{
        "post":post,
    })


def tution(request):
    all_tution_post=Tution.objects.all()
    return render(request, "main/tution.html",{
        "all_tution_post":all_tution_post,
    })


def tution_details(request,id):
    post=Tution.objects.filter(id=id).first()
    return render(request, "main/tution_details.html",{
        "post":post,
    })


def take_rent(request,owner_id):
    if request.user.is_authenticated:
        owner=Rent.objects.filter(id=owner_id).first()
        print(owner.creator)

        obj=RentPurchaserDetails(owner_name=owner.creator,buyer_name=request.user,
                                district=owner.district,division=owner.division,
                                rent_price=owner.rent_price,square_foot=owner.total_square_feet,washroom=owner.total_washroom,
                                bedroom=owner.total_bed)
        obj.save()

        ren_obj=Rent.objects.get(id=owner_id)
        ren_obj.flag="y"
        ren_obj.save()
        messages.success(request, "Thanks You take rent service go to dahboard my rent for details")
        return redirect("/") 
    
    else:
        return redirect("user_login")



