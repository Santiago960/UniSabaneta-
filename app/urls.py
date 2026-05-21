from django.urls import path

from . import views

urlpatterns = [

    path('', views.inicio, name='inicio'),

    path('materias/', views.materias, name='materias'),

    path('ingles/', views.ingles, name='ingles'),

    path('recomendacion/', views.recomendacion, name='recomendacion'),

    path('horarios/', views.horarios, name='horarios'),

    path('perfil/', views.perfil, name='perfil'),

        path(
    'reporte-materias/',
    views.reporte_materias,
    name='reporte_materias'
),

path(
    'reporte-horarios/',
    views.reporte_horarios,
    name='reporte_horarios'
),

    path('login/', views.login_view, name='login'),

    path('registro/', views.registro, name='registro'),

    path('logout/', views.logout_view, name='logout'),

]