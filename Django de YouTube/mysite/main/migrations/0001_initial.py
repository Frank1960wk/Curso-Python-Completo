# Generated by Django 3.1.7 on 2021-03-23 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso_titulo', models.CharField(max_length=200)),
                ('curso_contenido', models.TextField()),
                ('curso_publicado', models.DateField(verbose_name='fecha de publicación')),
            ],
        ),
    ]
