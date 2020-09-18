# Generated by Django 3.0 on 2020-09-17 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_manageraccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('ID', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=15)),
                ('isManager', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='ManagerAccount',
        ),
        migrations.DeleteModel(
            name='UserAccount',
        ),
    ]