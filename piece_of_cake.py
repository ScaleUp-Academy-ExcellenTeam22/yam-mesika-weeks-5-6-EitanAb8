from functools import reduce


def get_recipe_price(prices, optionals=[], **ingredients) -> float:
    """
    The function calculates the total price of the desired ingredients.
    :param prices: A dictionary of ingredients and their price for 100 grams.
    :param optionals: Ingredients to ignore in the cart.
    :param ingredients: The Amount of grams for each ingredient the costumer wants to buy.
    :return:
    """
    return reduce(lambda summary, name: summary+(prices[name]/100)*(ingredients[name])
                  if name in ingredients.keys() and name not in optionals else summary+0, prices, 0)


def main():
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk', 'banana'], chocolate=300))
    print(get_recipe_price({}))


if __name__ == '__main__':
    main()