from django.shortcuts import render
from django.http import HttpResponse
from vendor.models import Vendor
import json
import math

# Create your views here.
def home(request):
    return render(request, 'index.html')
    
def search(request):
    return render(request, 'map.html')

def calculate_dist(loc1lat, loc1lng, loc2lat, loc2lng):
    print('asdf')
    R = 3959 #mi
    phi1 = loc1lat / 180 * math.pi
    phi2 = loc2lat / 180 * math.pi 
    dphi = (loc2lat - loc1lat) / 180 * math.pi
    dlambda = (loc2lng - loc1lng) / 180 * math.pi
    a = math.sin(dphi/2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda/2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c 
 
def find_vendors(request):
    try:
        obj = json.loads(request.body.decode('utf-8'))
        max_dist = float(obj['range'])
        

        vendor_results = Vendor.objects.all()
        for tag in obj['tags']:
            vendor_results = vendor_results.filter(tag__name=tag)
            
        vendors = []         
        for vendor in vendor_results:
            dist = calculate_dist(obj['lat'], obj['lng'], vendor.lat, vendor.lng)
            print(dist)
            if dist <= max_dist:
                vendors.append({
                    'name': vendor.name,
                    'address': vendor.address,
                    'phone': vendor.phone,
                    'desc': vendor.desc,
                    'lat': vendor.lat,
                    'lng': vendor.lng,
                    'dist': dist
                })
        
        vendors = sorted(vendors, key=lambda vendor: vendor['dist'])
        print(vendors)
        return HttpResponse(json.dumps(vendors),content_type='application/json')
    except KeyError:
        return HttpResonse('{"error":"Bad format"}',content_type='application/json')
    except ValueError:
        return HttpResponse('{"error":"Malformed JSON"}',content_type='application/json')
    