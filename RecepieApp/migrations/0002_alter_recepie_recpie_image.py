# Generated by Django 4.2.3 on 2023-07-11 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecepieApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recepie',
            name='recpie_image',
            field=models.ImageField(upload_to='recepie'),
        ),
    ]