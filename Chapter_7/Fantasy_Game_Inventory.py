inventory = {"torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}


def display_inventory(player_inventory: dict):
    """
    Prints the contents of an inventory dictionary.

    Args:
        player_inventory: A dictionary representing the player's inventory.
    """
    print("Inventory:")
    item_total = 0
    for key, value in player_inventory.items():
        print(f"{value} {key}")
        item_total += value

    print(f"Total number of items: {item_total}")


display_inventory(inventory)
