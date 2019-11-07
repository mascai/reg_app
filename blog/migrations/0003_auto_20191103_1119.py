# Generated by Django 2.0.13 on 2019-11-03 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191026_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advuser',
            name='is_activated',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Прошёл активацию?'),
        ),
        migrations.AlterField(
            model_name='advuser',
            name='send_messages',
            field=models.BooleanField(default=True, verbose_name='Слать оповещёния о новых комментариях?'),
        ),
    ]
