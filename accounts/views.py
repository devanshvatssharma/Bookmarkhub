from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView
from django.http import HttpResponse,HttpResponseRedirect
from .forms import UserRegistrationForm
from django.urls import reverse,reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm

class LoginUserView(LoginView):
    template_name="accounts/login.html"
    redirect_authenticated_user=True
    def get_success_url(self):
        return reverse_lazy("dashboard")
    def form_valid(self, form):
        messages.success(self.request,"Logged in successfully!")
        return super().form_valid(form)
    

def register_view(request):
    if request.method=="GET":
        if request.user.is_authenticated:
            return redirect("dashboard")
        form=UserRegistrationForm()
        return render(request,"accounts/register.html",{
            "form":form,
        })
    elif request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if(form.is_valid()):
            messages.success(request,"Successfully Registered")
            form.save()
            return redirect("login_page")
        return render(request,"accounts/register.html",{
            "form":form
        })
class LogoutUserView(LogoutView):
    next_page=reverse_lazy("login_page")

class ChangePasswordView(PasswordChangeView):
    form_class=PasswordChangeForm
    success_url=reverse_lazy("profile")
    template_name="bookmarks/passwordchange.html"
    def form_valid(self, form):
        messages.success(self.request,"Password change successfully!!")
        return super().form_valid(form)
    
def home(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return redirect("login_page")