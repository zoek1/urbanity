# Generated by Django 3.0.3 on 2020-06-14 18:32

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='POI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(max_length=800)),
                ('precision', models.IntegerField(default=10)),
                ('poi', models.CharField(default='', max_length=200)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('space', models.CharField(default='', max_length=200)),
                ('did', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('space', models.CharField(default='', max_length=200)),
                ('did', models.CharField(default='', max_length=200)),
                ('info', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('status', models.CharField(choices=[('active', 'active'), ('challenged', 'challenged')], default='active', max_length=200)),
                ('challenge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='availability.Features')),
                ('poi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='availability.POI')),
            ],
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('space', models.CharField(default='', max_length=200)),
                ('did', models.CharField(default='', max_length=200)),
                ('schedule', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('challenge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='availability.Availability')),
                ('poi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='availability.POI')),
            ],
        ),
    ]
