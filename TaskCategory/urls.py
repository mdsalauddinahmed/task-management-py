from django.urls import path 
from .import views

urlpatterns = [
    path('',views.add_Category,name='add_category'),
    path('edit_category/<int:id>',views.edit_Category,name='edit_category'),
     
]
