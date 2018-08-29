# Generated by Django 2.0.7 on 2018-08-29 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0011_mingler_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalHashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=120)),
            ],
        ),
        migrations.RemoveField(
            model_name='mingler',
            name='cropping',
        ),
        migrations.RemoveField(
            model_name='mingler',
            name='image',
        ),
        migrations.AlterField(
            model_name='mingler',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]