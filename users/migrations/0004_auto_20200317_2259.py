# Generated by Django 2.2.5 on 2020-03-17 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200317_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='currency',
            field=models.CharField(choices=[('krw', 'KRW'), ('usd', 'USD')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('kr', 'Korean'), ('en', 'English')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='superhost',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, default=''),
        ),
    ]
