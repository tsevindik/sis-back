from django.core.exceptions import MultipleObjectsReturned
from django.utils.translation import get_language, ugettext_lazy as _
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UniversityTransSerializer, UniversitySerializer, UniversityConfigSerializer
from .models import University, UniversityConfig, UniversityTrans


class UniversityConfigApi(APIView):
    @staticmethod
    def get_university():
        try:
            return University.objects.prefetch_related('universitytrans_set').get(is_primary=True)
        except University.DoesNotExist:
            err_msg = _('Birincil üniversite bulunamadı.')
            return Response({'err': err_msg})
        except MultipleObjectsReturned:
            err_msg = _('Birden çok obje döndürüldü.')
            return Response({'err': err_msg})

    @staticmethod
    def get_universityconfig():
        try:
            return UniversityConfig.objects.get()
        except UniversityConfig.DoesNotExist:
            err_msg = _('Universite ayarları bulunamadı.')
            return Response({'err': err_msg})

    @staticmethod
    def get_university_trans(university, exception_lang):
        try:
            return university.universitytrans_set.get_by_language(get_language())
        except UniversityTrans.DoesNotExist:
            return university.universitytrans_set.get_by_language(exception_lang)

    def get(self, request, format=None):
        university = self.get_university()
        universityconfig = self.get_universityconfig()
        university_trans = self.get_university_trans(university, universityconfig.default_language)

        university_serializer = UniversitySerializer(instance=university)
        university_trans_serializer = UniversityTransSerializer(instance=university_trans)
        university_config_serializer = UniversityConfigSerializer(instance=universityconfig)

        return Response({
            "university": {
                "neutral": university_serializer.data,
                "trans": university_trans_serializer.data,
            },
            "university_config": university_config_serializer.data,
        })
