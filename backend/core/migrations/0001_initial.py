# Generated by Django 4.2.22 on 2025-06-07 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LegalEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('type', models.CharField(choices=[('PERSON', 'Personne physique'), ('SCI', 'SCI')], default='PERSON', max_length=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entities', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('surface', models.DecimalField(decimal_places=2, max_digits=7)),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='property_photos/')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='core.legalentity')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(max_length=120)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('duration_months', models.PositiveIntegerField()),
                ('start_date', models.DateField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans', to='core.property')),
            ],
        ),
        migrations.CreateModel(
            name='Lease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_name', models.CharField(max_length=120)),
                ('rent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('lease_pdf', models.FileField(upload_to='leases/')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leases', to='core.property')),
            ],
        ),
    ]
