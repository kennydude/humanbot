from rest_framework import serializers

from humanbot.core.models import Human


class HumanSerializer(serializers.ModelSerializer):
    picture = serializers.CharField(source='picture.url', read_only=True)

    class Meta:
        model = Human
        fields = ['id', 'name', 'picture']
