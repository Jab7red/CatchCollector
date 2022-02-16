# Generated by Django 4.0.2 on 2022-02-16 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(choices=[('R', 'Red'), ('W', 'White'), ('B', 'Blue'), ('G', 'Green'), ('Y', 'Yellow'), ('S', 'Shad')], default='R', max_length=100)),
                ('catch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.catch')),
            ],
        ),
    ]