from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()
    