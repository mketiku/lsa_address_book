from django.db import models
from django.utils import timezone

class AddressEntry(models.Model):
    owner = models.CharField(max_length=200)
    first_name =  models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email_address = models.EmailField()
    street_address = models.CharField(max_length=200)

    @property
    def name(self):
        return ("{} {}").format(self.first_name, self.last_name)

    def __str__(self):
        res = "Name: {} \n Phone: {} \n Email: {} \n  Phone: {} \n Street Address: {}, \n ".format(
            self.name, self.phone_number, self.email_address,
            self.street_address)

        return res
    def __repr__(self):
        res = "Name: {}".format(
            self.name)

        return res
