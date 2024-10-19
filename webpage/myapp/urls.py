from django.urls import path
from .views import AboutPage, ContactPage, RegisterPage, LoginPage, HomePage, LogoutPage, headerPage, basePage

urlpatterns = [
     
    path('', basePage, name='base'),
    path('about/', AboutPage, name='about'),
    path('contact/', ContactPage, name='contact'),
    path('login/', LoginPage, name='login'),
    path('register', RegisterPage, name='register'),
    path('home/', HomePage, name='home'),
    path('logout/', LogoutPage, name='logout'),
    
    
]
