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

def full_stringer_list(request):
    stringers = stringers.objects.all().order_by('sport')
    return render(request, 'full_string_list.html', { 'stringers':stringers})

def main (request):
    return render(request, 'index.html')

def badminton (request):
    return render(request, 'badminton.html')

def squash(request):
    return render(request, 'squash.html')

def tennis(request):
    return render(request, 'tennis.html')



#note: this is where we want to pull data from db
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)