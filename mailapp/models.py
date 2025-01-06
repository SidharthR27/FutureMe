from django.db import models

# Create your models here.

from django.db import models

class FutureMail(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    send_whatsapp = models.BooleanField(default=False)  # Yes/No option for WhatsApp
    mobile_number = models.CharField(max_length=15, blank=True, null=True)  # Optional field for WhatsApp

    def __str__(self):
        return self.name
