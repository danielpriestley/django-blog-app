# Generated by Django 2.0.10 on 2019-02-07 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190207_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(default='blog/static/media/default.jpg', upload_to=''),
        ),
    ]
