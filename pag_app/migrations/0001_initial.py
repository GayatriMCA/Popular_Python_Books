# Generated by Django 3.2.2 on 2021-05-29 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Author', models.CharField(max_length=200)),
                ('Title', models.CharField(max_length=200)),
                ('Description', models.TextField()),
                ('slug', models.SlugField()),
            ],
        ),
    ]
