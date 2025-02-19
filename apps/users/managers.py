import typing

from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

if typing.TYPE_CHECKING:
    from .models import User


class UserManager(BaseUserManager):
    model: type["User"]

    def create_user(self, username: str, password: str | None = None, **kwargs):
        if username is None:
            raise TypeError({"success": False, "detail": _("User should have a phone")})

        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username: str, password: str | None = None, **kwargs):
        user = self.create_user(username=username, password=password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.is_verified = True
        user.save(using=self._db)

        return user
