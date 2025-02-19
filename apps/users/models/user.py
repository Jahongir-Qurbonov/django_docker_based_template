from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from ..managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, verbose_name=_("Username"), unique=True, db_index=True)
    phone = models.CharField(max_length=12, verbose_name=_("Phone number"), unique=True, db_index=True)

    email = models.EmailField(
        max_length=255,
        verbose_name=_("Email"),
        unique=True,
        db_index=True,
        null=True,
        blank=True,
    )

    first_name = models.CharField(max_length=50, verbose_name=_("First name"), null=True)
    last_name = models.CharField(max_length=50, verbose_name=_("Last name"), null=True)
    middle_name = models.CharField(max_length=50, verbose_name=_("Last name"), null=True)

    is_superuser = models.BooleanField(default=False, verbose_name=_("Super user"))
    is_staff = models.BooleanField(default=False, verbose_name=_("Staff user"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active user"))
    is_verified = models.BooleanField(default=False, verbose_name=_("Verified user"))

    modified_at = models.DateTimeField(auto_now=True, verbose_name=_("Modified date"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created date"))

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return " ".join(filter(None, [self.last_name, self.first_name, self.middle_name]))
