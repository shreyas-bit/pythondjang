# Generated by Django 5.0.6 on 2024-06-28 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('content', models.TextField()),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]
