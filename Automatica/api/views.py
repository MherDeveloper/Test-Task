from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response
from api.models import Visit, Store
from api.serializers import VisitModelSerializer, StoreListSerializer


class VisitViewSet(viewsets.ModelViewSet):

    queryset = Visit.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VisitModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['store__worker__phone_number']

    def get_queryset(self):
        if 'search' in self.request.query_params:
            return self.queryset.filter(store__worker__phone_number=self.request.query_params['search'])
        return self.queryset

    def list(self, request, *args, **kwargs):
        if 'search' in request.GET:
            store_ids = self.get_queryset().values_list('store_id', flat=True)
            serializer = StoreListSerializer(Store.objects.filter(id__in=store_ids), many=True)
            return Response(serializer.data)
        return super().list(request, *args, **kwargs)
