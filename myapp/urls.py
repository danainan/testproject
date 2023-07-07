from django.urls import path
from myapp import views

urlpatterns = [
        path('', views.index, name='index'),
        path('livefe', views.livefe, name='livefe'),
        path('reset_camera', views.reset_camera, name='reset_camera'),
        path('initialize_camera', views.initialize_camera, name='initialize_camera'),
        path('display_file_capture', views.display_file_capture, name='display_file_capture'),
        path('ocr/', views.ocr, name='ocr'),


        


    ]