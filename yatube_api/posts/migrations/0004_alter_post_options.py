# Generated by Django 3.2.16 on 2023-11-01 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-pub_date',)},
        ),
    ]