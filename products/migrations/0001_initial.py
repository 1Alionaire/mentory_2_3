# Generated by Django 5.0 on 2023-12-16 09:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
                ('category_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('dateAdded', models.DateTimeField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.productcategory')),
            ],
        ),
    ]
