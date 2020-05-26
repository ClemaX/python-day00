cookbook = {
    'sandwich':
    {
        'ingredients':
        [
            'ham',
            'bread',
            'cheese',
            'tomatoes'
        ],
        'meal': 'lunch',
        'prep_time': 10
    },
    'cake':
    {
        'ingredients':
        [
            'flour',
            'sugar',
            'eggs'
        ],
        'meal': 'dessert',
        'prep_time': 60
    },
    'salad':
    {
        'ingredients':
        [
            'avocado',
            'arugula',
            'tomatoes',
            'spinach'
        ],
        'meal': 'lunch',
        'prep_time': 15
    },
}


def print_recipe(name):
    recipe = cookbook.get(name)
    if recipe:
        print(f"~{name}~")
        print(f"ingredients: ")
        for ingredient in recipe['ingredients']:
            print(f" - {ingredient}")
        print(f"To be eaten for {recipe['meal']}.")
        print(f"Takes {recipe['prep_time']} minutes of cooking.")
    else:
        print(f"~{name}~ can't be found!")


def delete_recipe(name):
    recipe = cookbook.pop(name, None)
    if recipe:
        print(f"Deleted ~{name}~!")
    else:
        print(f"~{name}~ can't be found!")


def add_recipe(name, ingredients, meal, prep_time):
    cookbook[name] = {
        'ingredients': ingredients,
        'meal': meal,
        'prep_time': prep_time
    }


def print_recipes():
    print("{0:<10} | {1:<10}".format("RECIPE", "TYPE"))
    print('=' * 20)
    for recipe in cookbook:
        print(f"{recipe:<10} | {cookbook[recipe]['meal']}")
        print('-' * 20)


def menu_add():
    name = input("name: ")
    print("ingredients (enter empty line to end):")
    ingredients = []
    while True:
        ingredient = input(" - ")
        if not ingredient:
            break
        ingredients.append(ingredient)
    meal = input("meal: ")
    prep_time = input("preparation time (in min.): ")
    add_recipe(name, ingredients, meal, prep_time)
    pass


def menu_delete():
    print("Please enter the name of the recipe to be deleted.")
    name = input(">> ")
    delete_recipe(name)
    pass


def menu_print():
    print("Please enter the recipe's name to get its details.")
    name = input(">> ")
    print_recipe(name)
    pass


def menu_list():
    print_recipes()
    pass


def menu_quit():
    print("Cookbook closed.")
    quit()


def menu_help():
    print("This option does not exist, " +
          "please type the corresponding number.\n" +
          "To exit, enter 5.")


def menu():
    options = {
        1: ("Add a recipe", menu_add),
        2: ("Delete a recipe", menu_delete),
        3: ("Print a recipe", menu_print),
        4: ("Print the cookbook", menu_list),
        5: ("Quit", menu_quit),
    }

    print("Please select an option by typing the corresponding number:")
    for option in options:
        print(f"{option}: {options[option][0]}")

    done = False
    while not done:
        choice = input(">> ")
        try:
            choice = int(choice)
            done = choice in options
            if not done:
                menu_help()
        except ValueError:
            menu_help()
    options[choice][1]()


while True:
    menu()
    print()
