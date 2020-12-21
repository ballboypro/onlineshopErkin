from django.test import TestCase, Client
from .models import Product, Category


class CartTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_cart(self):
        response = self.client.get('/cart/')

        self.assertEqual(response.status_code, 200)


class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name='msi', slug='Bob')

    def test_name_label(self):
        category=Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Имя категории')

    def test_name_max_length(self):
        category=Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)

    def test_object_name_is_slug_comma_name(self):
        category=Category.objects.get(id=1)
        self.assertEquals(category.name, str(category))

    def test_get_absolute_url(self):
        category=Category.objects.get(id=1)
        self.assertEquals(category.get_absolute_url(), '/category/Bob/')


class ProductTestCase(TestCase):
    def setUp(self):
        c = Category.objects.create(name='Notebook', slug='Macbooks')
        Product.objects.create(category=c, title='Asus', slug='Macs', price='1000')






