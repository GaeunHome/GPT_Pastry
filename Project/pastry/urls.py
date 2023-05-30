from django.urls import path 
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns = [ 
    path('', views.index, name='index'), 
    path('menu/', views.menu, name='menu'), 
    path('cart/', views.cart, name='cart'), 
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'), 
    path('remove_from_cart/<int:order_item_id>/', views.remove_from_cart, name='remove_from_cart'), 
    path('checkout/', views.checkout, name='checkout'), 
    path('login/', views.login_view, name='login'), 
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'), 
    path('register/', views.register, name='register'), 
    path('edit_profile/', views.edit_profile, name='edit_profile'), 
    path('view_order/<int:order_id>/', views.view_order, name='view_order'), 
]