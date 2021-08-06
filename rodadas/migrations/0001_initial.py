# Generated by Django 3.2.6 on 2021-08-03 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rodada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('date', models.DateTimeField()),
                ('description', models.TextField()),
                ('drive', models.URLField()),
                ('presentation', models.URLField()),
                ('recording', models.URLField()),
            ],
        ),
    ]
