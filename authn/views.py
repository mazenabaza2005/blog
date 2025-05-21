from pyexpat.errors import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse

from authn.forms import LoginForm, ContactForm, RegisterForm
from django.contrib import messages


def login_view(request):
    next_url = request.GET.get('next', reverse('site:posts:list'))
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(next_url)
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'next_url': next_url})


def logout_view(request):
    logout(request)
    return redirect('site:authn:login')


from django.contrib import messages
from django.contrib.auth import login

def register_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)  
            messages.success(request, "Registration complete!")
            return redirect('site:posts:list')
    return render(request, 'register.html', {'form': form})

    


# def contact_view(request):
#     form = ContactForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             # Process the form data (e.g., send an email)
#             return redirect('posts:list')
#     return render(request, 'contact.html', {'form': form})