inventory = {
    'arrow': 12,
    'gold coin': 42,
    'rope': 1,
    'torch': 6,
    'dagger': 1,
    'scrolls': 17
    }

new_items = {
    'gold coin': 8,
    'sword': 1,
    'arrow': 4,
    'torch': 2,
    'helmet': 1,

    }

def print_inventory(inventory):
    total_items = 0
    for k, v in inventory.items():
        print(v, k)
        total_items += v
    print(total_items, "items in inventory\n")

# print_inventory(inventory)

def add_inventory(inventory, items_add):
    for k, v in items_add.items():

        inventory.setdefault(k, 0)
        inventory[k] += v
    print_inventory(inventory)

add_inventory(inventory, new_items)