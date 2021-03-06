# Generated by Django 3.2.4 on 2021-06-23 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20210624_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlescopeship',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.article'),
        ),
        migrations.AlterField(
            model_name='articlescopeship',
            name='scope',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scopeships', to='articles.scope'),
        ),
    ]
