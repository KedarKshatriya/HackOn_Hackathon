# Generated by Django 2.2.7 on 2020-04-18 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidManager', '0007_auto_20200417_2217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opac', models.CharField(default=0.05, max_length=100)),
            ],
        ),
    ]
