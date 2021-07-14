# Generated by Django 3.2.3 on 2021-07-14 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20210714_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='doj',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='empid',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='house',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='state',
            field=models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=20),
        ),
        migrations.AddField(
            model_name='staff',
            name='street',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='street2',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
