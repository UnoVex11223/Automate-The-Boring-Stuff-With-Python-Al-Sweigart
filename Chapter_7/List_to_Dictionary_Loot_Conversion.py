from Fantasy_Game_Inventory import display_inventory

def add_to_inventory(inventory: dict, added_items: list):
    """
    Adds items from a list to an inventory dictionary.

    Args:
        inventory: The dictionary to update.
        added_items: A list of strings representing the items to add.

    Returns:
        The inventory dictionary updated with the new items.
    """
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
