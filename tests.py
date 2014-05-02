import unittest
from fooditem import FoodItem

class FoodItemTests(unittest.TestCase):

    def setUp(self):
        self.banana = FoodItem('banana')
        banana_nutrition = {
            'calories' : 110,
            'total_fat': 0,
            'sat_fat': 0,
            'poly_fat': 0,
            'mono_fat': 0,
            'trans_fat': 0,
            'cholesterol': 0,
            'sodium': 0,
            'potassium': 450,
            'total_carbs': 29,
            'dietary_fiber': 3,
            'sugars': 15,
            'protein': 1,
            'vitamin_a': 2,
            'vitamin_c': 20,
            'calcium': 0,
            'iron': 2
        }
        self.banana.set_nutrition(banana_nutrition)

    def test_set_and_get_nutrition_facts(self):
        self.assertEqual(self.banana.get_nutrition('calories'), 110)


