# FantasyGameInventory.py
print("Name:Lata.S.B",
       "USN:1AY24AI060",
       "Section:'O'")
def display_inventory(inventory):
    print("Inventory:")
    total_items = 0
    for item, count in inventory.items():
        print(f"{count} x {item}")
        total_items += count
    print(f"Total number of items: {total_items}\n")

def add_to_inventory(inventory, loot):
    for item in loot:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

# Example inventory and loot
if _name_ == "_main_":
    inventory = {"gold coin": 42, "rope": 1, "torch": 6, "dagger": 1}
    dragon_loot = ["gold coin", "dagger", "gold coin", "ruby", "gold coin"]

    print("Before collecting loot:")
    display_inventory(inventory)

    inventory = add_to_inventory(inventory, dragon_loot)

    print("After collecting loot:")
    display_inventory(inventory)