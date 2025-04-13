from django.http import HttpResponse 
from django.shortcuts import render 
def home(request):
    # process 1 
    # process 2 
    # process 3
    return HttpResponse("Hello Django!")

def profile(request):
    # process 1 
    # process 2
    # process 3
    return HttpResponse("Hello Profile !") 


def dashborad(request):
    # process 1 
    # process 2 
    # process 3
    return HttpResponse("Hello Dashboard!")

def about(request):
    return render (request, template_name="about.html")