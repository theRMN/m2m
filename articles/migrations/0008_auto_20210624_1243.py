# Generated by Django 3.2.4 on 2021-06-24 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20210624_0601'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlescopeship',
            options={'verbose_name': 'Тематика статьи', 'verbose_name_plural': 'Тематики статьи'},
        ),
        migrations.AlterField(
            model_name='articlescopeship',
            name='scope',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='scopeships', to='articles.scope', verbose_name='Разделы'),
        ),
    ]