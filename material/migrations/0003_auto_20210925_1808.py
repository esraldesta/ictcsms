# Generated by Django 3.1.6 on 2021-09-25 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0002_alter_material_lasting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='material',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='material',
            name='lasting',
            field=models.IntegerField(choices=[(1, 'new'), (2, 'to be fixed'), (3, 'wasted')], default=1),
        ),
        migrations.AlterField(
            model_name='material',
            name='status',
            field=models.IntegerField(choices=[(1, 'new'), (2, 'to be fixed'), (3, 'wasted')], default=1),
        ),
    ]