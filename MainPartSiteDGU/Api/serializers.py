from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.timezone import now
from rest_framework import serializers
from rest_framework.settings import api_settings

from Students.models import *


class SerializerListStudents(serializers.ModelSerializer):
    direction = serializers.CharField(source='direction.name')
    course = serializers.CharField(source='get_course_display')
    days = serializers.SerializerMethodField()

    class Meta:
        model = ProfileStudent
        fields = ['full_name', 'course', 'direction', 'days']

    def get_days(self, obj):
        return 'sds'


class SerializerDitailStudents(serializers.ModelSerializer):
    direction = serializers.CharField(source='direction.name')
    student_status = serializers.CharField(source='student_status.name')
    course = serializers.CharField(source='get_course_display')
    organization = serializers.CharField(source='get_organization_display')

    class Meta:
        model = ProfileStudent
        fields = ['full_name', 'course', 'direction', 'organization', 'student_status']
