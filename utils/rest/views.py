from django.http import Http404
from django.utils.translation import ugettext_lazy as _

from rest_framework.generics import GenericAPIView


class QueryAPIView(GenericAPIView):
    def get_object(self):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            obj = queryset.get()
            self.check_object_permissions(self.request, obj)
            return obj
        except self.queryset.model.DoesNotExist:
            raise Http404(_("Nesne bulunamadı."))


class ObjectAPIView(GenericAPIView):
    def get_object(self):
        try:
            obj = self.filter_queryset(self.get_queryset())
            self.check_object_permissions(self.request, obj)
            return obj
        except self.queryset.model.DoesNotExist:
            raise Http404(_("Nesne bulunamadı."))
