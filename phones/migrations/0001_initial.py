# Generated by Django 4.2.3 on 2023-07-30 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('image', models.URLField()),
                ('price', models.FloatField()),
                ('release_date', models.DateField()),
                ('lte_exists', models.BooleanField()),
            ],
        ),
    ]
