# Generated by Django 4.2.2 on 2023-07-01 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_pdf_pdf_var'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdf_var',
            name='document_title',
            field=models.CharField(default=12, max_length=10),
            preserve_default=False,
        ),
    ]