# Generated by Django 3.0.2 on 2020-01-20 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
    ]
