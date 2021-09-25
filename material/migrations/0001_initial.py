# Generated by Django 3.2.7 on 2021-09-25 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('serial_no', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('pincode', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('amount', models.IntegerField()),
                ('status', models.CharField(choices=[(1, 'new'), (2, 'to be fixed'), (3, 'wasted')], default=1, max_length=50)),
                ('lasting', models.CharField(choices=[(1, 'new'), (2, 'to be fixed'), (3, 'wasted')], default=1, max_length=50)),
                ('shelf_no', models.IntegerField(blank=True, null=True)),
                ('column_row', models.IntegerField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='material.category')),
            ],
        ),
    ]
