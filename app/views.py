from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    # return HttpResponse("welcome")
    context = {"message": "Hello from Django!"}
    return render(request, "home.html", context)



def about(request):
        return render(request, "about.html")
def contact_as(request):
        return render(request, "contact_as.html")