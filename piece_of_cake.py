
def get_recipe_price(prices, optionals=None, **ingredients):
    # This function receives:
    # prices - dictionary of ingredients and their price for 100 grams.
    # optionals - ingredients to ignore in the cart
    # ingredients - grams for each ingredient we want to buy
    # the function will calculate and return the sum of the ingredients price

    final_price = 0
    for name, price in prices.items():
        final_price += price*(ingredients[name]/100) if name in ingredients.keys() else 0
    return final_price


def main():

    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(get_recipe_price({}))


if __name__ == '__main__':
    main()
