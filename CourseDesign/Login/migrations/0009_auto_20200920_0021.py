# Generated by Django 3.1.1 on 2020-09-19 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0008_auto_20200920_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.user'),
        ),
    ]
