# Generated by Django 3.1.2 on 2020-10-25 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='id_ticket',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='events.fulluser'),
            preserve_default=False,
        ),
    ]
