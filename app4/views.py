from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view7(request):
    return HttpResponse('<i>view7 is executing</i>')

def view8(request):
    return HttpResponse('<i>view8 is executing</i>')