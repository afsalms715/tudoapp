from django.urls import path
from . import views
urlpatterns = [
    path('',views.fun,name='home'),
    path('update/<int:todu_id>/',views.update,name='update'),
    path('delete/<int:todu_id>/',views.delete,name='delete')
]