# Generated by Django 3.2.4 on 2021-06-24 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_articlescopeship_scope'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlescopeship',
            name='article',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='scopeships', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='articlescopeship',
            name='scope',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='scopeships', to='articles.scope'),
        ),
    ]
