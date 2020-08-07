from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_view),
    path('list/', views.list_view),
    path('<int:post_id>/delete/', views.delete_view),
    path('<int:post_id>/update/', views.update_view),
]