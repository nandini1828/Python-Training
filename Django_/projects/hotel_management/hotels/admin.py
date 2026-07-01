from django.contrib import admin
from .models import Amenity, Branch, Hotel, Room, RoomType


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'city', 'country', 'phone', 'email')
    search_fields = ('name', 'code', 'city', 'country')


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'hotel', 'floor_count')
    list_filter = ('hotel',)
    search_fields = ('name',)


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'max_guests', 'base_price')
    search_fields = ('name', 'code')


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'branch', 'room_type', 'is_available', 'price')
    list_filter = ('branch', 'room_type', 'is_available')
    search_fields = ('room_number', 'branch__name')
