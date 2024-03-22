# Generated by Django 3.2 on 2024-03-07 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('convertor', '0002_receiptfile_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDFFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='pdf_files/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConvertedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_file', models.FileField(upload_to='csv_files/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('pdf_file', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='convertor.pdffile')),
            ],
        ),
    ]