# Generated by Django 3.2.2 on 2021-06-14 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_customuser_access_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
