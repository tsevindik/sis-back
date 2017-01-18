from rest_framework import serializers

from ..models import main


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = main.University
        fields = ('official_name',)


class UniversityConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = main.UniversityConfig
        fields = ('default_language', 'major_count', 'major_gpa', 'minor_count', 'minor_gpa')
