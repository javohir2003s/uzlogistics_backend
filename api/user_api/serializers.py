from rest_framework import serializers
from users.models import User

class RegisterUserSerializer(serializers.ModelSerializer):
    tg_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = User
        fields = ['tg_id', 'full_name', 'phone_number', 'role', 'language']

    def validate_phone_number(self, value):
        user = User.objects.filter(phone_number=value)
        if user:
            raise serializers.ValidationError('Phone number already exists')
        return value

    def validate_tg_id(self, value):
        user = User.objects.filter(tg_id=value)
        if user:
            raise serializers.ValidationError('TG ID already exists')
        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['tg_id', 'full_name', 'phone_number', 'role', 'language', 'sub_start', 'sub_end']

