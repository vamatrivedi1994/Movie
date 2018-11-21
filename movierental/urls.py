from django.urls import path

from . import views

urlpatterns = [
    path('available/', views.available,name='available'),
    path('rented/', views.rented,name='rented'),
    path('movies/', views.movies,name='movies'),
    path('customer/', views.customer,name='customer'),
    path('addmovie/', views.addmovie,name='addmovie'),
    path('addcustomer/', views.addcustomer,name='addcustomer'),
    path('removemovie/<int:num>', views.removemovie,name='removemovie'),
    path('removecustomer/<int:num>',views.removecustomer,name='removecustomer'),
]
