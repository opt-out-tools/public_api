# Generated by Django 2.2.5 on 2019-09-17 15:13

import django.contrib.postgres.fields
import django.db.models.deletion
import opt_out.public_api.api.enums
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Predictions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texts',
                 django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urls', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), size=None)),
                ('self_submission', models.BooleanField()),
                ('is_part_of_larger_attack', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='SubmissionDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identify', models.CharField(max_length=100)),
                ('age', models.PositiveSmallIntegerField()),
                ('job', models.CharField(max_length=160)),
                ('perpetrator', models.CharField(
                    choices=[('person you know', opt_out.public_api.api.enums.PerpetratorType('person you know')), (
                    'multiple persons you know',
                    opt_out.public_api.api.enums.PerpetratorType('multiple persons you know')),
                             ('single stranger', opt_out.public_api.api.enums.PerpetratorType('single stranger')), (
                             'multiple strangers', opt_out.public_api.api.enums.PerpetratorType('multiple strangers'))],
                    max_length=40)),
                ('interaction', models.CharField(choices=[('post daily to my friends',
                                                           opt_out.public_api.api.enums.InteractionType(
                                                               'post daily to my friends')), ('post daily for work',
                                                                                              opt_out.public_api.api.enums.InteractionType(
                                                                                                  'post daily for work')),
                                                          ('post rarely for my friends',
                                                           opt_out.public_api.api.enums.InteractionType(
                                                               'post rarely for my friends')), ('post rarely for work',
                                                                                                opt_out.public_api.api.enums.InteractionType(
                                                                                                    'post rarely for work')),
                                                          ('never post',
                                                           opt_out.public_api.api.enums.InteractionType('never post'))],
                                                 max_length=40)),
                ('reaction_type', models.CharField(choices=[('my behaviour has not changed',
                                                             opt_out.public_api.api.enums.ReactionType(
                                                                 'my behaviour has not changed')), (
                                                            'i avoid controversial topics and self-censor',
                                                            opt_out.public_api.api.enums.ReactionType(
                                                                'i avoid controversial topics and self-censor')), (
                                                            'i took a break from platform',
                                                            opt_out.public_api.api.enums.ReactionType(
                                                                'i took a break from platform')), (
                                                            'i no longer post pictures of myself',
                                                            opt_out.public_api.api.enums.ReactionType(
                                                                'i no longer post pictures of myself')), (
                                                            'i no longer use platform',
                                                            opt_out.public_api.api.enums.ReactionType(
                                                                'i no longer use platform'))], max_length=40)),
                ('experienced',
                 django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=300), size=None)),
                ('feeling', models.CharField(max_length=300)),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Submission')),
            ],
        ),
    ]
