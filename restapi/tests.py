# from django.test import TestCase
# from restapi import models
from unittest import TestCase

# Create your tests here.
def two_integers_sum(a, b):
    return 0


class TestSum(TestCase):
    def test_sum(self):
        self.assertEqual(two_integers_sum(1, 2), 3)


# class TestModels(TestCase):
# def test_expense(self):
# expense = models.Expense.objects.create(
# amount=249.99,
# merchant="amazon",
# description="anc headphones",
# category="music",
# )
# inserted_expense = models.Expense.objects.get(pk=expense.id)

# self.assertEqual(249.99, inserted_expense.amount)
# self.assertEqual("amazon", inserted_expense.merchant)
# self.assertEqual("anc headphones", inserted_expense.description)
# self.assertEqual("music", inserted_expense.category)
