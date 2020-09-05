from django.urls import path
from .views import *

urlpatterns = [
    path('', newsfeed, name="newsfeed"),
    path('post/update/<int:id>', updatepost, name="update-post"),
    path('post/delete/<int:id>', deletepost, name="delete-post"),
    path('comment/update/<int:id>', updatecomment, name="update-comment"),
    path('comment/delete/<int:id>', deletecomment, name="delete-comment"),
]

