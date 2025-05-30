# Generated by Django 4.2.11 on 2024-10-20 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('date', models.DateField()),
                ('location', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.TextField(max_length=15)),
                ('registeration_date', models.DateTimeField(auto_now_add=True)),
                ('events', models.ManyToManyField(related_name='participants', to='events.event')),
            ],
        ),
    ]
