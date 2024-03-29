# Generated by Django 4.1.12 on 2023-11-07 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theme_pixel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=1000000)),
                ('prenom', models.CharField(default=None, max_length=1000000)),
                ('numeros', models.IntegerField()),
                ('pays', models.CharField(max_length=1000000)),
            ],
        ),
        migrations.AlterField(
            model_name='investissement',
            name='email_personne',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theme_pixel.utilisateurs'),
        ),
        migrations.DeleteModel(
            name='Utilisateur',
        ),
    ]
