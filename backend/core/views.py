from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView,
)

from .models import Property, Loan, Lease, LegalEntity
from .forms  import PropertyForm, LoanForm, LeaseForm


# ──────────────────────────────────────────────
#  Helper : garantir qu’une LegalEntity existe
# ──────────────────────────────────────────────
def get_or_create_entity_for(user):
    entity = user.entities.first()
    if entity is None:
        entity = LegalEntity.objects.create(
            user=user,
            name=user.get_full_name() or user.username,
            type=LegalEntity.PERSON,
        )
    return entity


# ──────────────────────────────────────────────
#  Property (CRUD)
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


class PropertyDetail(LoginRequiredMixin, DetailView):
    model = Property
    template_name = "core/property_detail.html"
    context_object_name = "property"

    def get_queryset(self):
        return get_or_create_entity_for(self.request.user).properties.all()


class PropertyUpdate(LoginRequiredMixin, UpdateView):
    model = Property
    form_class = PropertyForm
    template_name = "core/property_form.html"
    success_url = reverse_lazy("property_list")

    def get_queryset(self):
        return get_or_create_entity_for(self.request.user).properties.all()


class PropertyDelete(LoginRequiredMixin, DeleteView):
    model = Property
    template_name = "core/property_confirm_delete.html"
    success_url = reverse_lazy("property_list")

    def get_queryset(self):
        return get_or_create_entity_for(self.request.user).properties.all()


# ──────────────────────────────────────────────
#  Loan
# ──────────────────────────────────────────────
class LoanCreate(LoginRequiredMixin, CreateView):
    model = Loan
    form_class = LoanForm
    template_name = "core/loan_form.html"
    success_url = reverse_lazy("property_list")

    # on récupère le bien depuis l’URL
    def dispatch(self, request, *args, **kwargs):
        self.property = get_or_create_entity_for(request.user).properties.get(
            pk=kwargs["property_pk"]
        )
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.property = self.property
        return super().form_valid(form)


class LoanUpdate(LoginRequiredMixin, UpdateView):
    model = Loan
    form_class = LoanForm
    template_name = "core/loan_form.html"
    success_url = reverse_lazy("property_list")

    def get_queryset(self):
        entity = get_or_create_entity_for(self.request.user)
        return Loan.objects.filter(property__entity=entity)   # ← FIX


class LoanDelete(LoginRequiredMixin, DeleteView):
    model = Loan
    template_name = "core/loan_confirm_delete.html"
    success_url = reverse_lazy("property_list")

    def get_queryset(self):
        entity = get_or_create_entity_for(self.request.user)
        return Loan.objects.filter(property__entity=entity)   # ← FIX


# ──────────────────────────────────────────────
#  Lease
# ──────────────────────────────────────────────
class LeaseCreate(LoginRequiredMixin, CreateView):
    model = Lease
    form_class = LeaseForm
    template_name = "core/lease_form.html"
    success_url = reverse_lazy("property_list")

    def dispatch(self, request, *args, **kwargs):
        self.property = get_or_create_entity_for(request.user).properties.get(
            pk=kwargs["property_pk"]
        )
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.property = self.property
        return super().form_valid(form)


class LeaseUpdate(LoginRequiredMixin, UpdateView):
    model = Lease
    form_class = LeaseForm
    template_name = "core/lease_form.html"
    success_url = reverse_lazy("property_list")

    def get_queryset(self):
        entity = get_or_create_entity_for(self.request.user)
        return Lease.objects.filter(property__entity=entity)  # ← FIX


class LeaseDelete(LoginRequiredMixin, DeleteView):
    model = Lease
    template_name = "core/lease_confirm_delete.html"
    success_url = reverse_lazy("property_list")

    def get_queryset(self):
        entity = get_or_create_entity_for(self.request.user)
        return Lease.objects.filter(property__entity=entity)  # ← FIX
