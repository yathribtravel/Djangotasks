from django.shortcuts import render ,redirect, HttpResponseRedirect
from .form import stydent_forms
from django.contrib import messages
# Create your views here.



def home(request):
  

    if request.method=="POST":
        form =stydent_forms(request.POST)
        if form.is_valid():
           try:
             form.save()
             print("save",request.path)
             return redirect(request.path)
           except:
              form.add_error("name", "error message1")
              form.add_error("name", "error message2")
              print("eeee")
            #   messages.error(request,"errro")
             
            
            
            
            # return HttpResponseRedirect("/")
    else:
        form =stydent_forms()
        # print("not save")


    return render(request,"index.html",{"form":form})



def home1(request):
  

    if request.method=="POST":
        form =stydent_forms(request.POST)
        if form.is_valid():
           try:
             form.save()
             print("save",request.path)
             return redirect(request.path)
           except:
              form.add_error("name", "error message1")
              form.add_error("name", "error message2")
              print("eeee")
            #   messages.error(request,"errro")
             
            
            
            
            # return HttpResponseRedirect("/")
    else:
        form =stydent_forms()
        # print("not save")


    return render(request,"index1.html",{"form":form})

# 
"""
https://stackoverflow.com/questions/67508409/how-to-fill-in-a-modelform-within-django-view
https://docs.djangoproject.com/en/5.2/topics/forms/
"""