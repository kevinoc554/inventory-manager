# Generated by Django 4.0.5 on 2022-06-12 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_inventory_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='delete_comment',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]