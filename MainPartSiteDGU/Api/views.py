import datetime

from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from six import text_type

from .serializers import *
from Students import models
from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response


class MyTokenObtainSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # data = super(TokenObtainPairSerializer, self).validate(attrs)
        # print(attrs['username'])
        data = super(TokenObtainPairSerializer, self).validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = text_type(refresh)
        if self.user.is_superuser:
            new_token = refresh.access_token
            data['access'] = text_type(new_token)
        else:
            data['access'] = text_type(refresh.access_token)

        return data


class MyTokenObtainView(TokenObtainPairView):
    serializer_class = MyTokenObtainSerializer


class PricesPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'size'

    # def get_paginated_response(self, data):
    #     return Response({
    #         'results': data,
    #         'count': self.page.paginator.count
    #     })


class ListStudents(generics.ListAPIView):
    queryset = models.ProfileStudent.objects.select_related('student', 'direction') \
        .only('student', 'direction', 'course', 'student__first_name', 'student__last_name', 'student__middle_name')
    serializer_class = SerializerListStudents
    filterset_fields = [
        'student'
    ]

    # permission_classes = (IsAuthenticated,)


class DitailStudents(generics.RetrieveAPIView):
    queryset = ProfileStudent.objects.all()
    serializer_class = SerializerDitailStudents
    # permission_classes = (IsAuthenticated,)


class test(APIView):
    def get(self):
        model = ProfileStudent.objects.all()
        s = SerializerDitailStudents(model)
        return Response({'s': s})
