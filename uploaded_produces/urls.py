from django.urls import path
from . import views

urlpatterns = [
    path('', views.abstract_view, name="abstract_view"),
    path("<int:pk>/", views.detail_view, name="detail_view"),
]
