# Generated by Django 3.2.4 on 2021-06-23 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_tags_scopes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='scope',
        ),
        migrations.AddField(
            model_name='scopes',
            name='tag',
            field=models.ManyToManyField(related_name='scope', to='articles.Article'),
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]