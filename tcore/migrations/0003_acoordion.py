# Generated by Django 3.2.5 on 2024-03-03 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcore', '0002_alter_model_aciklama'),
    ]

    operations = [
        migrations.CreateModel(
            name='acoordion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=20)),
                ('aciklama', models.TextField()),
            ],
        ),
    ]
