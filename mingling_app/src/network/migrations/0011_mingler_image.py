# Generated by Django 2.0.7 on 2018-08-28 15:23

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0010_mingler_cropping'),
    ]

    operations = [
        migrations.AddField(
            model_name='mingler',
            name='image',
            field=image_cropping.fields.ImageCropField(default='pic_folder/None/no-img.jpg', upload_to='media/'),
        ),
    ]
