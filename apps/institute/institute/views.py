from django.utils.translation import ugettext_lazy as _

from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.rest.mixins import MultipleFieldLookupMixin
from utils.rest.views import GenericObjectAPIView
from .serializers import UniversityTransSerializer, UniversitySerializer, UniversityConfigSerializer
from .models import University, UniversityConfig, UniversityTrans


class UniversityConfigHomeView(APIView):
    @staticmethod
    def get_university():
        return University.objects.prefetch_related('universitytrans_set').get_primary()

    @staticmethod
    def get_university_config():
        return UniversityConfig.objects.get_single()

    @staticmethod
    def get_university_trans(university, exception_lang):
        try:
            from django.utils.translation import get_language
            return university.universitytrans_set.get_by_language(get_language())
        except UniversityTrans.DoesNotExist:
            return university.universitytrans_set.get_by_language(exception_lang)

    def get(self, request, format=None):
        university = self.get_university()
        university_config = self.get_university_config()
        university_trans = self.get_university_trans(university, university_config.default_language)

        university_serializer = UniversitySerializer(instance=university)
        university_trans_serializer = UniversityTransSerializer(instance=university_trans)
        university_config_serializer = UniversityConfigSerializer(instance=university_config)

        return Response({
            "university": {
                "neutral": university_serializer.data,
                "trans": university_trans_serializer.data,
            },
            "university_config": university_config_serializer.data,
        })


class PrimaryUniversityView(UpdateModelMixin, GenericObjectAPIView):
    queryset = University.objects.get_primary()
    serializer_class = UniversitySerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class UniversityTransView(CreateAPIView):
    queryset = UniversityTrans.objects.all()
    serializer_class = UniversityTransSerializer
    lookup_field = "neutral"


class UniversityTransByNeutralIdView(ListAPIView):
    queryset = UniversityTrans.objects.all()
    serializer_class = UniversityTransSerializer
    lookup_field = "neutral"


class UniversityTransByNeutralIdLanguageView(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = UniversityTrans.objects.all()
    serializer_class = UniversityTransSerializer
    lookup_fields = ("language_code", "neutral")


class UniversityConfigView(UpdateModelMixin, GenericObjectAPIView):
    queryset = UniversityConfig.objects.get()
    serializer_class = UniversityConfigSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
