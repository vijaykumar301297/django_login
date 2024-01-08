from django.urls import path
from signin import views

urlpatterns = [
    path('home/', views.home, name ='home'),
    path('', views.signin, name ='login'),
    path('signup/', views.signup, name ='signup'),
    path('logout/', views.logout_user, name='logout'),
]

