# Generated by Django 3.2.18 on 2023-03-22 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=70)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Categorie',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emailto', models.CharField(max_length=70)),
                ('EmailFrom', models.CharField(max_length=200)),
                ('subjectText', models.CharField(max_length=70)),
                ('bodyText', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Contact',
            },
        ),
        migrations.CreateModel(
            name='Organigramme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=70)),
                ('mission', models.CharField(default='membre', max_length=200)),
            ],
            options={
                'db_table': 'Organigramme',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=70)),
                ('prenom', models.CharField(blank=True, max_length=70, null=True)),
                ('genre', models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin')], default='M', max_length=10)),
                ('phone', models.CharField(max_length=70)),
                ('adhesion', models.DateField(blank=True)),
                ('photo', models.FileField(blank=True, null=True, upload_to='photo/')),
                ('actif', models.BooleanField(default=True)),
                ('fonction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fdm.organigramme')),
            ],
            options={
                'db_table': 'Equipe',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=70)),
                ('photo', models.FileField(blank=True, null=True, upload_to='photo/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fdm.categorie')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='fdm.user')),
            ],
            options={
                'db_table': 'Article',
            },
        ),
    ]
