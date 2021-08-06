from django.utils import timezone
from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from rodadas.models import Rodada
from .serializers import RodadaSerializer


class RodadasViewSet(viewsets.ModelViewSet):
    queryset = Rodada.objects.all().order_by("-date")
    serializer_class = RodadaSerializer
    permission_classes = [permissions.AllowAny]


class ProximaRodadaViewSet(viewsets.ModelViewSet):
    queryset = Rodada.objects.all()
    serializer_class = RodadaSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = Rodada.objects.filter(
            date__gte=timezone.datetime.now()
        ).order_by(
            "date"
        ).first()
        serializer = RodadaSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UltimasRodadasViewSet(viewsets.ModelViewSet):
    queryset = Rodada.objects.all()
    serializer_class = RodadaSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = Rodada.objects.filter(
            date__lt=timezone.datetime.now()
        ).filter(
            date__isnull=False
        ).order_by(
            "-date"
        )
        serializer = RodadaSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
