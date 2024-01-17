from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
from .views import user_logout, order_product

urlpatterns = [
    path("", views.index, name="index"),
    path("item/<str:id>", views.item, name="item"),
    path("shop", views.shop, name="shop"),
    path('blog', views.blog, name='blog'),
    path('category/<str:name>', views.category, name='category'),
    path('logout/', user_logout, name='shop_logout'),
    path('login/', LoginView.as_view(next_page='index'), name="shop_login"),
    path('signup', views.signup, name='signup'),
    path('profile', views.profile, name='profile'),
    path('search', views.search, name='search'),
    path('order_product/<int:id>/', order_product, name='order_product'),
]
