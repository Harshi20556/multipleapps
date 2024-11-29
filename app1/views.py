from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view1(request):
    return HttpResponse('<h1>view1 is executing</h1>')

def view2(request):
    return HttpResponse('<h1>view2 is executing</h1>')