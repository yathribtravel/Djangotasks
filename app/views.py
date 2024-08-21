from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    if request.method=="POST":
            for i in range(1,2+1):
                  print(request.POST["x1"+str(i)],request.POST["x2"+str(i)],request.POST["x3"+str(i)])
        
    return render(request,"index.html")