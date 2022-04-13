# Generated by Django 2.1.5 on 2022-04-05 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nometpren', models.CharField(max_length=120)),
                ('telephone', models.DecimalField(decimal_places=0, max_digits=10, unique=True)),
                ('telephone1', models.DecimalField(decimal_places=0, max_digits=10, unique=True)),
                ('wilaya', models.CharField(choices=[('Wilaya', 'Adrar'), ('Wilaya', 'Chlef'), ('Wilaya', 'Laghouat'), ('Wilaya', 'Oum El Bouaghi'), ('Wilaya', 'Batna'), ('Wilaya', 'Béjaïa'), ('Wilaya', 'Biskra'), ('Wilaya', 'Bechar'), ('Wilaya', 'Blida'), ('Wilaya', 'Bouira'), ('Wilaya', 'Tamanrasset'), ('Wilaya', 'Tbessa'), ('Wilaya', 'Tlemcen'), ('Wilaya', 'Tiaret'), ('Wilaya', 'Tizi Ouzou'), ('Wilaya', 'Alger'), ('Wilaya', 'Djelfa'), ('Wilaya', 'Jijel'), ('Wilaya', 'Sétif'), ('Wilaya', 'Saefda'), ('Wilaya', 'Skikda'), ('Wilaya', 'Sidi Bel Abbes'), ('Wilaya', 'Annaba'), ('Wilaya', 'Guelma'), ('Wilaya', 'Constantine'), ('Wilaya', 'Medea'), ('Wilaya', 'Mostaganem'), ('Wilaya', "M'Sila"), ('Wilaya', 'Mascara'), ('Wilaya', 'Ouargla'), ('Wilaya', 'Oran'), ('Wilaya', 'El Bayadh'), ('Wilaya', 'Illizi'), ('Wilaya', 'Bordj Bou Arreridj'), ('Wilaya', 'Boumerdes'), ('Wilaya', 'El Tarf'), ('Wilaya', 'Tindouf'), ('Wilaya', 'Tissemsilt'), ('Wilaya', 'El Oued'), ('Wilaya', 'Khenchela'), ('Wilaya', 'Souk Ahras'), ('Wilaya', 'Tipaza'), ('Wilaya', 'Mila'), ('Wilaya', 'Ain Defla'), ('Wilaya', 'Naama'), ('Wilaya', 'Ain Temouchent'), ('Wilaya', 'Ghardaïa'), ('Wilaya', 'Relizane')], max_length=10)),
                ('commune', models.CharField(max_length=10)),
                ('adresse', models.CharField(max_length=200)),
                ('montant', models.DecimalField(decimal_places=5, max_digits=10)),
                ('numerocommande', models.DecimalField(decimal_places=0, max_digits=10)),
                ('poids', models.DecimalField(decimal_places=0, max_digits=4)),
                ('remarque', models.TextField(max_length=100)),
                ('produit', models.TextField(null=True)),
                ('typeenvoi', models.CharField(choices=[('V', 'livraison'), ('EC', 'échange'), ('PU', 'Pick up'), ('RE', 'recouvrement'), ('V', '---------')], default='V', max_length=100)),
                ('typeprestation', models.CharField(choices=[('V', '---------'), ('AD', 'à domicile'), ('SD', 'Stop desk')], default='V', max_length=100)),
            ],
        ),
    ]
