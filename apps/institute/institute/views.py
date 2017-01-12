from django.core.exceptions import MultipleObjectsReturned
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import University, UniversityConfig
from .serializers import UniversitySerializer, UniversityConfigSerializer


class UniversityConfigApi(APIView):
    def get(self, request, format=None):
        try:
            university = University.objects.get(is_primary=True)
            university_serializer = UniversitySerializer(university)
            university_config = UniversityConfig()
            university_config_serializer = UniversityConfigSerializer(university_config)
            return Response({
                'university': university_serializer.data,
                'university_config': university_config_serializer.data,
            })
        except MultipleObjectsReturned:
            return Response({'err': 'Multiple Objects Returned.'})
        except University.DoesNotExist:
            return Response({'err': 'University does not exists.'})
        except UniversityConfig.DoesNotExist:
            return Response({'err': 'University config does not exists.'})
