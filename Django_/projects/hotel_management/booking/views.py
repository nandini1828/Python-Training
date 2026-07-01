from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ReservationForm, RoomFilterForm
from .models import Guest, Reservation, Room


def home(request):
    filter_form = RoomFilterForm(request.GET or None)
    rooms = Room.objects.filter(is_available=True)
    if filter_form.is_valid():
        room_type = filter_form.cleaned_data.get('room_type')
        if room_type:
            rooms = rooms.filter(room_type=room_type)
    reservation_form = ReservationForm(request.POST or None)
    if request.method == 'POST' and reservation_form.is_valid():
        room_id = request.POST.get('room_id')
        room = Room.objects.filter(id=room_id, is_available=True).first()
        if room:
            guest, _ = Guest.objects.get_or_create(
                email=reservation_form.cleaned_data['guest_email'],
                defaults={
                    'name': reservation_form.cleaned_data['guest_name'],
                    'phone': reservation_form.cleaned_data['guest_phone'],
                }
            )
            reservation = Reservation.objects.create(
                guest=guest,
                room=room,
                check_in=reservation_form.cleaned_data['check_in'],
                check_out=reservation_form.cleaned_data['check_out'],
                status='pending',
            )
            room.is_available = False
            room.save()
            messages.success(request, 'Your booking request has been submitted. Admin will review it shortly.')
            return redirect('reservation_confirmation', reservation_id=reservation.id)
        messages.error(request, 'The selected room is no longer available.')
    reservations = Reservation.objects.order_by('-created_at')[:5]
    return render(request, 'booking/home.html', {
        'rooms': rooms,
        'reservations': reservations,
        'filter_form': filter_form,
        'reservation_form': reservation_form,
    })


def reservation_confirmation(request, reservation_id):
    reservation = Reservation.objects.filter(id=reservation_id).select_related('guest', 'room').first()
    if not reservation:
        return redirect('home')
    return render(request, 'booking/confirmation.html', {
        'reservation': reservation,
    })


@login_required
@user_passes_test(lambda user: user.is_staff)
def manage_reservations(request):
    pending_requests = Reservation.objects.filter(status='pending').select_related('guest', 'room').order_by('-created_at')
    recent_reservations = Reservation.objects.order_by('-created_at').select_related('guest', 'room')[:20]
    return render(request, 'booking/manage_requests.html', {
        'pending_requests': pending_requests,
        'recent_reservations': recent_reservations,
    })


@login_required
@user_passes_test(lambda user: user.is_staff)
def manage_reservation_action(request, reservation_id, action):
    reservation = get_object_or_404(Reservation, id=reservation_id, status='pending')
    if request.method == 'POST':
        if action == 'approve':
            reservation.status = 'approved'
            reservation.save()
            messages.success(request, f'Reservation for {reservation.guest.name} has been approved.')
        elif action == 'reject':
            reservation.status = 'rejected'
            reservation.room.is_available = True
            reservation.room.save()
            reservation.save()
            messages.success(request, f'Reservation for {reservation.guest.name} has been rejected and the room is available again.')
        else:
            messages.error(request, 'Unknown reservation action.')
    return redirect('manage_reservations')
