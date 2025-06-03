from django.shortcuts import render ,HttpResponse ,redirect
from django.core.mail import send_mail
# Create your views here.

def home(request):
 
    return render(request,"index.html")


def send_email(request):
    send_mail("Subject_here","Here is the message.","yathribtravelsystem@gmail.com",["dd8429920@gmail.com",],fail_silently=False,)
    return redirect("/")


