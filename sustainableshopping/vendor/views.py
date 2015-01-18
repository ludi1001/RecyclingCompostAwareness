from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from vendor.forms import *
from vendor.models import *
import json
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
@login_required
def home(request):
    vendor = Vendor.objects.get(user=request.user)
    return render(request, 'vendorhome.html', { 'vendor': vendor })
 
@login_required 
def update(request):
    try:
        obj = json.loads(request.body.decode('utf-8'))
        vendor = Vendor.objects.get(user=request.user)
        print(obj)
        vendor.name = obj['name']
        vendor.phone = obj['phone']
        vendor.address = obj['address']
        vendor.desc = obj['desc']
        vendor.lat = obj['lat']
        vendor.lng = obj['lng']
        
        for tag in obj['tags']:
            vendor.tag_set.add(Tag.objects.get(name=tag))
        vendor.save()
        return HttpResponse('{"error":"success"}',content_type='application/json')
    except KeyError:
        return HttpResonse('{"error":"Bad format"}',content_type='application/json')
    except ValueError:
        return HttpResponse('{"error":"Malformed JSON"}',content_type='application/json')
    
    
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