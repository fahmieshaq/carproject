from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('branches', views.BranchModelViewSet)
router.register('vehicles', views.VehicleModelViewSet)
router.register('vehicledetails', views.VehicleDetailModelViewSet)
router.register('renters', views.RenterModelViewSet)
router.register('rentervehicle', views.RenterVehicleModelViewSet)


urlpatterns = [
    path('', include(router.urls))
]