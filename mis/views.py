from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from loans.models import Loan
from accounts.models import userProfile

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
           auth.login(request, user)
           return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:    
        return render(request, 'mis/login.html')

def home(request):

    return render(request, 'mis/home.html')

def logout(request):
    return redirect('login')

def loans(request):
    loans = Loan.objects.all()
    context = {
            'loans' :loans
        }
    
    return render(request, 'mis/loans.html',context)

def borrowers(request):
    borrowers = userProfile.objects.all()
    context = {
        'borrowers': borrowers
    }
    
    return render(request, 'mis/borrowers.html', context)


