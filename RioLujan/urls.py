from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView

urlpatterns = [
    path('login/',views.login_request,name='iniciar_sesion'),
    path('RioLujan/', views.seleccionar, name='seleccionar'),
    path('not-found/', TemplateView.as_view(template_name='404.html'), name='not_found'),
    path('logout/', LogoutView.as_view(template_name='registro/logout.html'), name='logout'),

    # estado de aprobación
    path('update_Estado_De_Aprobacion/<int:estado_id>/', views.update_Estado_De_Aprobacion, name='update_Estado_De_Aprobacion'),
    path('Estado_De_Aporobacion_otro/', views.Estado_De_Aporobacion_otro, name='Estado_De_Aporobacion_otro'),
    path('Estado_De_Aprobacion/', views.Estado_De_Aprobacion_all, name='Estado_De_Aprobacion'),
    path('carga_Estado_De_Aprobacion/', views.carga_Estado_De_Aprobacion, name='carga_Estado_De_Aprobacion'),
    path('delete_Estado_De_Aprobacion/<int:estado_id>/', views.delete_Estado_De_Aprobacion, name='delete_Estado_De_Aprobacion'),

    
]