# Generated by Django 3.1 on 2021-11-08 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myquiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('Sno', models.AutoField(primary_key=True, serialize=False)),
                ('Ques', models.CharField(default='', max_length=300)),
                ('opt1', models.CharField(default='', max_length=200)),
                ('opt2', models.CharField(default='', max_length=200)),
                ('opt3', models.CharField(default='', max_length=200)),
                ('opt4', models.CharField(default='', max_length=200)),
            ],
        ),
    ]