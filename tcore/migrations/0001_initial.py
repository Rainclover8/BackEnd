# Generated by Django 3.2.5 on 2024-03-01 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resim', models.FileField(upload_to='media/resimler', verbose_name='resim')),
                ('baslik', models.CharField(max_length=20)),
                ('aciklama', models.TextField()),
            ],
        ),
    ]
