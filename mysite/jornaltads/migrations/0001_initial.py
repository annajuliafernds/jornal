# Generated by Django 4.0.6 on 2024-09-20 01:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Edicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_edicao', models.DateField()),
                ('titulo_edicao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sobrenome', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=60)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60)),
                ('texto_noticia', models.TextField(max_length=255)),
                ('data_noticia', models.DateField(default=django.utils.timezone.now)),
                ('edicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jornaltads.edicao')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_comentario', models.CharField(max_length=255)),
                ('noticia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jornaltads.noticia')),
            ],
        ),
    ]
