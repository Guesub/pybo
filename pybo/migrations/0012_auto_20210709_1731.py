# Generated by Django 3.2.2 on 2021-07-09 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0011_citycode'),
    ]

    operations = [
        migrations.AddField(
            model_name='citycode',
            name='provins',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='citycode',
            name='code',
            field=models.IntegerField(),
        ),
    ]