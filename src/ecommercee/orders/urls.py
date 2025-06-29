from django.urls import path
from django.conf.urls.static import static
from orders import views

urlpatterns = [
    path('cart',views.show_cart,name="cart")
]
