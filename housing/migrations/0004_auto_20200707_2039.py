# Generated by Django 3.0.5 on 2020-07-07 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0003_auto_20200706_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image1',
            field=models.ImageField(blank=True, upload_to='housing_pics'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, upload_to='housing_pics'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image3',
            field=models.ImageField(blank=True, upload_to='housing_pics'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image4',
            field=models.ImageField(blank=True, upload_to='housing_pics'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image5',
            field=models.ImageField(blank=True, upload_to='housing_pics'),
        ),
    ]
