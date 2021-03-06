# Generated by Django 3.1.7 on 2021-03-07 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='camera_type',
            field=models.CharField(choices=[('canon', 'canon'), ('nikon', 'nikon'), ('sony', 'sony'), ('panasonic', 'panasonic'), ('other', 'other')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='category',
            field=models.CharField(choices=[('code', 'code'), ('mobile review', 'mobile review'), ('comedy', 'comedy'), ('reaction', 'reaction'), ('cooking', 'cooking'), ('education', 'education')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='crew',
            field=models.CharField(choices=[('solo', 'solo'), ('small', 'small'), ('large', 'large')], max_length=255),
        ),
    ]
