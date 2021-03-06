# Generated by Django 2.0.7 on 2018-08-20 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mingler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120, null=True)),
                ('img_path', models.TextField(null=True)),
                ('my_hashtags', models.TextField(null=True)),
                ('looking_for_hashtags', models.TextField(null=True)),
                ('description', models.TextField(max_length=2000, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
