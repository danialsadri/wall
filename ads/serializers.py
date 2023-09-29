from .models import Ad
from rest_framework import serializers


class AdSerializer(serializers.ModelSerializer):
    publisher = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Ad
        fields = "__all__"
        read_only_fields = ['id', 'created', 'is_public']
        extra_kwargs = {
            "image": {'required': False},
        }
