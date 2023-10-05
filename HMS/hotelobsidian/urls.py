from django.urls import path
from . import views
from . import loginfunctions
from . import signupfunction

urlpatterns = [
    path('', views.default, name='default'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('homepage/', loginfunctions.user_dashboard, name='homepage')
]

