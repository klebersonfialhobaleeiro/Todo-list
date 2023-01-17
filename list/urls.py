from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'), #pagina principal

    #login e outros 
    path('login_and_singup/', views.login, name='login'),
    path('register/', views.register, name='register'), 
    path('logout/', views.logout, name="logout"),
    path('dashboard/', views.dashboard, name='dashboard'), 

    # as Notas criar_item
    path('criar_item', views.criar_item, name='criar_item'), 
    path('minhas_notas', views.list, name='list'), 
    path('delete', views.delete_item, name="delete_item"),
    path('update-item', views.update_item, name="update-item"),
    path('update-status', views.update_status, name="update-status"),

    # a dashboard 
    path('total-sum', views.total_sum, name='total-sum'),
    path('relatorio', views.relatorio, name='relatorio'),
    path('status', views.status, name='status'),
]