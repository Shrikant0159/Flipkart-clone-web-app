from django.urls import path
from . import views
urlpatterns = [
    path('', views.ProductView.as_view(),name='home'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/', views.cart_to, name='cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('checkout/', views.checkout, name='checkout'),
    path('customerregistration/', views.customer_registration, name='customerregistration'),
    path('log_in/', views.log_in, name='log_in'),
    path('log_out/', views.log_out, name='log_out'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('profile/', views.profile, name='profile'),

    path('fashion/', views.fashion, name='fashion'),
    path('beauty/', views.beauty, name='beauty'),
    path('applinces/', views.tv_applinces, name='applinces'),
    path('elctronics/', views.electronics, name='elctronics'),
    path('best_deal/', views.best_deal, name='best_deal'),
    path('home_decorator/', views.home_decorator, name='home_decorator'),
    path('furniture/', views.furniture, name='furniture'),
    path('grocery/', views.grocery, name='grocery'),
    path('mobile/', views.mobile, name='mobile'),


    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
]
