from django.urls import path
from . import views

urlpatterns = [
    path("properties/", views.PropertyList.as_view(), name="property_list"),
    path("properties/add/", views.PropertyCreate.as_view(), name="property_add"),
    path("properties/<int:pk>/", views.PropertyDetail.as_view(), name="property_detail"),
    path("properties/<int:pk>/edit/", views.PropertyUpdate.as_view(), name="property_edit"),      # ← NEW
    path("properties/<int:pk>/delete/", views.PropertyDelete.as_view(), name="property_delete"),  # ← NEW
    path("loans/add/", views.LoanCreate.as_view(), name="loan_add"),
    path("leases/add/", views.LeaseCreate.as_view(), name="lease_add"),
]
