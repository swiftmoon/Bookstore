# Generated by Django 4.0.2 on 2022-02-26 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='')),
                ('author', models.CharField(default='admin', max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('describe', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
