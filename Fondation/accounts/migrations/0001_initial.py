# Generated by Django 3.2.18 on 2023-04-21 19:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField()),
                ('phone', models.IntegerField()),
                ('photo', models.ImageField(blank=True, default='photo/nature.jpg', null=True, upload_to='photo/')),
                ('genre', models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin')], default='M', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]