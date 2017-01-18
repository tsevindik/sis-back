class MultipleFieldLookupMixin(object):
    def get_object(self):
        from rest_framework.generics import get_object_or_404
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]:
                filter[field] = self.kwargs[field]
        return get_object_or_404(queryset, **filter)
