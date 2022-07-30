# Generated by Django 4.0.6 on 2022-07-30 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('total_pages', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('isbn', models.CharField(max_length=13)),
                ('date', models.DateField()),
                ('author', models.ManyToManyField(to='books.author')),
            ],
        ),
    ]