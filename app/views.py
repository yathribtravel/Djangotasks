from django.shortcuts import render,HttpResponse

# Create your views here.

from . models import test


def home(request):
    data=test.objects.all()
    # print(data["name"])
    return HttpResponse(list(data.values("name","age")))
    # return render (request,context={"data":data})