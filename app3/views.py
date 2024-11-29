from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view5(request):
    return HttpResponse('<h1>view5 is executing</h1>')

def view6(request):
    return HttpResponse('<h1>view6 is executing</h1>')