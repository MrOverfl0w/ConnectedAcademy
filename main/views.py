from django.shortcuts import render
from main import models
from django.shortcuts import redirect
from django.contrib.auth import get_user


# Create your views here.
def Main(request):
    return render(request, 'Main_Screen.html')

def SignUp(request):
    if get_user(request).is_anonymous():
        if request.method == 'POST':
            data = request.POST
            models.createUser(data)
            return redirect('LogIn')
        return render(request, 'SignUp.html')
    else:
        return redirect('check')

def LogIn(request):
    if get_user(request).is_anonymous():
        return redirect('AuthLogIn')
    else:
        return redirect('check')

    
def check(request):
    return render(request, 'check.html')