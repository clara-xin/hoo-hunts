from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Clue(models.Model):
    title = models.CharField(max_length=100)
    clue_text = models.TextField()
    hint_text = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    multiple_choice = models.CharField(max_length=200)
    created_by = models.CharField(max_length=25)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)
    decline_reason = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    PENDING = 0
    ACCEPTED = 1
    DENIED = 2
    VERIFICATION_STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (DENIED, 'Denied'),
    )

    was_verified = models.IntegerField(choices=VERIFICATION_STATUS_CHOICES, default=PENDING)

    def get_was_verified_display(self):
        return dict(self.VERIFICATION_STATUS_CHOICES).get(self.was_verified, 'Unknown')

    def is_pending(self):
        return self.was_verified == self.PENDING

    def is_accepted(self):
        return self.was_verified == self.ACCEPTED

    def is_denied(self):
        return self.was_verified == self.DENIED
    def clue(self):
        return self.clue_text
    def hint(self):
        return self.hint_text
    def mult(self):
        return self.multiple_choice
    def make_verified(self):
        self.was_verified = True
        return
    def status(self):
        return self.was_verified
    def get_lat(self):
        return self.latitude
    def get_lon(self):
        return self.longitude

    
class Player(models.Model):
    name = models.CharField(max_length=25)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    submission = models.ForeignKey(Clue, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)