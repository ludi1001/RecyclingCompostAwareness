from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from vendor.forms import *
from vendor.models import *
from django.contrib.auth.models import User

# Create your views here.
@login_required
def home(request):
    return render(request, 'vendorhome.html')
    
def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['email'], form.cleaned_data['email'], form.cleaned_data['password'])
            user.save()
            
            vendor = Vendor(user=user)
            vendor.save()
            return redirect('/vendor')
        print("invalid form")
    return render(request, 'signup.html', {'form': form})