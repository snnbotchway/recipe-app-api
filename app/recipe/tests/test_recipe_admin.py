"""Recipe admin tests"""
from decimal import Decimal

from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from recipe.models import (
    Recipe, Tag, Ingredient)


def create_recipe(user, **params):
    """Creates and returns new recipe"""
    defaults = {
        "title": "Sample Recipe Name",
        "time_minutes": 20,
        "description": "Boil for 5 minutes, allow to cool for 15 minutes.",
        "price": Decimal('34.12'),
        "link": "https://recipe.com/recipe.pdf"
    }
    defaults.update(params)
    return Recipe.objects.create(user=user, **defaults)


def create_tag(user, **params):
    """Creates and returns new tag"""
    defaults = {"name": "Sample Tag Name"}
    defaults.update(params)
    return Tag.objects.create(user=user, **defaults)


def create_ingredient(user, **params):
    """Creates and returns new ingredient"""
    defaults = {"name": "Sample Ingredient Name"}
    defaults.update(params)
    return Ingredient.objects.create(user=user, **defaults)


class RecipeAdminSiteTests(TestCase):
    """RecipeAdmin site tests."""

    def setUp(self):
        """Setup variables used by numerous functions in the class."""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testPass123',
            first_name='admin_first_name',
            last_name='admin_last_name'
        )
        self.client.force_login(self.admin_user)
        self.recipe = create_recipe(user=self.admin_user)

    def test_recipe_list_page(self):
        """Test recipe list page responds well."""
        url = reverse('admin:recipe_recipe_changelist')

        response = self.client.get(url)

        self.assertContains(response, self.recipe.title)
        self.assertContains(response, self.recipe.id)
        self.assertContains(response, self.recipe.time_minutes)
        self.assertContains(response, self.recipe.price)
        self.assertContains(response, self.recipe.user)
        self.assertNotContains(response, self.recipe.description)

    def test_recipe_detail_page(self):
        """Test recipe detail page responds well."""
        url = reverse('admin:recipe_recipe_change',
                      args=[self.recipe.id])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_add_recipe_page(self):
        """Test add recipe page responds well."""
        url = reverse('admin:recipe_recipe_add')

        response = self.client.post(url)

        self.assertEqual(response.status_code, 200)


class TagAdminSiteTests(TestCase):
    """TagAdmin site tests."""

    def setUp(self):
        """Setup variables used by numerous functions in the class."""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testPass123',
            first_name='admin_first_name',
            last_name='admin_last_name'
        )
        self.client.force_login(self.admin_user)
        self.tag = create_tag(user=self.admin_user)

    def test_tag_list_page(self):
        """Test tag list page responds well."""
        url = reverse('admin:recipe_tag_changelist')

        response = self.client.get(url)

        self.assertContains(response, self.tag.name)
        self.assertContains(response, self.tag.user)

    def test_tag_detail_page(self):
        """Test tag detail page responds well."""
        url = reverse('admin:recipe_tag_change',
                      args=[self.tag.id])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_add_tag_page(self):
        """Test add tag page responds well."""
        url = reverse('admin:recipe_tag_add')

        response = self.client.post(url)

        self.assertEqual(response.status_code, 200)


class IngredientAdminSiteTests(TestCase):
    """IngredientAdmin site tests."""

    def setUp(self):
        """Setup variables used by numerous functions in the class."""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testPass123',
            first_name='admin_first_name',
            last_name='admin_last_name'
        )
        self.client.force_login(self.admin_user)
        self.ingredient = create_ingredient(user=self.admin_user)

    def test_ingredient_list_page(self):
        """Test ingredient list page responds well."""
        url = reverse('admin:recipe_ingredient_changelist')

        response = self.client.get(url)

        self.assertContains(response, self.ingredient.name)
        self.assertContains(response, self.ingredient.user)

    def test_ingredient_detail_page(self):
        """Test ingredient detail page responds well."""
        url = reverse('admin:recipe_ingredient_change',
                      args=[self.ingredient.id])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_add_ingredient_page(self):
        """Test add ingredient page responds well."""
        url = reverse('admin:recipe_ingredient_add')

        response = self.client.post(url)

        self.assertEqual(response.status_code, 200)
