from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view),
    path('profile/update/', views.profile_update),
    path('profile/delete/', views.profile_delete),
]