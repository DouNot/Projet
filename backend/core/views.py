# core/views.py  – imports regroupés
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView,
)

from .models import Property, Loan, Lease, LegalEntity
from .forms  import PropertyForm, LoanForm, LeaseForm


# ──────────────────────────────────────────────
#  Helpers
# ──────────────────────────────────────────────
def get_or_create_entity_for(user):
    """
    Renvoie la première LegalEntity de l'utilisateur, ou la crée
    s'il n'en possède pas encore (ex. comptes créés avant le signal).
    """
    entity = user.entities.first()
    if entity is None:
        entity = LegalEntity.objects.create(
            user=user,
            name=user.get_full_name() or user.username,
            type=LegalEntity.PERSON,
        )
    return entity


# ──────────────────────────────────────────────
#  Property
# ──────────────────────────────────────────────
class PropertyList(LoginRequiredMixin, ListView):
    template_name = "core/property_list.html"
    context_object_name = "properties"

    def get_queryset(self):
        return get_or_create_entity_for(self.request.user).properties.all()


class PropertyCreate(LoginRequiredMixin, CreateView):
    model = Property
    form_class = PropertyForm
    template_name = "core/property_form.html"
    success_url = reverse_lazy("property_list")

    def form_valid(self, form):
        form.instance.entity = get_or_create_entity_for(self.request.user)
        return super().form_valid(form)


# ──────────────────────────────────────────────
#  Loan
# ──────────────────────────────────────────────
class LoanCreate(LoginRequiredMixin, CreateView):
    model = Loan
    form_class = LoanForm
    template_name = "core/loan_form.html"
    success_url = reverse_lazy("property_list")

    def get_form_kwargs(self):
        # s'assure que l'entité existe avant de filtrer la queryset
        get_or_create_entity_for(self.request.user)
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


# ──────────────────────────────────────────────
#  Lease
# ──────────────────────────────────────────────
class LeaseCreate(LoginRequiredMixin, CreateView):
    model = Lease
    form_class = LeaseForm
    template_name = "core/lease_form.html"
    success_url = reverse_lazy("property_list")

    def get_form_kwargs(self):
        get_or_create_entity_for(self.request.user)
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

# ──────────────────────────────────────────────
#  Property : vue détail
# ──────────────────────────────────────────────
class PropertyDetail(LoginRequiredMixin, DetailView):
    model = Property
    template_name = "core/property_detail.html"
    context_object_name = "property"

    def get_queryset(self):
        # sécurité : l’utilisateur ne peut voir que SES propres biens
        return self.request.user.entities.first().properties.all()


# ──────────────────────────────────────────────
#  Property : Property Update
# ──────────────────────────────────────────────

class PropertyUpdate(LoginRequiredMixin, UpdateView):
    model = Property
    form_class = PropertyForm
    template_name = "core/property_form.html"       # on réutilise le même
    success_url = reverse_lazy("property_list")

    def get_queryset(self):
        return self.request.user.entities.first().properties.all()

# ──────────────────────────────────────────────
#  Property : Property Delete
# ──────────────────────────────────────────────
class PropertyDelete(LoginRequiredMixin, DeleteView):
    model = Property
    template_name = "core/property_confirm_delete.html"
    success_url = reverse_lazy("property_list")

    def get_queryset(self):
        return self.request.user.entities.first().properties.all()