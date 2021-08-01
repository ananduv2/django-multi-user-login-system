# Generated by Django 3.2.5 on 2021-08-01 07:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0063_auto_20210801_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprojectdata',
            name='batch',
        ),
        migrations.AddField(
            model_name='studentprojectdata',
            name='certificate',
            field=models.FileField(blank=True, default=None, null=True, upload_to='certiicates/'),
        ),
        migrations.AddField(
            model_name='studentprojectdata',
            name='verified_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='query',
            name='datetime',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 8, 1, 13, 18, 4, 35244), null=True),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Inactive', max_length=20)),
                ('batch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.batch')),
            ],
        ),
        migrations.AddField(
            model_name='studentprojectdata',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='accounts.project'),
        ),
    ]
