from django.conf import settings
from django.db import models


class Resident(models.Model):
    """
    A Resident is a member of the village. They can join subcomittees and
    have other associated information to them. it is a one-to-one relation
    to the UserModel
    """

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # relating to the person:
    # note that firstname, lastname, email, etc, are handled by django

    house_number = models.CharField(
        max_length=4,
    )

    short_bio = models.TextField("About You")

    birthday = models.DateField(blank=True)
