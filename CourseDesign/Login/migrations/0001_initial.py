# Generated by Django 3.0 on 2020-09-19 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('ID', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=15)),
                ('isManager', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('ID', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('description', models.CharField(max_length=250)),
                ('owner', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Login.Account')),
                ('name', models.CharField(max_length=20)),
                ('isMale', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Login.Account')),
                ('name', models.CharField(max_length=20)),
                ('birthday', models.DateField()),
                ('isMale', models.BooleanField(default=True)),
                ('college', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]