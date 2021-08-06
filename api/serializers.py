from rest_framework import serializers

from rodadas.models import Rodada


class RodadaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rodada
        fields = [
            "id", "title", "date", "description",
            "drive", "presentation", "recording"
        ]