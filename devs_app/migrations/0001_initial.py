# Generated by Django 3.1.2 on 2021-01-12 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UREG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=100)),
                ('phonenumber', models.BigIntegerField()),
                ('city', models.CharField(max_length=20)),
                ('zip', models.IntegerField(max_length=6)),
            ],
        ),
    ]
