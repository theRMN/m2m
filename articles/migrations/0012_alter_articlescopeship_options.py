# Generated by Django 3.2.4 on 2021-08-16 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_alter_articlescopeship_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlescopeship',
            options={'ordering': ['-is_main'], 'verbose_name': 'Тематика статьи', 'verbose_name_plural': 'Тематики статьи'},
        ),
    ]
