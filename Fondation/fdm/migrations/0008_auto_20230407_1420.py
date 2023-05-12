# Generated by Django 3.2.18 on 2023-04-07 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fdm', '0007_alter_article_texte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=models.ImageField(blank=True, default='photo/nature.jpg', null=True, upload_to='photo/'),
        ),
        migrations.AlterField(
            model_name='organigramme',
            name='mission',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='organigramme',
            name='titre',
            field=models.CharField(default='membre', max_length=70),
        ),
    ]