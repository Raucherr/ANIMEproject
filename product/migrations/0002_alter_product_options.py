# Generated by Django 4.0.3 on 2022-03-30 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id']},
        ),
    ]