# Generated by Django 4.2.6 on 2024-06-04 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0005_supporter_chat_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='chats',
            name='Chat_Owner',
            field=models.IntegerField(default='0'),
        ),
    ]
