# Generated by Django 3.1.2 on 2020-10-09 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('des', models.TextField()),
                ('price', models.IntegerField()),
                ('start_date', models.DateField()),
                ('duration_days', models.PositiveIntegerField()),
            ],
        ),
    ]
