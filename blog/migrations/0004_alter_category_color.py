# Generated by Django 3.2.5 on 2021-08-04 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='color',
            field=models.CharField(blank=True, choices=[('pink', 'pink'), ('red', 'red'), ('aqua', 'aqua'), ('green', 'green'), ('grey', 'grey'), ('yellow', 'yellow'), ('custom-blue', 'custom-blue'), ('orange', 'orange')], max_length=12, null=True),
        ),
    ]
