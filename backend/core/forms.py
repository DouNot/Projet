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
        model  = Loan
        fields = ["property", "bank", "amount", "rate",
                  "duration_months", "start_date"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["property"].queryset = user.entities.first().properties.all()

class LeaseForm(forms.ModelForm):
    start_date = forms.DateField(widget=DATE_WIDGET)
    end_date   = forms.DateField(widget=DATE_WIDGET)
    lease_pdf  = forms.FileField(required=False)      

    class Meta:
        model  = Lease
        fields = ["property", "tenant_name", "rent",
                  "start_date", "end_date", "lease_pdf"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["property"].queryset = user.entities.first().properties.all()
