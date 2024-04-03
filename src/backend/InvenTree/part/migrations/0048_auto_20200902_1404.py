# Generated by Django 3.0.7 on 2020-09-02 14:04

import InvenTree.fields

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0047_auto_20200808_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='IPN',
            field=models.CharField(blank=True, help_text='Internal Part Number', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='part',
            name='keywords',
            field=models.CharField(blank=True, help_text='Part keywords to improve visibility in search results', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='part',
            name='link',
            field=InvenTree.fields.InvenTreeURLField(blank=True, help_text='Link to external URL', null=True),
        ),
        migrations.AlterField(
            model_name='part',
            name='revision',
            field=models.CharField(blank=True, help_text='Part revision or version number', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='part',
            name='notes',
            field=models.TextField(blank=True, help_text='Part notes - supports Markdown formatting', null=True),
        ),
        migrations.AlterField(
            model_name='part',
            name='units',
            field=models.CharField(blank=True, default='', help_text='Stock keeping units for this part', max_length=20, null=True),
        ),
    ]