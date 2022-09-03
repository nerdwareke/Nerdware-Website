# Generated by Django 4.0.4 on 2022-07-05 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('where_did_you_find_us', models.CharField(max_length=100)),
                ('applyfor', models.CharField(max_length=100)),
                ('website_url', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('where_did_you_find_us', models.CharField(max_length=100)),
                ('budget', models.CharField(max_length=100)),
                ('website_url', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]