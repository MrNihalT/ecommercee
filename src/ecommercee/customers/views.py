from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from customers.models import Customer


def show_account(request):
    context = {}
    if request.POST and 'register' in request.POST:
        context['register'] = True
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')

            user = User.objects.create_user(
                username = username,
                password = password,
                email = email
            )
            customer = Customer.objects.create(
                name=username,
                user = user,
                phone = phone,
                address = address
            )
            return redirect('home')
        except Exception as e:
            error_message = "user name alerdy defined or invalid credintials "
            messages.error(request,error_message)
    if request.POST and 'login' in request.POST:
        context['register'] = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'invalid username or password')
            
    return render(request,'account.html',context)

def signout(request):
    logout(request)
    return redirect('home')