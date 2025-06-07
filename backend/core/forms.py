from django import forms
from .models import Property, Loan, Lease

DATE_WIDGET = forms.DateInput(attrs={"type": "date"})

class PropertyForm(forms.ModelForm):
    class Meta:
        model  = Property
        fields = ["address", "surface", "purchase_price", "photo"]


class LoanForm(forms.ModelForm):
    start_date = forms.DateField(widget=DATE_WIDGET)

    class Meta:
        model   = Loan
        exclude = ["property"]         # champ masqué


class LeaseForm(forms.ModelForm):
    start_date = forms.DateField(widget=DATE_WIDGET)
    end_date   = forms.DateField(widget=DATE_WIDGET)
    lease_pdf  = forms.FileField(required=False)

    class Meta:
        model   = Lease
        exclude = ["property"]         # champ masqué
