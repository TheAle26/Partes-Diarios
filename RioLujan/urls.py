from django.urls import path
from RioLujan import views
from django.contrib.auth.views import LogoutView

urlpatterns=[

    #path('login/',views.login_request,name='iniciar_sesion'),
    path('RioLujan/',views.seleccionar,name='seleccionar'),

    #estado de aprobarciuon
    path('RioLujan/update_Estado_De_Aprobacion/<int:estado_id>/',views.update_Estado_De_Aprobacion,name='update_Estado_De_Aprobacion'),
    path('RioLujan/Estado_De_Aporobacion_otro/',views.seleccionar,name='Estado_De_Aporobacion_otro'),
    path('RioLujan/Estado_De_Aprobacion/',views.Estado_De_Aprobacion_all,name='Estado_De_Aprobacion'),
    path('RioLujan/carga_Estado_De_Aprobacion/',views.carga_Estado_De_Aprobacion,name='carga_Estado_De_Aprobacion'),

   
]