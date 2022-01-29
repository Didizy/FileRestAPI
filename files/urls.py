from django.contrib import admin
from django.urls import path, include
from files import views

urlpatterns = [
    path('upload/', views.file_upload, name='upload'),
    path('list/', views.file_list, name='list'),
    path('delete/<int:pk>/', views.file_delete, name='delete'),
    path('download/<str:name>', views.file_download, name='download'),
    path('js_list/', views.file_js, name="js")
]
