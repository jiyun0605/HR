from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/profile/', views.profile_view),
    path('<int:user_id>/profile/update/', views.profile_update),
]