# Generated by Django 2.2.5 on 2020-08-31 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_bigbluebutton', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='internal_meeting_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='parent_meeting_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='welcome_text',
            field=models.TextField(default='Welcome!'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
