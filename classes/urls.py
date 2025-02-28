from django.urls import path
from .views import home, greet,retrive_classroom,calculate_area

urlpatterns=[
    path("",home,name="home"),
    path("greet/<str:name>/", greet, name="greet"),
    path("classroom/<str:class_name>/",retrive_classroom,name="retrive_classroom"),
    path("calculate_area/", calculate_area, name="calculate_area"),
]