from django.contrib import messages
from django.contrib.auth import logout, login as make_login
from django.shortcuts import render, redirect, reverse
from .forms import CustomUserCreationForm

# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('core:index')

def UserRegister(request):
    userRegisterForm = CustomUserCreationForm()
    if request.method == 'POST':
        userRegisterForm = CustomUserCreationForm(request.POST)
        if userRegisterForm.is_valid():
            user = userRegisterForm.save()
            if user is not None:
                make_login(request, user)
                messages.success(request, 'Datos del cliente almacenados.')
                return redirect(reverse('core:index'))
    else:
        userRegisterForm = CustomUserCreationForm()
    return render(request, 'registration/user_register.html', {'userRegisterForm':userRegisterForm})