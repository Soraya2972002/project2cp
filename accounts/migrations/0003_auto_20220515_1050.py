# Generated by Django 3.2.13 on 2022-05-15 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='en_cours_livraison',
            field=models.CharField(default='', max_length=8000, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='livres',
            field=models.CharField(default='', max_length=800000000, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='wilaya',
            field=models.CharField(choices=[('Adrar', 'Adrar'), ('Chlef', 'Chlef'), ('Laghouat', 'Laghouat'), ('Oum El Bouaghi', 'Oum El Bouaghi'), ('Batna', 'Batna'), ('Béjaïa', 'Béjaïa'), ('Biskra', 'Biskra'), ('Bechar', 'Bechar'), ('Blida', 'Blida'), ('Bouira', 'Bouira'), ('Tamanrasset', 'Tamanrasset'), ('Tbessa', 'Tbessa'), ('Tlemcen', 'Tlemcen'), ('Tiaret', 'Tiaret'), ('Tizi Ouzou', 'Tizi Ouzou'), ('Alger', 'Alger'), ('Djelfa', 'Djelfa'), ('Jijel', 'Jijel'), ('Sétif', 'Sétif'), ('Saefda', 'Saefda'), ('Skikda', 'Skikda'), ('Sidi Bel Abbes', 'Sidi Bel Abbes'), ('Annaba', 'Annaba'), ('Guelma', 'Guelma'), ('Constantine', 'Constantine'), ('Medea', 'Medea'), ('Mostaganem', 'Mostaganem'), ("M'Sila", "M'Sila"), ('Mascara', 'Mascara'), ('Ouargla', 'Ouargla'), ('Oran', 'Oran'), ('El Bayadh', 'El Bayadh'), ('Illizi', 'Illizi'), ('Bordj Bou Arreridj', 'Bordj Bou Arreridj'), ('Boumerdes', 'Boumerdes'), ('El Tarf', 'El Tarf'), ('Tindouf', 'Tindouf'), ('Tissemsilt', 'Tissemsilt'), ('El Oued', 'El Oued'), ('Khenchela', 'Khenchela'), ('Souk Ahras', 'Souk Ahras'), ('Tipaza', 'Tipaza'), ('Mila', 'Mila'), ('Ain Defla', 'Ain Defla'), ('Naama', 'Naama'), ('Ain Temouchent', 'Ain Temouchent'), ('Ghardaïa', 'Ghardaïa'), ('Relizane', 'Relizane'), ('', '')], default='', max_length=100, null=True),
        ),
    ]
