from django.urls import path , include
from . import views

urlpatterns = [
    path("",views.homePageView.as_view(),name = "home"),
    path('about/',views.AboutPageView.as_view(),name='about'),

]