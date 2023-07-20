from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        if AbstractUser.get_full_name(self) != '':
            name = AbstractUser.get_full_name(self)
        else:
            name = self.username
        return name