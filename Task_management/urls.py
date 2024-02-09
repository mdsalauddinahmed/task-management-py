from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('show_task/', views.show,name='show'),
    path('add_task/',include('TaskModel.urls')),
    path('add_category/', include('TaskCategory.urls')),
]
