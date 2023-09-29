from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .serializers import UserSerializer


class ProfileView(APIView):
    serializer_class = UserSerializer

    def get(self, request: Request):
        user_serializer = UserSerializer(instance=request.user)
        return Response(data=user_serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request):
        user_serializer = UserSerializer(instance=request.user, data=request.data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(data=user_serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(data=user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
