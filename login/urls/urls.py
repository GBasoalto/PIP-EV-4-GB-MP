from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from login.views import views


urlpatterns = [
    path('', LoginView.as_view(template_name='login/index.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', views.home, name='home'),
]
