from rest_framework import serializers
from users.serializers import RelatedUserSerializer
from .models import Room


class RoomSerializer(serializers.ModelSerializer):

    user = RelatedUserSerializer()

    class Meta:
        model = Room
        exclude = ["modified", ]
        read_only_fields = ['users', 'id', 'created', 'updated', ]

    def validate(self, data):
        return data
