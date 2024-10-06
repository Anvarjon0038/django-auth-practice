from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, ProfileImageForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required



def register(request):
    try:
        if request.method == "POST":
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Пользаватель {username} был успешно создан!')
                return redirect('home')
        else:
            form = UserRegisterForm()
        return render(request,
                      'users/registration.html',
                      {
                          'title': 'Страница регистрации',
                          'form': form,
                      }

                      )
    except Exception:
        print("Eror")

@login_required
def profile(request):
    profileForm = ProfileImageForm()
    updateUserForm = UserUpdateForm()

    data = {
        'profileForm': profileForm,
        'updateUserForm': updateUserForm
    }

    return render(request, 'users/profile.html', data)


