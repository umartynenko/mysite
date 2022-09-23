from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)

# Подключаем наш API, используя автоматичепскую маршрутизацию URL.
#  Включаем  URL-адреса входа для доступного просмотра API.
urlpatterns = [
    path('', include(router.urls)),
    path('api_auth/',
         include('rest_framework.urls', namespace='rest_framework'))
]
