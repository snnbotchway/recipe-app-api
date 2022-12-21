# Generated by Django 3.2.16 on 2022-12-20 09:07

from django.db import migrations, models
import recipe.models
import recipe.validators


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0011_recipeimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeimage',
            name='image',
            field=models.ImageField(upload_to=recipe.models.recipe_image_file_path, validators=[recipe.validators.validate_file_size]),
        ),
    ]