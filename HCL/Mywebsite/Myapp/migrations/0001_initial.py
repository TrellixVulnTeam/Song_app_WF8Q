# Generated by Django 2.1.dev20180206232904 on 2018-02-12 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Odc1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=60)),
                ('person_age', models.IntegerField()),
            ],
        ),
    ]
