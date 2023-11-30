from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views.generic import View
from .models import stringers
# more like request handler

# request -> response
#aka action

# Create your views here.

def say_hello(request):
    #pull data from db
    #transform 
    #send data
    #return HttpResponse('Hello World')
    return render(request, 'hello.html', {'name': 'Mosh'})

def main (request):
    return render(request, 'index.html')

def badminton (request):
    stringerdata = stringers.objects.all().order_by('fullName')
    return render(request, 'badminton.html', { 'stringers': stringerdata})
    return render(request, 'badminton.html')

def stringer_badminton_cust(request):
    stringerdata = stringers.objects.all().order_by('numberOfLifeTimeCustomers')
    return render(request, 'badminton.html', { 'stringers': stringerdata})

def stringer_badminton_cost(request):
    stringerdata = stringers.objects.all().order_by('cost')
    return render(request, 'badminton.html', { 'stringers': stringerdata})

def stringer_badminton_rating(request):
    stringerdata = stringers.objects.all().order_by('rating')
    return render(request, 'badminton.html', { 'stringers': stringerdata})

def squash(request):
    return render(request, 'squash.html')

def stringer_tennis_cust(request):
    stringerdata = stringers.objects.all().order_by('numberOfLifeTimeCustomers')
    return render(request, 'tennis.html', { 'stringers': stringerdata})

def stringer_tennis_cost(request):
    stringerdata = stringers.objects.all().order_by('cost')
    return render(request, 'tennis.html', { 'stringers': stringerdata})

def stringer_tennis_rating(request):
    stringerdata = stringers.objects.all().order_by('rating')
    return render(request, 'tennis.html', { 'stringers': stringerdata})

#note: this is where we want to pull data from db
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)