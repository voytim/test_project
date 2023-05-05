import requests

api_key = '02d638dac4514d7eb4ee6996610f7b34'


def get_dish(ingredients, number):
    req = 'https://api.spoonacular.com/recipes/findByIngredients'
    my_params = {
        'apiKey': api_key,
        'ingredients': ingredients,
        'number': number
    }

    response = requests.get(req, params=my_params)
    result = response.json()
    res = []
    for dish in result:
        id = dish['id']
        title = dish['title']
        img_ref = dish['image']
        missed_ing = []
        for ing in dish['missedIngredients']:
            missed_ing.append(ing['name'])
        res.append((img_ref, missed_ing, id, title))
    return res


def get_recipe(id):
    req = f"https://api.spoonacular.com/recipes/{id}/information?includeNutrition=false"
    response = requests.get(req, params={'apiKey': api_key})
    result = response.json()
    recipe_ref = result['spoonacularSourceUrl']
    return recipe_ref
