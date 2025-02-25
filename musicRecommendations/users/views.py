from django.db.models import F
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.views.generic import DetailView
from django.utils import timezone
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import SignUpForm

from .models import User

# Create your views here.
class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "users/profile.html"
    context_object_name = 'user'
    login_url = '/users/login/'

class SignUpView(View):

    def get(self, request):
        form = SignUpForm()
        return render(request, "users/signup.html", {'form': form})
    
    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('songs:index')
        return render(request, "users/signup.html", {'form': form})

class LoginView(View):
    
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "users/login.html", {'form': form})
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('songs:index'))
        return render(request, "users/login.html", {'form': form})

class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('songs:index')
    
class DeleteAccountView(LoginRequiredMixin, View):
    login_url = '/users/login/'

    def post(self, request, *args, **kwargs):
        user = request.user
        logout(request)
        user.delete()
        return redirect('songs:index')