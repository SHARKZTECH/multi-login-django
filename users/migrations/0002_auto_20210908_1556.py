# Generated by Django 3.2.6 on 2021-09-08 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='telephone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='nationid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
