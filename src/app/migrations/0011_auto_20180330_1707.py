# Generated by Django 2.0.3 on 2018-03-30 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_node_is_relay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delegate',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
