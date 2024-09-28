from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login as login_auth
# Create your views here.

def signup(request):
    if request.method == 'POST':
        print('post')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password_confirm = request.POST.get('password_confirm', '')

        if all([name, email, password, password_confirm]):
            new_user = User.objects.create_user(name, email, password)
            return redirect('/login/')
        else:
            print("Field missing")
        print(request.POST)
    else:
        print('just show form')
    return render(request, 'account/signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        print("Email: {}, Password: {}".format(email, password))
        if all([email and password]):
            user = authenticate(request, email=email, password=password, backend='account.User')
            
            if user is not None:
                login_auth(request, user)
                #print('User:', user)
                #print(request.user)
                #print(request.user.is_authenticated)
                return redirect('/')

        else:
                print('Invalid email or password')
                return render(request, 'account/login.html', {'error': 'Invalid email or password'})
    return render(request, 'account/login.html')

