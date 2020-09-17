from django.urls import path
from . import views

urlpatterns = [
    path('signUp/', views.sign_up),
    path('signIn/', views.sign_in),
    path('user/<pk>/verify/<token>/', views.verify, name='verify'),
    path('signOut/',views.sign_out)
]