# Generated by Django 3.1.2 on 2020-10-14 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20201013_2331'),
    ]

    operations = [
        migrations.CreateModel(
            name='campusAmbassador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user_id', models.PositiveIntegerField()),
                ('event_id', models.PositiveIntegerField()),
                ('previous_experience', models.TextField()),
                ('approval', models.BooleanField(default=False)),
            ],
        ),
    ]
