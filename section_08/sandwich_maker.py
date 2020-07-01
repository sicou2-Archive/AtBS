# What kind of sandwich do you want?
# with inputMenu() bread type: wheat, white, sourdough
# With inputMenu() protein type: chicken, turkey, ham, tofu
# With inputYesNo() cheese?
# With inputMenu() if yes cheese, what kind: cheddar, swiss, mozzarella
# With inputYesNo(), mayo, mustard, lettuce, tomato
# inputInt() how many sandwiches do they want? Must be more than 1.
# Make prices for each item and total it up for 'checkout'.

sandwich_prices = {
    'bread': {
        'wheat': 1,
        'white': 1,
        'sourdough': 1,
    },
    'protein': {
        'chicken': 1,
        'bacon': 1,
        'turkey': 1,
        'ham': 1,
        'tofu': 1,
    },
    'cheese': {
        'cheddar': 1,
        'Swiss': 1,
        'mozzarella': 1,
    },
    'toppings': {
        'mayo': 1,
        'mustard': 1,
        'lettuce': 1,
        'tomato': 1,
    },
}

print("Help me build the sandwich you want to day.")
bread_q = "What kind of bread would you like? ### STOPPED HERE"
bread = inputMenu('What kind of bread would you like?')
