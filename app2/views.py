from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view3(request):
    return HttpResponse('<b>view3 is executing</b>')

def view4(request):
    return HttpResponse('<b>view4 is executing</b>')