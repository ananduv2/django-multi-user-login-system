# Generated by Django 3.2.3 on 2021-07-12 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210713_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='status',
            field=models.CharField(choices=[('Yet to start', 'Yet to start'), ('Yet to start', 'Ongoing'), ('Yet to start', 'Completed')], default='Yet to start', max_length=100),
        ),
    ]
