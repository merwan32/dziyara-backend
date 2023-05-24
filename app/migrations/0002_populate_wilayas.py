from django.db import migrations

def populate_wilayas(apps, schema_editor):
    Wilaya = apps.get_model('app', 'Wilaya')

  
    wilayas = [
        {'wilaya_id': 1, 'name': 'Adrar'},
        {'wilaya_id': 2, 'name': 'Chlef'},
        {'wilaya_id': 3, 'name': 'Laghouat'},
        {'wilaya_id': 4, 'name': 'Oum El Bouaghi'},
        {'wilaya_id': 5, 'name': 'Batna'},
        {'wilaya_id': 6, 'name': 'Béjaïa'},
        {'wilaya_id': 7, 'name': 'Biskra'},
        {'wilaya_id': 8, 'name': 'Béchar'},
        {'wilaya_id': 9, 'name': 'Blida'},
        {'wilaya_id': 10, 'name': 'Bouira'},
        {'wilaya_id': 11, 'name': 'Tamanrasset'},
        {'wilaya_id': 12, 'name': 'Tébessa'},
        {'wilaya_id': 13, 'name': 'Tlemcen'},
        {'wilaya_id': 14, 'name': 'Tiaret'},
        {'wilaya_id': 15, 'name': 'Tizi Ouzou'},
        {'wilaya_id': 16, 'name': 'Alger'},
        {'wilaya_id': 17, 'name': 'Djelfa'},
        {'wilaya_id': 18, 'name': 'Jijel'},
        {'wilaya_id': 19, 'name': 'Sétif'},
        {'wilaya_id': 20, 'name': 'Saïda'},
        {'wilaya_id': 21, 'name': 'Skikda'},
        {'wilaya_id': 22, 'name': 'Sidi Bel Abbès'},
        {'wilaya_id': 23, 'name': 'Annaba'},
        {'wilaya_id': 24, 'name': 'Guelma'},
        {'wilaya_id': 25, 'name': 'Constantine'},
        {'wilaya_id': 26, 'name': 'Médéa'},
        {'wilaya_id': 27, 'name': 'Mostaganem'},
        {'wilaya_id': 28, 'name': 'M\'Sila'},
        {'wilaya_id': 29, 'name': 'Mascara'},
        {'wilaya_id': 30, 'name': 'Ouargla'},
        {'wilaya_id': 31, 'name': 'Oran'},
        {'wilaya_id': 32, 'name': 'El Bayadh'},
        {'wilaya_id': 33, 'name': 'Illizi'},
        {'wilaya_id': 34, 'name': 'Bordj Bou Arréridj'},
        {'wilaya_id': 35, 'name': 'Boumerdès'},
        {'wilaya_id': 36, 'name': 'El Tarf'},
        {'wilaya_id': 37, 'name': 'Tindouf'},
        {'wilaya_id': 38, 'name': 'Tissemsilt'},
        {'wilaya_id': 39, 'name': 'El Oued'},
        {'wilaya_id': 40, 'name': 'Khenchela'},
        {'wilaya_id': 41, 'name': 'Souk Ahras'},
        {'wilaya_id': 42, 'name': 'Tipaza'},
        {'wilaya_id': 43, 'name': 'Mila'},
        {'wilaya_id': 44, 'name': 'Aïn Defla'},
        {'wilaya_id': 45, 'name': 'Naâma'},
        {'wilaya_id': 46, 'name': 'Aïn Témouchent'},
        {'wilaya_id': 47, 'name': 'Ghardaïa'},
        {'wilaya_id': 48, 'name': 'Relizane'},
    ]

 
    for wilaya_data in wilayas:
        wilaya = Wilaya(**wilaya_data)
        wilaya.save()

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),  
    ]

    operations = [
        migrations.RunPython(populate_wilayas),
    ]
