from rest_framework import serializers
from users.serializers import RelatedUserSerializer
from .models import Room


class RoomSerializer(serializers.ModelSerializer):

    user = RelatedUserSerializer(read_only=True)

    is_favs = serializers.SerializerMethodField()

    class Meta:
        model = Room
        exclude = ["modified", ]
        read_only_fields = ['user', 'id', 'created', 'updated', "is_favs"]

    def validate(self, data):
        return data

    def get_is_favs(self, obj):
        request = self.context.get("request")
        if request:
            user = request.user
            if user.is_authenticated:
                return obj in user.favs.all()
        return False

    def create(self, validated_data):
        user = self.context.get("request").user
        room = Room.objects.create(**validated_data, user=user)
        return room
