class FoodItem:

    def __init__(self, name):
        self.name = name
        self.nutrition = {
            'calories',
            'total_fat',
            'sat_fat',
            'poly_fat',
            'mono_fat',
            'trans_fat',
            'cholesterol',
            'sodium',
            'potassium',
            'total_carbs',
            'dietary_fiber',
            'sugars',
            'protein',
            'vitamin_a',
            'vitamin_c',
            'calcium',
            'iron'}

    def set_nutrition(self, nutrition_dictionary):
        self.nutrition = nutrition_dictionary

    def get_nutrition(self, key):
        return self.nutrition[key]