from django.urls import path
from . import views

urlpatterns = [
    path("", views.produce_index, name="produce_index"),
    path("<int:pk>/", views.produce_detail, name="produce_detail"),
    path("<category>/", views.produce_category, name="produce_category"),
]
