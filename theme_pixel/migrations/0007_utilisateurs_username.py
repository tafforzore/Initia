# Generated by Django 4.2.7 on 2023-11-20 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme_pixel', '0006_produit_couverture_principale_alter_produit_photos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateurs',
            name='username',
            field=models.CharField(default='unknow', max_length=10000),
        ),
    ]
