from django.urls import include
from django.urls import path
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r"rodadas", views.RodadasViewSet)
router.register(r"proxima", views.ProximaRodadaViewSet)
router.register(r"ultimas", views.UltimasRodadasViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
