"""Utils for the booking app."""
from django.contrib.sessions.models import Session

from .models import Booking


def get_booking(request):
    booking = None
    if request.user.is_authenticated():
        try:
            booking = Booking.objects.get(
                user=request.user,
                booking_status__slug='inprogress')
        except Booking.DoesNotExist:
            # The user does not have any open bookings
            pass
    else:
        session = Session.objects.get(
            session_key=request.session.session_key)
        try:
            booking = Booking.objects.get(session=session)
        except Booking.DoesNotExist:
            # The user does not have any bookings in his session
            pass
    return booking

def persist_booking(booking, user):
    if booking is not None:
        existing_bookings = Booking.objects.filter(
            user=user, booking_status__slug='inprogress').exclude(
            pk=booking.pk)
        existing_bookings.delete()

        booking.session = None
        booking.user = user
        booking.save()