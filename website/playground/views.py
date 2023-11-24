from django.shortcuts import render
from django.http import HttpResponse
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



#note: this is where we want to pull data from db
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)