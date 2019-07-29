# Generated by Django 2.2.1 on 2019-05-18 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('f', 'Female'), ('m', 'Male'), ('u', 'Undisclosed')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='phone_no',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.IntegerField(unique=True),
        ),
    ]