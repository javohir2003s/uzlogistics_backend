from rest_framework.generics import CreateAPIView
from .serializers import RegisterUserSerializer
from users.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404


class RegisterUserAPIView(CreateAPIView):
    serializer_class = RegisterUserSerializer
    queryset = User.objects.all()


class UserAPIView(APIView):
    def get(self, request, tg_id):
        user = get_object_or_404(User, tg_id=tg_id)
        serializer = RegisterUserSerializer(user, many=False)
        return Response({'user': serializer.data}, status=200)
