from django.urls import path

from angajat import views

app_name = 'angajat'

urlpatterns = [
    path('', views.AngajatView.as_view(), name='lista_angajat'),
    path('adaugare/', views.CreateAngajatView.as_view(), name='adaugare'),
    path('<int:pk>/update/', views.UpdateAngajatView.as_view(), name='modificare'),
    path('<int:pk>/delete', views.delete_angajat, name='stergere'),
    path('<int:pk>/activate', views.activare_angajat, name='activare'),

]
