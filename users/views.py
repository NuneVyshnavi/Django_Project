from django.shortcuts import render, redirect

from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm
)

from django.contrib.auth import (
    login,
    logout
)


def register_view(request):

    form = UserCreationForm()

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('/')

    return render(request, 'register.html', {
        'form': form
    })


def login_view(request):

    form = AuthenticationForm()

    if request.method == 'POST':

        form = AuthenticationForm(
            data=request.POST
        )

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect('/')

    return render(request, 'login.html', {
        'form': form
    })


def logout_view(request):

    logout(request)

    return redirect('/login/')

# Create your views here.
