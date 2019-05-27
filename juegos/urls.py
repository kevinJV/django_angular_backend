from django.urls import path
from .views import JuegosDetail
from .views import JuegosList


urlpatterns = [
    path('', JuegosList.as_view()),
    path('<int:pk>/', JuegosDetail.as_view()),
]