# xxx What kind of sandwich do you want?
# xxx with inputMenu() bread type: wheat, white, sourdough
# xxx With inputMenu() protein type: chicken, turkey, ham, tofu
# xxx With inputYesNo() cheese?
# xxx With inputMenu() if yes cheese, what kind: cheddar, swiss, mozzarella
# xxx With inputYesNo(), mayo, mustard, lettuce, tomato
# xxx inputInt() how many sandwiches do they want? Must be more than 1.
# xxx Make prices for each item and total it up for 'checkout'.
import pyinputplus as pyip


sandwich_prices = {
    'wheat': 1.05,
    'white': 1.10,
    'sourdough': 1.15,
    'chicken': 1.20,
    'bacon': 1.25,
    'turkey': 1.30,
    'ham': 1.35,
    'tofu': 1.40,
    'cheddar': 1.00,
    'Swiss': 1.05,
    'mozzarella': 1.10,
    'mayo': .1,
    'mustard': .15,
    'lettuce': .05,
    'tomato': .05,
}

sandwich = []

print("Help me build the sandwich you want to day.")
bread_q = "What kind of bread would you like? White, Wheat, Sourdough: "
sandwich.append(pyip.inputMenu(['white', 'wheat', 'sourdough'], bread_q))

protein_q = ("Choose one kind of protein you want. Bacon, Chicken, Ham, Tofu,"
             " Turkey: ")
sandwich.append(pyip.inputMenu(
    ['bacon', 'chicken', 'ham', 'tofu', 'turkey'],
    protein_q
)
)

cheese_q_1 = "Do you want cheese on that? "
cheese_yes_no = pyip.inputYesNo(cheese_q_1)

if cheese_yes_no == 'yes':  # if no breaks print below
    cheese_q = ("What kind of cheese would you like? Cheddar, Swiss,"
                " Mozzarella: ")
    sandwich.append(pyip.inputMenu(
        ['Cheddar', 'Swiss', 'Mozzarella'],
        cheese_q
    )
    )

toppings_list = ['mayo', 'mustard', 'lettuce', 'tomato']
toppings = []

for topping in toppings_list:
    topping_q = f"Do you want {topping} added? "
    topping_wanted = pyip.inputYesNo(topping_q)
    if topping_wanted == 'yes':
        sandwich.append(topping)

quantity_q = "How many sandwiches do you want? "
quantity = pyip.inputInt(quantity_q, min=1)


cost = 0
for part in sandwich:
    cost += sandwich_prices[part]

total = cost * quantity

print(f"Your total cost for your sandwich will be ${round(total, 2)}.")
