# Generated by Django 4.0.2 on 2022-03-23 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_alter_addbussi_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='addbussi',
            name='imagelink',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
