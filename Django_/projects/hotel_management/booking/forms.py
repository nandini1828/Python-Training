from django import forms
from django.utils import timezone

ROOM_TYPE_CHOICES = [
    ('', 'All room types'),
    ('single', 'Single'),
    ('double', 'Double'),
    ('suite', 'Suite'),
]

class RoomFilterForm(forms.Form):
    room_type = forms.ChoiceField(choices=ROOM_TYPE_CHOICES, required=False)
    check_in = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    check_out = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    def clean(self):
        cleaned = super().clean()
        check_in = cleaned.get('check_in')
        check_out = cleaned.get('check_out')
        if check_in and check_out and check_out <= check_in:
            raise forms.ValidationError('Check-out must be after check-in.')
        if check_in and check_in < timezone.localdate():
            raise forms.ValidationError('Check-in date cannot be in the past.')
        return cleaned

class ReservationForm(forms.Form):
    guest_name = forms.CharField(max_length=100)
    guest_email = forms.EmailField()
    guest_phone = forms.CharField(max_length=20, required=False)
    check_in = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    check_out = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    def clean(self):
        cleaned = super().clean()
        check_in = cleaned.get('check_in')
        check_out = cleaned.get('check_out')
        if check_in and check_out and check_out <= check_in:
            raise forms.ValidationError('Check-out must be after check-in.')
        if check_in and check_in < timezone.localdate():
            raise forms.ValidationError('Check-in date cannot be in the past.')
        return cleaned
