from rest_framework import serializers
from cargo.models import Cargo, Region, District, Location
from users.models import User


class GetRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']


class GetDistrictSerializer(serializers.ModelSerializer):
    region = GetRegionSerializer()
    class Meta:
        model = District
        fields = ['id', 'region', 'name']


class CreateLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'district']


class GetLocationSerializer(serializers.ModelSerializer):
    district = GetDistrictSerializer()# yoki DistrictSerializer qilib berish mumkin

    class Meta:
        model = Location
        fields = ['id', 'district',]



class CreateCargoSerializer(serializers.ModelSerializer):
    tg_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Cargo
        fields = [
            'id',
            'tg_id', 'from_location', 'to_location',
            'weight_kgs', 'description',
        ]
        extra_kwargs = {
            'id': {'read_only': True}
        }

    def create(self, validated_data):
        tg_id = validated_data.pop('tg_id')
        user = User.objects.get(tg_id=tg_id)
        return Cargo.objects.create(user=user, **validated_data)


class GetCargoSerializer(serializers.ModelSerializer):
    from_location = GetLocationSerializer()
    to_location = GetLocationSerializer()

    class Meta:
        model = Cargo
        fields = [
            'from_location',
            'to_location',
            'weight_kgs',
            'description',
            'created_at',
            ]
