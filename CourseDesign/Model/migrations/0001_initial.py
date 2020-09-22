# Generated by Django 3.1.1 on 2020-09-21 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('description', models.CharField(max_length=250)),
                ('owner', models.CharField(max_length=15)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.CharField(max_length=18, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=18)),
                ('name', models.CharField(max_length=20)),
                ('isMale', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=18, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=18)),
                ('name', models.CharField(max_length=20)),
                ('birthday', models.DateField()),
                ('isMale', models.BooleanField(default=True)),
                ('college', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('QQ', models.CharField(max_length=20)),
                ('tel', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.CharField(max_length=18)),
                ('seller', models.CharField(max_length=18)),
                ('status', models.IntegerField()),
                ('comment', models.CharField(max_length=200)),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Model.commodity')),
            ],
        ),
    ]