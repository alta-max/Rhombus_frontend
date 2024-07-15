# Generated by Django 5.0.1 on 2024-07-15 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=50)),
                ('nat_lang_input', models.CharField(max_length=300)),
                ('regex_pattern', models.CharField(max_length=100)),
            ],
        ),
    ]