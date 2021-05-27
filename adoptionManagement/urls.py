from django.urls import path
# from django.contrib.auth import views as auth_views
from . import views

app_name= "adoptionManagement"
urlpatterns = [
    path("", views.displayDog, name="home"),
    path("upload/", views.uploadDog, name="uploadDog"),
    path("updateDog/<str:pk>/", views.updateDog, name="updateDog"),
    path("deleteDog/<str:pk>/", views.deleteDog, name="deleteDog"),
    path("queue/", views.registerDog, name="registerDog"),
    path("registrations/", views.displayRegistration, name="displayRegistration"),
    path("acceptRegistration/<str:pk>/", views.acceptRegistration, name="acceptRegistration"),
    path("requestDog/<str:pk>/", views.requestDog, name="requestDog"),
    path("cancelRequest/<str:pk>/", views.cancelRequest, name="cancelRequest"),
    path("displayRequest/", views.displayRequest, name="displayRequest"),
    path("clientRequest/", views.clientRequest, name="clientRequest"),
    path("acceptRequest/<str:pk>/", views.acceptRequest, name="acceptRequest"),
    path("declineRequest/<str:pk>/", views.declineRequest, name="declineRequest"),
    path("search/", views.searchResult, name = "searchResult"),
   
    

]