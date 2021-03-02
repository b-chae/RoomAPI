from rest_framework import serializers
from users.serializers import RelatedUserSerializer
from .models import Room


class ReadRoomSerializer(serializers.ModelSerializer):

    user = RelatedUserSerializer()

    class Meta:
        model = Room
        exclude = ("modified",)


class WriteRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        exclude = ("user", "modified", "created")

    def validate(self, data):
        return data
