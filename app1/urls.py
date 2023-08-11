from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home_view, name='home'),
    path('textinput/', views.user_text, name='textinput'),
    path('processing/<str:username>/', views.form_data, name='processing'),
    path('fileinput/', views.upload_file, name='fileinput'),
    path('fileprocessing/<str:username>/', views.file_data, name='fileprocessing'),
]
