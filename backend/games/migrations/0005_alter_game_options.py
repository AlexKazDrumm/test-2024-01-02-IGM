# Generated by Django 4.2.2 on 2024-12-01 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_game_license_type_game_platform_game_publisher'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ['id']},
        ),
    ]
