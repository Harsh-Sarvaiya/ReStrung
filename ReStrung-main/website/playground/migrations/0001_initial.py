# Generated by Django 4.2.7 on 2023-11-27 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stringers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=100)),
                ('streetAddress', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=2)),
                ('postalCode', models.CharField(max_length=6)),
                ('phoneNumber', models.CharField(max_length=10)),
                ('emailAddress', models.EmailField(max_length=254)),
                ('rating', models.IntegerField(choices=[(0, 'Zero'), (1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')])),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('numberOfLifeTimeCustomers', models.CharField(max_length=10)),
                ('dateJoined', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
