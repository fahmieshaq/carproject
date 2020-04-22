from rest_framework import serializers
from . import models


class BranchModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Branch
        fields = ('id', 'url', 'name', 'city')  # you can add 'vehicles' too.


class VehicleModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Vehicle
        fields = ('id', 'url', 'name', 'type', 'branch_id', 'branch', 'renters')


class VehicleDetailModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.VehicleDetail
        fields = ('id', 'url', 'price', 'vehicle_id', 'vehicle')


class RenterModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Renter
        fields = ('id', 'url', 'firstname', 'lastname', 'vehicles')


class RenterVehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.RenterVehicle
        fields = ('id', 'url', 'renter_id', 'renter', 'vehicle_id', 'vehicle', 'date_rented')
