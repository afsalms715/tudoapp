from django.urls import path
from . import views
urlpatterns = [
    path('',views.fun,name='fun'),
    path('update/',views.update,name='update')
]