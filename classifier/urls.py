from django.urls import path
# from django.contrib.auth import views as auth_views
from . import views

app_name= "classifier"
urlpatterns = [
    
    path("scanner/", views.scanner, name = "scanner"),
    # path("prediction/", views.prediction, name = "prediction")
    

]