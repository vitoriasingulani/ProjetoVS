# Generated by Django 5.0.3 on 2024-11-27 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuarios', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=100)),
                ('idade', models.IntegerField()),
            ],
        ),
    ]