from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def home(request):
    # return HttpResponse("welcome")
     return render(request,"home.html")


def pramter1(request,name,id):

    print(name,id)
    # return HttpResponse("welcome")
    return render(request,"home.html")

def pramter2(request):
    # name=request.GET.get('name')#('<par name here>','<default value here>')
    # id=request.GET.get('id')
    # or
    name=request.GET['name']
    id=request.GET['id']
    print(name,id)
    return render(request,"home.html")

def pramter3(request):
    name=request.POST.get('name',"none")
    id=request.POST.get('id',"cccc") #('<par name here>','<default value here>')
    # or
    # name=request.GET['name']
    # id=request.GET['id']
    print(name,id)
    return render(request,"home.html")
# ==================================
# request.POST.get('<par name here>','<default value here>')
#  request.GET.get('<par name here>','<default value here>')
# ==================================
# {# "index.html" #}
# <form action="{% url 'my_app1:test' %}" method="post">
#   {% csrf_token %}
#   <input type="text" name="fruits" value="apple" /></br>
#   <input type="text" name="meat" value="beef" /></br>
#   <input type="submit" />
# </form>