# Generated by Django 4.2.1 on 2023-05-23 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('magazynier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Przepisy',
            fields=[
                ('przepis_id', models.AutoField(primary_key=True, serialize=False)),
                ('nazwa_przepisu', models.CharField(default='', max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skladniki',
            fields=[
                ('krotka_id', models.AutoField(primary_key=True, serialize=False)),
                ('ilosc_produktu', models.FloatField(default=0.0)),
                ('produkt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='magazynier.produkty')),
                ('przepis', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='piekarz.przepisy')),
            ],
            options={
                'unique_together': {('przepis', 'produkt')},
            },
        ),
    ]
