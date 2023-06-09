# Generated by Django 4.1.7 on 2023-03-30 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', models.EmailField(max_length=254)),
                ('send_date', models.DateField()),
                ('send_time', models.TimeField()),
                ('template', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='ToDoList',
            new_name='Objetos',
        ),
    ]
