from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
  path('',views.index,name="index"),
  path('developer',views.devloper,name='devloper')
]
