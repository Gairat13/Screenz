# Generated by Django 3.1 on 2021-03-04 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0007_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='genre',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
    ]