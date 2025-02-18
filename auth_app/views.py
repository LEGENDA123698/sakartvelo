from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import *
from django.contrib import messages
from django.views.generic import *
from django.urls import reverse_lazy

def logout_view(request):
    logout(request)
    return redirect('main-page')

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main-page')
        else:
            print("FormNotValid")
    else:
        form = UserCreateForm()

    return render(request, 'auth_html/register.html', context = {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = UserAuthForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("login")
                return redirect('main-page')
            else:
                messages.error(request, 'invalid login or password')
    else:
        form = UserAuthForm()

    return render(request, 'auth_html/login.html', context = {'form': form})

class ProfileInfoView(TemplateView):
    template_name = 'auth_html/profile_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context



def profile_menu(request):
    return render(request, 'auth_html/profile_menu.html')


    
    
class UserProfileUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'auth_html/edit_profile_info.html'
    success_url = reverse_lazy('profile-info')

    def get_object(self):
        return self.request.user 

