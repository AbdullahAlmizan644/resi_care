from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm
from django.contrib import messages
from .forms import RentForm,TeacherForm,TutionForm
from home.models import RentPurchaserDetails
from .models import RentPayment

# Create your views here.

def user_login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request, "Welcome to user dashboard")
            return redirect("/user_dashboard")
            
        else:
            messages.error(request, "wrong username or password")
            return redirect(request.path)
        
    return render(request, "user_auth/login.html")



def forget_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to success page
            messages.error(request, "Password reset successfully")
            return redirect(user_login)
    else:
        form = PasswordResetForm()
    return render(request, 'user_auth/forget_password.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect("/")



def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, "Account Created successfully now login")
            return redirect(user_login)
    else:
        form = UserCreationForm()
    return render(request, 'user_auth/register.html', {'form': form})



def user_dashboard(request):
    if request.user.is_authenticated:
        user=User.objects.get(username=request.user)
        print(request.user)
        return render(request, "user_auth/user_dashboard.html")

    else:
        return redirect("/user_login")



def house_rent_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = RentForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.creator = request.user
                instance.save()
                
                messages.success(request,"Post Added Successfully")
                return redirect(user_dashboard)
            else:
                form = RentForm()
             
            return render(request, 'user_auth/house_rent_post.html', {
                'form': form
            })
        
        return render(request, 'user_auth/house_rent_post.html',{
            "c_username":request.user
        })

 

    else:
        return redirect("/user_login")
     


def teacher_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TeacherForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.creator = request.user
                instance.save()
                
                messages.success(request,"Post Added Successfully")
                return redirect(user_dashboard)
            else:
                form = TeacherForm()
             
            return render(request, 'user_auth/teacher_post.html', {
                'form': form
            })
        
        return render(request, 'user_auth/teacher_post.html',{
            "c_username":request.user
        })


    else:
        return redirect("/user_login")
     



def tution_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TutionForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.creator = request.user
                instance.save()
                
                messages.success(request,"Post Added Successfully")
                return redirect(user_dashboard)
            else:
                form = TutionForm()
             
            return render(request, 'user_auth/tution_post.html', {
                'form': form
            })
        
        
        


    else:
        return redirect("/user_login")
     


def my_rent(request):
    rent_details=RentPurchaserDetails.objects.filter(buyer_name=request.user).all()
    return render(request, 'user_auth/my_rent.html',{
        "rent_details":rent_details,
    })


def bill(request,id):
    post=RentPurchaserDetails.objects.filter(id=id).first()

    if request.method=="POST":
        name=request.POST.get("name")
        country=request.POST.get("country")
        division=request.POST.get("division")
        district=request.POST.get("district")
        address=request.POST.get("address")
        zip_code=request.POST.get("zip_code")
        rent_price=request.POST.get("rent_price")
        payment=request.POST.get("payment")

        obj=RentPayment(name=name,country=country,division=division,
                        district=district,address=address,
                        zip_code=zip_code,rent_price=rent_price)
        
        obj.save()

        messages.success(request, "Your payment done!")
        return redirect("user_dashboard")

    return render(request,"user_auth/bill.html",{
        "post":post,
    })

