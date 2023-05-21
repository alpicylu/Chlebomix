from django.urls import path
from . import views

urlpatterns = [
    path('zaloguj/', views.login_user, name='login')
]

