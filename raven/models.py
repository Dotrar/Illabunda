from django.conf import settings
from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import StreamFieldPanel

# Create your models here.

class HomePage(Page):
    # https://docs.wagtail.io/en/stable/reference/streamfield/blocks.html#streamfield-block-reference
    body = StreamField(
        [
            ("heading", blocks.CharBlock(form_classname="full title")),
            ("subheading", blocks.CharBlock(form_classname="sub title")),
            ("paragraph", blocks.RichTextBlock()),
            ("image", ImageChooserBlock()),
        ]
    )

    content_panels = Page.content_panels + [StreamFieldPanel("body")]


class ResidentManager(BaseUserManager):
    def _create_user(self, email, password, **kwargs):
        user = self.model(email=self.normalize_email(email), is_active=True, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **kwargs):
        kwargs.setdefault("is_superuser", False)
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault("is_superuser", True)
        return self._create_user(email, password, **kwargs)


class Resident(AbstractBaseUser, PermissionsMixin):
    """
    A Resident is a member of the village. They can join subcomittees and
    have other associated information to them.

    We use this as the AUTH_USER_MODEL as we want to change how the user logs
    in, and we don't want to introduce "usernames" - things should be a little
    more humane and personal
    """

    USERNAME_FIELD = "email"

    email = models.EmailField(unique=True, blank=False)
    is_active = models.BooleanField(default=False)

    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)

    def get_full_name(self):
        return f"{self.firstname} {self.lastname}"

    def get_short_name(self):
        return f"{self.firstname} ({self.house_number})"

    house_number = models.CharField(
        max_length=4,
    )

    short_bio = models.TextField(blank=True)

    birthday = models.DateField(blank=True)

    objects = ResidentManager()
