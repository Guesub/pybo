# Generated by Django 3.2.2 on 2021-06-14 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_alter_customuser_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='access_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
