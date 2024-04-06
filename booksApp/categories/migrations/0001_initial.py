# Generated by Django 5.0.3 on 2024-04-05 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=120, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]