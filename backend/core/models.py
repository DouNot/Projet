from django.conf import settings
from django.db import models


class LegalEntity(models.Model):
    PERSON = "PERSON"
    SCI = "SCI"
    TYPE_CHOICES = [(PERSON, "Personne physique"), (SCI, "SCI")]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="entities"
    )
    name = models.CharField(max_length=120)
    type = models.CharField(max_length=6, choices=TYPE_CHOICES, default=PERSON)

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"


class Property(models.Model):
    entity = models.ForeignKey(
        LegalEntity, on_delete=models.CASCADE, related_name="properties"
    )
    address = models.CharField(max_length=255)
    surface = models.DecimalField(max_digits=7, decimal_places=2)  # m²
    purchase_price = models.DecimalField(max_digits=12, decimal_places=2)
    photo = models.ImageField(upload_to="property_photos/", blank=True, null=True)

    def __str__(self):
        return self.address


class Loan(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="loans"
    )
    bank = models.CharField(max_length=120)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    rate = models.DecimalField(max_digits=5, decimal_places=2)  # ex : 1.45 %
    duration_months = models.PositiveIntegerField()
    start_date = models.DateField()

    def __str__(self):
        return f"{self.bank} – {self.amount} €"


class Lease(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="leases"
    )
    tenant_name = models.CharField(max_length=120)
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    lease_pdf = models.FileField(upload_to="leases/")

    def __str__(self):
        return f"Bail {self.tenant_name} – {self.property.address}"
