from django.db import models

from apps.base.models import TimeStampModel
from apps.slots.models import Slot
from apps.users.models import User


class Booking(TimeStampModel):
    """
    Booking model representing a user's ticket purchase.

    Attributes:
        status (int): Booking status (BOOKED or CANCELLED).
        user (ForeignKey): User who made the booking.
        slot (ForeignKey): Slot for which the booking was made.
    """

    class Status(models.IntegerChoices):
        CANCELLED = 0
        BOOKED = 1

    status = models.IntegerField(choices=Status.choices, default=Status.BOOKED)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE, related_name="bookings")

    def __str__(self):
        return f"Booking #{self.id} - {self.user.email}"


class Seat(TimeStampModel):
    """
    BookingSeat model linking seats to a booking and slot.

    Attributes:
        row (str): Seat row identifier (e.g., A, B, C).
        number (int): Seat number within the row.
        booking (ForeignKey): Booking reference.
    """

    row = models.PositiveIntegerField()
    number = models.PositiveIntegerField()

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name="seats")

    def __str__(self):
        return f"{self.row} - {self.number}"
