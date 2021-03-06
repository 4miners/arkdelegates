# Generated by Django 2.0.3 on 2018-03-13 08:54

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voters', models.IntegerField(blank=True, null=True)),
                ('uptime', models.FloatField(blank=True, null=True)),
                ('approval', models.FloatField(blank=True, null=True)),
                ('rank', models.IntegerField(blank=True, db_index=True, null=True)),
                ('forged', models.FloatField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('payload', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
            ],
        ),
        migrations.RemoveField(
            model_name='votehistory',
            name='delegate',
        ),
        migrations.RemoveField(
            model_name='delegate',
            name='approval',
        ),
        migrations.RemoveField(
            model_name='delegate',
            name='forged',
        ),
        migrations.RemoveField(
            model_name='delegate',
            name='uptime',
        ),
        migrations.AddField(
            model_name='delegate',
            name='website',
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='proposal',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='VoteHistory',
        ),
        migrations.AddField(
            model_name='history',
            name='delegate',
            field=models.ManyToManyField(related_name='history', to='app.Delegate'),
        ),
    ]
