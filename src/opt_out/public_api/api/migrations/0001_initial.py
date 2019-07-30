# Generated by Django 2.2.3 on 2019-07-30 14:02

import django.contrib.postgres.fields
from django.db import migrations, models
import src.opt_out.public_api.api.enums


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FurtherDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identify', models.CharField(choices=[(src.opt_out.public_api.api.enums.Identify('female'), 'female'), (src.opt_out.public_api.api.enums.Identify('transgender female'), 'transgender female')], max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('submission_id', models.AutoField(primary_key=True, serialize=False)),
                ('urls', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), size=None)),
                ('self_submission', models.BooleanField()),
                ('is_part_of_larger_attack', models.BooleanField()),
            ],
        ),
    ]
