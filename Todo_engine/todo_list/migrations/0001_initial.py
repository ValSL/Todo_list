# Generated by Django 3.0.3 on 2020-02-08 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('check', models.BooleanField()),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
