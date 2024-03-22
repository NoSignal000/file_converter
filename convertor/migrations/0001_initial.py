# Generated by Django 3.2 on 2024-01-17 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReceiptFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='receipts/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('converted_csv', models.FileField(blank=True, null=True, upload_to='receipts/converted_csv/')),
            ],
        ),
    ]