# Generated by Django 3.0 on 2020-09-03 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0043_auto_20200903_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='reassign_reason',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
