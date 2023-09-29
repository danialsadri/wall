from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Ad
from .serializers import AdSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .pagination import StandardResultsSetPagination
from .permissions import IsPublisherOrReadOnly


class AdListView(APIView, StandardResultsSetPagination):
    serializer_class = AdSerializer

    def get(self, request: Request):
        ads = Ad.objects.filter(is_public=True)
        result = self.paginate_queryset(ads, request)
        ad_serializer = AdSerializer(instance=result, many=True)
        return self.get_paginated_response(data=ad_serializer.data)


class AdDetailView(APIView):
    serializer_class = AdSerializer

    def get(self, request: Request, ad_id):
        ad = get_object_or_404(Ad, id=ad_id, is_public=True)
        ad_serializer = AdSerializer(instance=ad)
        return Response(data=ad_serializer.data, status=status.HTTP_200_OK)


class AdCreateView(APIView):
    serializer_class = AdSerializer

    def post(self, request: Request):
        ad_serializer = AdSerializer(data=request.data)
        if ad_serializer.is_valid():
            ad_serializer.validated_data['publisher'] = request.user
            ad_serializer.save()
            return Response(data=ad_serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=ad_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdUpdateView(APIView):
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, IsPublisherOrReadOnly]

    def put(self, request: Request, ad_id):
        ad = get_object_or_404(Ad, id=ad_id, is_public=True)
        ad_serializer = AdSerializer(instance=ad, data=request.data, partial=True)
        if ad_serializer.is_valid():
            ad_serializer.save()
            return Response(data=ad_serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(data=ad_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddDeleteView(APIView):
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, IsPublisherOrReadOnly]

    def delete(self, request: Request, ad_id):
        ad = get_object_or_404(Ad, id=ad_id, is_public=True)
        ad.delete()
        return Response(data=None, status=status.HTTP_204_NO_CONTENT)


class AdSearchView(APIView, StandardResultsSetPagination):
    serializer_class = AdSerializer

    def get(self, request: Request):
        query = request.query_params.get('query')
        queryset = Ad.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        result = self.paginate_queryset(queryset, request)
        ad_serializer = AdSerializer(instance=result, many=True)
        return Response(data=ad_serializer.data, status=status.HTTP_200_OK)
