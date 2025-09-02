from rest_framework.generics import ListAPIView, RetrieveAPIView, GenericAPIView, CreateAPIView
from cargo.models import Region, District, Cargo, Location
from .serializers import GetRegionSerializer, GetDistrictSerializer, CreateCargoSerializer, CreateLocationSerializer, \
    GetCargoSerializer


class RegionListAPIView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = GetRegionSerializer


class DistrictByRegionAPIView(ListAPIView):
    queryset = District.objects.all()
    serializer_class = GetDistrictSerializer

    def get_queryset(self):
        region_id = self.kwargs['region_id']
        return District.objects.filter(region_id=region_id)


class CreateCargoAPIView(CreateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CreateCargoSerializer


class CreateLocationAPIView(CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = CreateLocationSerializer


class GetDetailCargoAPIView(RetrieveAPIView):
    queryset = Cargo.objects.all()
    serializer_class = GetCargoSerializer

    def get_queryset(self):
        tg_id = self.request.query_params.get("tg_id")
        return super().get_queryset().filter(user__tg_id=tg_id)
