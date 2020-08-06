from rest_framework import serializers
from .utils import Util, User


class CreateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=4)
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)
    password = serializers.HiddenField(default=Util.get_encrypted_password())

    class Meta:
        model = User
        fields = 'email', 'first_name', 'last_name', 'password'

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email', 'Введенный email уже используется'})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'email', 'first_name', 'last_name'


class UserChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'email', 'first_name', 'last_name'
