# Generated by Django 5.0.4 on 2024-05-25 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_product_desc_alter_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pdf',
            field=models.FileField(default=None, max_length=1000, null=True, upload_to=''),
        ),
    ]
