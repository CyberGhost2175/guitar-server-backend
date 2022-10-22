from dataclasses import fields
from rest_framework import serializers

from apps.guitar_server.models import *


class GuitarSerializer(serializers.ModelSerializer):
    class Meta:
        model= Guitar
        fields = "__all__"

class AmplifierSerializer(serializers.ModelSerializer):
    class Meta:
        model= Amplifier
        fields= "__all__"
class PickSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pick
        fields = "__all__"

class CapoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Capo
        fields="__all__"



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password"
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance        


