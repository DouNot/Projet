from django.urls import path
from . import views

urlpatterns = [
    # Biens
    path("properties/", views.PropertyList.as_view(),          name="property_list"),
    path("properties/add/", views.PropertyCreate.as_view(),    name="property_add"),
    path("properties/<int:pk>/", views.PropertyDetail.as_view(), name="property_detail"),
    path("properties/<int:pk>/edit/", views.PropertyUpdate.as_view(), name="property_edit"),
    path("properties/<int:pk>/delete/", views.PropertyDelete.as_view(), name="property_delete"),

    # Prêts & baux (l’ID du bien figure dans l’URL)
    path("properties/<int:property_pk>/loans/add/",  views.LoanCreate.as_view(),  name="loan_add"),
    path("loans/<int:pk>/edit/",   views.LoanUpdate.as_view(),   name="loan_edit"),
    path("loans/<int:pk>/delete/", views.LoanDelete.as_view(),   name="loan_delete"),
    # Baux
    path("properties/<int:property_pk>/leases/add/", views.LeaseCreate.as_view(), name="lease_add"),
    path("leases/<int:pk>/edit/",  views.LeaseUpdate.as_view(),  name="lease_edit"),
    path("leases/<int:pk>/delete/",views.LeaseDelete.as_view(),  name="lease_delete"),

]
