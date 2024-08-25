
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="name"),
    # 127.0.0.1:8000/t1/mego/2
    path('t1/<str:name>/<int:id>', views.pramter1,name="pramter1"),#
    # http://127.0.0.1:8000/t2/?name=youssef&id=10
    path('t2/', views.pramter2,name="pramter2"),
    # 
    path('t3/', views.pramter3,name="pramter3"),

]
