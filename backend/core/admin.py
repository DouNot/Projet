from django.contrib import admin
from .models import LegalEntity, Property, Loan, Lease

admin.site.register(LegalEntity)
admin.site.register(Property)
admin.site.register(Loan)
admin.site.register(Lease)
