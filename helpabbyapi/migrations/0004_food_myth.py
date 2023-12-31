# Generated by Django 3.2.12 on 2023-12-28 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('helpabbyapi', '0003_delete_myths'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodName', models.CharField(max_length=1000)),
                ('calories', models.IntegerField()),
                ('carbs', models.DecimalField(decimal_places=1, max_digits=1000)),
                ('protein', models.DecimalField(decimal_places=1, max_digits=1000)),
                ('fat', models.DecimalField(decimal_places=1, max_digits=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Myth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mythDesc', models.CharField(max_length=1000)),
                ('factDesc', models.CharField(max_length=1000)),
                ('source', models.CharField(max_length=100)),
            ],
        ),
    ]