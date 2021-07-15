from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import CustomUser
from .forms import SignUpForm,EditUserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup(request):
    if request.method == "POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,"Account Created Successfully !! ")
            fm.save()
    else:
        fm=SignUpForm()
    return render(request,'accounts/signup.html',{'form':fm})

def signin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                email=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=email,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Successfully!!')
                    return HttpResponseRedirect("/profile/")
        else:
            fm = AuthenticationForm()
        return render(request,'accounts/signin.html',{'form':fm})
    else:
        return redirect('/profile/')

@login_required
def profile(request):
    stu = CustomUser.objects.all()
    nm=request.user.email
    # print(nm)
    return render(request,'accounts/profile.html',{'stu':stu,'usr':nm})
@login_required
def edit_user_details(request,pk):
    Euser = CustomUser.objects.get(pk=pk)
    if request.method == "POST":
        fm=EditUserProfileForm(request.POST,instance=Euser)
        if fm.is_valid():
            messages.success(request,"Details Updated")
            fm.save()
            return redirect('/profile/')
    else:
        fm=EditUserProfileForm(instance=Euser)
    return render(request,'accounts/updateprofile.html',{'form':fm})

@login_required
def deleteuserdetails(request,pk):
    Euser=CustomUser.objects.get(pk=pk)
    nm=Euser.name
    if Euser.is_superuser:
        messages.info(request,f"{nm} user can not delete because superuser")
        return redirect('/profile')
    else:
        Euser.delete()
        messages.success(request,"User Deleted SuccessFully!!")
    return redirect('/profile/')


@login_required
def user_logout(request):
    logout(request)
    return redirect('signin')
@login_required
def change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = SetPasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Password Changed Successfully!!')
                return HttpResponseRedirect('/profile')
        else:
            fm=SetPasswordForm(request.user)
        return render(request,'accounts/passwordchange.html',{'form':fm})
    else:
        return redirect('/signin/')