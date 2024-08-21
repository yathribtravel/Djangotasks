from django.shortcuts import render
from django.http import HttpResponse
import pandas
# Create your views here.
def home(request):
    return render(request,"home.html")


data=""
temp=""
def read_file(request):
    global data
    global temp
    if request.method=="POST":

        # file=request.POST["file"];
        my_uploaded_file = request.FILES['file']
        if  "csv"  in my_uploaded_file.name   :
             data= pandas.read_csv(my_uploaded_file)
        elif  "xlsx" in my_uploaded_file.name :    
            data= pandas.read_excel(my_uploaded_file)

        temp=data.head(10)     
            
       

    if request.method=="GET":

        
        l= request.GET.getlist('columns')
        # print(l)
    
        temp=data[l].head(10)
     


    return render(request,"table.html",{"data":temp,"columns":data.columns})#.to_html()



    # forloop.counter
    # forloop.counter0
    # forloop.first
    # forloop.last
    # forloop.parentloop
    # forloop.revcounter
    # forloop.revcounter0

def pagination(request):
    global data
    global temp
    page=int(request.GET.get("page"))
    limit=int(request.GET.get("limit"))

    a=(page-1)*limit
    b=a+(limit-1)
    data2=data.copy()
    temp=data2.loc[a:b,temp.columns]
    print(str(page),str(limit),str(a),str(b))
    # print(temp)
    # print(data2)
    return render(request,"table.html",{"data":temp,"columns":data.columns})#.to_html()

# def read_file_by_columns (request):
#        if request.method=="POST":
#         # file=request.POST["file"];
#         my_uploaded_file = request.FILES['file']
#         if  "csv"  in my_uploaded_file.name   :
#             data= pandas.read_csv(my_uploaded_file).head(10) 
#         elif  "xlsx" in my_uploaded_file.name :    
#             data= pandas.read_excel(my_uploaded_file).head(10) 
            
#         # print(my_uploaded_file.name)




#     return render(request,"table.html",{"data":data})#.to_html()


# file = request.FILES['filename']
# file.name           # Gives name
# file.content_type   # Gives Content type text/html etc
# file.size           # Gives file's size in byte
# file.read()         # Reads file

# print(request.FILES.items())
# for filename, file in request.FILES.items():
#     print(filename, file)

# for filename, file in request.FILES.iteritems():
#     name = request.FILES[filename].name
