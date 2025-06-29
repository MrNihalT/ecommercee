from django.urls import path
from django.conf.urls.static import static
from customers import views

urlpatterns = [
    path('account',views.show_account,name="account"),
    path('logout',views.signout,name="logout")
]
