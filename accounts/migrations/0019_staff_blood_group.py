# Generated by Django 3.2.3 on 2021-07-14 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20210714_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='blood_group',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
