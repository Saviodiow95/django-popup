from django.urls import path, include
from .views import *

urlpatterns = [

    path('book/create', BookCreate, name = "BookCreate"),
    path('author/create', AuthorCreatePopup, name = "AuthorCreate"),
    path('author/edit/<int:pk>', AuthorEditPopup, name = "AuthorEdit"),
    path('author/ajax/get_author_id', get_author_id, name = "get_author_id"),
   
]
