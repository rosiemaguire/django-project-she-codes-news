from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = AbstractUser.get_full_name(self)
        return full_name