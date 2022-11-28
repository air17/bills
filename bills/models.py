from django.db import models


class Bill(models.Model):
    """Bill model"""
    client_name = models.CharField("Client name", max_length=100)
    client_org = models.CharField("Client organization", max_length=100)
    number = models.IntegerField("Bill number")
    sum = models.DecimalField("Bill sum", decimal_places=2, max_digits=12)
    date = models.DateField("Date")
    service = models.TextField("Service name")

    def __str__(self):
        return f"{self.client_name} from {self.client_org} №{self.number}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["client_name", "client_org", "number"],
                name="unique bill",
            )
        ]
