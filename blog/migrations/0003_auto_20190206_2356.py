# Generated by Django 2.0.10 on 2019-02-06 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
