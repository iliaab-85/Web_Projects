# Generated by Django 4.2.6 on 2024-06-10 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0011_chats_visit_seller_chats_visit_support_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller_genuine',
            name='State',
            field=models.CharField(default='Create', max_length=20),
        ),
        migrations.AddField(
            model_name='seller_legal',
            name='State',
            field=models.CharField(default='Create', max_length=20),
        ),
    ]
