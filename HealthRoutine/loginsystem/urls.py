from django.urls import path
from . import views

urlpatterns = [
    path('signIn/', views.signIn_view),
    path('signUp/',views.signUp_view),
    path('logout/',views.logout_view),
]