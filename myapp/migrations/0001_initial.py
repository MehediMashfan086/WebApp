# Generated by Django 3.2.7 on 2021-10-04 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_id', models.CharField(max_length=20)),
                ('e_name', models.CharField(max_length=100)),
                ('e_email', models.EmailField(max_length=254)),
                ('e_contact', models.CharField(max_length=30)),
            ],
        ),
    ]