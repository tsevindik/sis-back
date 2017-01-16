from rest_framework import serializers

from ..models import main, trans
from .trans import UniversityTransSerializer


class UniversitySerializer(serializers.ModelSerializer):
    trans = UniversityTransSerializer(many=True)

    class Meta:
        model = main.University
        fields = ('trans',)

    def create(self, validated_data):
        trans_data = validated_data.pop('trans')
        university = main.University.objects.create(**validated_data)
        for singular_trans_data in trans_data:
            trans.UniversityTrans.objects.create(neutral=university, **singular_trans_data)
        return university


class UniversityConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = main.UniversityConfig
        fields = ('language', 'major_count', 'major_gpa', 'minor_count', 'minor_gpa')
