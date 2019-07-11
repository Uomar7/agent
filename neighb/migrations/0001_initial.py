# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-11 12:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=66)),
                ('pic1', models.ImageField(upload_to='houses/')),
                ('pic2', models.ImageField(upload_to='houses/')),
                ('pic3', models.ImageField(upload_to='houses/')),
                ('location', models.CharField(max_length=80)),
                ('price', models.CharField(max_length=80)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=40)),
                ('lname', models.CharField(max_length=40)),
                ('id_no', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('profile_pic', models.ImageField(blank=True, upload_to='avatar/')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=120)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='neighb.Home')),
                ('posted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighb.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='home',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='houses', to='neighb.Profile'),
        ),
    ]
