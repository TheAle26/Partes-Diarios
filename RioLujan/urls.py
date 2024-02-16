from django.urls import path
from RioLujan import views
from django.contrib.auth.views import LogoutView

urlpatterns=[

    path('login/',views.login_request,name='iniciar_sesion'),
   
]