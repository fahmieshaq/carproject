from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers
from rest_framework.decorators import action
from rest_framework.response import Response


class BranchModelViewSet(ModelViewSet):
    queryset = models.Branch.objects.all()
    serializer_class = serializers.BranchModelSerializer

    @action(methods=['get'], detail=False, url_path='getaclass')
    def get_a_class(self, request):
        data = models.Branch.objects.filter(name__iexact='A-Branch')

        """
        https://www.django-rest-framework.org/api-guide/serializers/#absolute-and-relative-urls
                
        When instantiating a HyperlinkedModelSerializer you must include the current request in the serializer context,
        Doing so will ensure that the hyperlinks can include an appropriate hostname, so that the resulting representation uses fully qualified URLs, such as:
        http://api.example.com/accounts/1/ rather than relative URLs, such as /accounts/1/
        If you do want to use relative URLs, you should explicitly pass {'request': None} in the serializer context.
        """
        serializer = serializers.BranchModelSerializer(data, many=True, context={'request': request})
        return Response(serializer.data)


class VehicleModelViewSet(ModelViewSet):
    queryset = models.Vehicle.objects.all()
    serializer_class = serializers.VehicleModelSerializer


class VehicleDetailModelViewSet(ModelViewSet):
    queryset = models.VehicleDetail.objects.all()
    serializer_class = serializers.VehicleDetailModelSerializer


class RenterModelViewSet(ModelViewSet):
    queryset = models.Renter.objects.all()
    serializer_class = serializers.RenterModelSerializer


class RenterVehicleModelViewSet(ModelViewSet):
    queryset = models.RenterVehicle.objects.all()
    serializer_class = serializers.RenterVehicleSerializer
