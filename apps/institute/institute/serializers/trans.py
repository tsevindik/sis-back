from rest_framework import serializers

from ..models import trans


class UniversityTransSerializer(serializers.ModelSerializer):
    class Meta:
        model = trans.UniversityTrans
