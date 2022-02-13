import unittest
from django.test import TestCase, Client, RequestFactory, SimpleTestCase
from django.urls import reverse

from flavors.models import Flavor


class FlavorModelTests(TestCase):

    def setUp(self):
        Flavor.objects.create(title='test', scoops_remaining=1, slug='test')

    def test_flavor_exists(self):
        flavor = Flavor.objects.filter(title='test', scoops_remaining=1, slug='test').exists()
        self.assertIs(flavor, True)


def add_x(base, x):
    return base + x


class AdditionTest(TestCase):

    def test_add_x_adds_x(self):
        base = 10
        x = 5
        expected = 15
        result = add_x(base, x)
        self.assertTrue(result == expected)


def div_x(base, x):
    return base | x
