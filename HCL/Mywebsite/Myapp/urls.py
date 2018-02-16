from django.urls import path
from .import views


urlpatterns = [
    path('dashboard', views.dashboard, name='Dashboard'),
    path('registration', views.registration, name='registration'),
    path('login', views.my_view,name='login'),
    path('logout', views.custon_logout, name='logout'),
    path('index/', views.index, name='index'),

]
