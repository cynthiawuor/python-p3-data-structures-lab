spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
 return [food["name"] for food in spicy_foods]
names = get_names(spicy_foods)
print("names")
pass

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []  
    for food in spicy_foods:
        if food["heat_level"] > 5:  
            spiciest_foods.append(food)  
    return spiciest_foods
    pass

def new_func(spicy_foods):
    food_names = []
    for food in spicy_foods:
        if isinstance(food, dict) and 'name' in food:
            food_names.append(food['name'])
        return food_names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods:
        if isinstance(food, dict) and 'heat_level' in food:
            if food['heat_level'] > 5:
                spiciest_foods.append(food)
        return spiciest_foods

    pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        if isinstance(food, dict) and 'name' in food and 'cuisine' in food and 'heat_level' in food:
            heat_emoji = "🌶" * food['heat_level']
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_emoji}")

    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if isinstance(food, dict) and 'name' in food and 'cuisine' in food:
            if food['cuisine'] == cuisine:
                return food  
    
    return None

    pass

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if isinstance(food, dict) and 'name' in food and 'cuisine' in food and 'heat_level' in food:
            if food['heat_level'] > 5:
                heat_emoji = "🌶" * food['heat_level']
                
                print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_emoji}")

    pass

def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0  

    total_heat = sum(food["heat_level"] for food in spicy_foods)
    average = total_heat // len(spicy_foods)  
    return average

    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
new_spicy_food = {'name': 'Spicy Tacos', 'cuisine': 'Mexican', 'heat_level': 4}
updated_spicy_foods = create_spicy_food(spicy_foods, new_spicy_food)
print(updated_spicy_foods)
pass

