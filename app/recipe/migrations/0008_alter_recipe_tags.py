# Generated by Django 3.2.16 on 2022-12-11 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0007_alter_recipe_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='recipes', to='recipe.Tag'),
        ),
    ]
