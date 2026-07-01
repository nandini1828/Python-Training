from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=32, unique=True)
    address = models.TextField()
    city = models.CharField(max_length=80)
    country = models.CharField(max_length=80)
    phone = models.CharField(max_length=30)
    email = models.EmailField()

    class Meta:
        ordering = ['name']
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'

    def __str__(self):
        return f"{self.name} ({self.code})"


class Branch(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='branches')
    name = models.CharField(max_length=120)
    floor_count = models.PositiveIntegerField(default=1)
    address = models.TextField(blank=True)

    class Meta:
        ordering = ['hotel', 'name']
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'

    def __str__(self):
        return f"{self.hotel.name} / {self.name}"


class RoomType(models.Model):
    code = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=80)
    description = models.TextField(blank=True)
    max_guests = models.PositiveSmallIntegerField(default=2)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['name']
        verbose_name = 'Room Type'
        verbose_name_plural = 'Room Types'

    def __str__(self):
        return self.name


class Amenity(models.Model):
    code = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Amenity'
        verbose_name_plural = 'Amenities'

    def __str__(self):
        return self.name


class Room(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.CharField(max_length=20)
    room_type = models.ForeignKey(RoomType, on_delete=models.PROTECT, related_name='rooms')
    amenities = models.ManyToManyField(Amenity, blank=True, related_name='rooms')
    is_available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = [['branch', 'room_number']]
        ordering = ['branch', 'room_number']
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'

    def __str__(self):
        return f"{self.branch.name} - {self.room_number}"
