

from django.contrib import admin
from django.urls import path,include
from Documents.views import upload_documents,clear_documents,search_documents

urlpatterns = [
    path('upload',upload_documents),
    path('clear',clear_documents),
    path('search',search_documents)
]