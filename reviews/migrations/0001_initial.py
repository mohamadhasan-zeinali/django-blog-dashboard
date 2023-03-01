# Generated by Django 3.1.5 on 2021-06-09 12:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('slug', models.SlugField(verbose_name='url')),
                ('description', models.TextField(max_length=500, verbose_name='description')),
                ('thumbnail', models.ImageField(upload_to='images', verbose_name='picture')),
                ('date', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('status', models.CharField(choices=[(' P ', 'PUBLISH'), (' d ', 'DRAFT')], max_length=3, verbose_name='status')),
            ],
        ),
    ]