from django.db import models

from .user import User


class UserResetToken(models.Model):
    """
    A model that stores SMS codes sent to a user's number.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_id = models.CharField(max_length=255)
    content = models.TextField(editable=False)
    expire_date = models.DateTimeField(db_index=True)
    is_used = models.BooleanField(default=False)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.phone

    @property
    def full_name(self):
        return self.user.full_name

    @property
    def phone(self):
        return self.user.phone
