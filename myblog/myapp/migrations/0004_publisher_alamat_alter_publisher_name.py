# Generated by Django 4.2.6 on 2023-10-19 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_book_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='alamat',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
