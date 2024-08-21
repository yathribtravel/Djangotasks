
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home ,name="home"),
    path('read_file/', views.read_file ,name="read_file"),
    path('pagination/', views.pagination ,name="pagination"),
]
