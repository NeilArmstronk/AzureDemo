from django.urls import path
from.import views


app_name = 'dpvinculado'
urlpatterns= [
#URLS for myapp1 app
     path('index',views.MyIndexView.as_view(), name="my_index_view"),
     ]