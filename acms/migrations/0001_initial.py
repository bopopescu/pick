# Generated by Django 3.0.6 on 2020-06-03 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_line', models.CharField(max_length=500)),
                ('second_line', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=500)),
                ('state', models.CharField(blank=True, choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh ', 'Arunachal Pradesh '), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir ', 'Jammu and Kashmir '), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Lakshadweep', 'Lakshadweep'), ('National Capital Territory of Delhi', 'National Capital Territory of Delhi'), ('Puducherry', 'Puducherry')], max_length=255, null=True)),
                ('pin_code', models.CharField(max_length=10)),
                ('country_code', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('longitude', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('phone', models.IntegerField()),
                ('onboarded_at', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acms.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('store_name', models.CharField(max_length=256)),
                ('google_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('store_type', models.CharField(max_length=500)),
                ('gstin', models.CharField(max_length=20)),
                ('onboarded_at', models.DateTimeField(auto_now=True)),
                ('no_of_lockers', models.IntegerField()),
                ('no_of_cctv', models.IntegerField()),
                ('ease_of_transprtation', models.BooleanField(default=False)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acms.Locations')),
                ('partner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acms.Partner')),
                ('store_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acms.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('phone', models.IntegerField()),
                ('is_phone_verified', models.BooleanField(default=False)),
                ('hash', models.TextField(max_length=256)),
                ('salt', models.TextField(max_length=32)),
                ('onboarded_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StoreTimings',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('open_time', models.DateTimeField()),
                ('close_time', models.DateTimeField()),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acms.Store')),
            ],
        ),
    ]
