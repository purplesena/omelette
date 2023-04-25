# Generated by Django 4.1.6 on 2023-03-16 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.CharField(default='15', max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(default='hey', max_length=500),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='physical_desc',
            field=models.CharField(default='georgeous', max_length=500),
        ),
    ]