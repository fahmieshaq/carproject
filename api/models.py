from django.db import models


class Branch(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    created_on = models.DateField(null=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    branch = models.ForeignKey(
        Branch,
        on_delete=models.DO_NOTHING,
        related_name='vehicles'
    )
    color = models.ForeignKey(
        Color,
        on_delete=models.DO_NOTHING,
        related_name='vehicles'
    )

    def __str__(self):
        return self.name


class VehicleDetail(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=10)
    vehicle = models.OneToOneField(
        Vehicle,
        on_delete=models.CASCADE,
        related_name='vehicledetail'
    )
    registered_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.price


class Renter(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    vehicles = models.ManyToManyField(
        'Vehicle',
        through='RenterVehicle',
        related_name='renters'
    )

    def __str__(self):
        return self.firstname + " " + self.lastname

    """ Adding m2m field (vehicles = models.ManyToManyField) makes renter output looks like:
    {
        "id": 1,
        "url": "http://127.0.0.1:8080/api/v1/renters/1/",
        "firstname": "Fahmi",
        "lastname": "Eshaq",
        "vehicles": [
            "http://127.0.0.1:8080/api/v1/vehicles/1/",
            "http://127.0.0.1:8080/api/v1/vehicles/2/",
            "http://127.0.0.1:8080/api/v1/vehicles/3/"
        ]
    },
    {
        "id": 2,
        "url": "http://127.0.0.1:8080/api/v1/renters/2/",
        "firstname": "Esra",
        "lastname": "Bob",
        "vehicles": [
            "http://127.0.0.1:8080/api/v1/vehicles/1/",
            "http://127.0.0.1:8080/api/v1/vehicles/2/"
        ]
    }
    """

class RenterVehicle(models.Model):
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date_rented = models.DateField(null=True)
