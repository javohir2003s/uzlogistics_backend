from datetime import datetime, timedelta
from django.db import models
from users.models import User
from django.utils import timezone


class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="districts")
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('region', 'name')

    def __str__(self):
        return f"{self.name}, {self.region.name}"


class Location(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="locations")

    def __str__(self):
        return f"{self.district.name}, {self.district.region.name}"


def default_available_date():
    return (timezone.now() + timedelta(days=1)).date()

class Cargo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cargos')
    from_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='cargo_departures')
    to_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='cargo_arrivals')
    cargo_type = models.CharField(max_length=120, blank=True, null=True)
    weight_kgs = models.FloatField()
    description = models.TextField(blank=True)
    date_available = models.DateField(default=default_available_date)
    created_at = models.DateTimeField(auto_now_add=True)
    price_offer = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.full_name} | {self.from_location} → {self.to_location} ({self.cargo_type})"


class Truck(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trucks')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='trucks')
    capacity_kg = models.FloatField()
    volume_m3 = models.FloatField()
    has_refrigeration = models.BooleanField(default=False)
    is_available = models.BooleanField(default=False)  # 🟢 “Men bo'shman”
    is_busy = models.BooleanField(default=False)


class Order(models.Model):
    STATUS_CHOICES = (
        ('assigned', 'Bajarildi'),
        ('cancelled', 'Bekor qilindi'),
    )
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT, related_name='orders')
    truck = models.ForeignKey(Truck, on_delete=models.PROTECT, related_name='orders')
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='assigned')
    created_at = models.DateTimeField(auto_now_add=True)