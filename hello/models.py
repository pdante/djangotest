from django.core.validators import RegexValidator
from django.db import models
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms


# Create your models here.

class User(models.Model):
    class Role(models.TextChoices):
        rider = "R", _("Rider")
        driver = "D", _("Driver")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'[1-9][0-9]{2}-[1-9][0-9]{2}-[0-9]{4}$')],
        help_text=_("format: xxx-xxx-xxxx"))
    role = models.CharField(max_length=1, choices=Role.choices)
    password = models.CharField(max_length=25, null=False, blank=False)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)


class Ride(models.Model):
    class Status(models.TextChoices):
        HAVE_NOT_LEFT = "HNL", _("Haven't Left")
        EN_ROUTE = "EN", _("En Route")
        LOST = "L", _("Lost")
        ARRIVED = "AR", _("Arrived")
        NOT_COMING = "NC", _("Not Coming")

    status = models.CharField(max_length=3, choices=Status.choices)
    rider = models.ForeignKey(User, on_delete=models.CASCADE,)
    from_location = models.CharField(max_length=100, null=False, blank=False)
    to_location = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return "from "+ str(self.from_location) + " to " + str(self.to_location)


class RideEvent(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE,)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(null=False, blank=False)


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', "role"]


class RideForm(ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.filter(first_name='*'))
    class Meta:
        model = Ride
        fields = ['status', 'rider', 'from_location', 'to_location']


class RideEventForm(ModelForm):
    class Meta:
        model = RideEvent
        fields = ['ride', 'description', 'created_at']
