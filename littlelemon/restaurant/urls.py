from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.MenuView.as_view()),
    path('items/<int:pk>', views.SingleMenuView.as_view()),
]
