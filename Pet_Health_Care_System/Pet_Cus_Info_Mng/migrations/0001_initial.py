# Generated by Django 5.0.10 on 2025-01-12 09:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('gender', models.CharField(choices=[('Male', 'Nam'), ('Female', 'Nữ')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Đực'), ('Female', 'Cái')], max_length=10)),
                ('date_of_birth', models.DateField()),
                ('age', models.IntegerField()),
                ('health_status', models.CharField(choices=[('Healthy', 'Khỏe mạnh'), ('Sick', 'Đang bệnh'), ('Recovering', 'Đang hồi phục')], max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pet_Cus_Info_Mng.customer')),
            ],
        ),
    ]
