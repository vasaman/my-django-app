# Generated by Django 3.0.8 on 2020-12-04 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=30)),
                ('last', models.CharField(max_length=30)),
                ('buses', models.ManyToManyField(blank=True, related_name='passenger', to='bus.bus')),
            ],
        ),
    ]
