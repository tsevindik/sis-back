# from django.utils.translation import ugettext_lazy as _

from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.rest.mixins import MultipleFieldLookupMixin
from utils.rest.views import ObjectAPIView
from .serializers import UniversityTransSerializer, UniversitySerializer, UniversityConfigSerializer
from .models import UniversityConfig, UniversityTrans


class UniversityConfigHomeView(APIView):
    @staticmethod
    def get_university_config():
        return UniversityConfig.objects.prefetch_related('primary_university').get_single()

    @staticmethod
    def get_university_trans(university, exception_lang):
        try:
            from django.utils.translation import get_language
            return university.universitytrans_set.get_by_language(get_language())
        except UniversityTrans.DoesNotExist:
            return university.universitytrans_set.get_by_language(exception_lang)

    def get(self, request, format=None):
        university_config = self.get_university_config()
        university = university_config.primary_university
        university_trans = self.get_university_trans(university, university_config.default_language)

        university_config_serializer = UniversityConfigSerializer(instance=university_config)
        university_serializer = UniversitySerializer(instance=university)
        university_trans_serializer = UniversityTransSerializer(instance=university_trans)

        return Response({
            "university": {
                "neutral": university_serializer.data,
                "trans": university_trans_serializer.data,
            },
            "university_config": university_config_serializer.data,
        })


class PrimaryUniversityView(UpdateModelMixin, ObjectAPIView):
    serializer_class = UniversitySerializer

    def get_queryset(self):
        return UniversityConfig.objects.get_primary_university()

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


class UniversityConfigView(UpdateModelMixin, ObjectAPIView):
    serializer_class = UniversityConfigSerializer

    def get_queryset(self):
        return UniversityConfig.objects.get_single()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
