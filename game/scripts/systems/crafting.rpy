init python:
    # --- Crafting & Interaction State ---
    crafting_items = []
    selected_items = []
    selected_item = None
    selected_holding_item = None


    medkit_contents = {
        "Bandage": {"conditions": ["bleeding", "cut"], "healing": 10},
        "Phenergan": {"conditions": ["nausea"], "healing": 5},
        "Antibiotics": {"conditions": ["infection"], "healing": 20},
        "Morphine": {"conditions": [""], "healing": 30},
        "Water Gel": {"conditions": ["burn"], "healing": 15},
        "Acetaminophen": {"conditions": [""], "healing": 10},
        "Diphenhydramine": {"conditions": ["pain"], "healing": 10},
        "SOFT-T": {"conditions": ["hemorrhage", "fracture","bleeding"], "healing": 10},
        "Naproxen": {"conditions": ["headache"], "healing": 10}
    }
    crafting_recipes = {
        ("Laser range finder", "Tactical flashlight"): {"result": "Laser Tactical Kit", "holding_item": "Glue"},
        ("Compass", "radio"): {"result": "Navigation Radio", "holding_item": "Screwdriver"}
    }
    deconstruction_recipes = {
        "Laser Tactical Kit": ["Laser range finder", "Tactical flashlight", "Glue"],
        "Navigation Radio": ["Compass", "Radio", "Screwdriver"],
        "First Aid Kit": ["Bandage", "Antibiotics", "Acetaminophen", "SOFT-T"],
        "Flashlight": ["Bulb", "Battery", "Reflector"],
        "radio": ["Antenna", "Battery", "Circuit Board"]
    }
    liquid_mix_recipes = {
        "Cleaning Solution": {"Water": 90, "Ethanol": 10},
        "Emulsion": {"Oil": 50, "Water": 50},
        "Slime": {"Water": 100, "Glue": 30},
    }

    def add_crafting_item(item):
        if len(crafting_items) < 2:
            crafting_items.append(item)
            renpy.notify(f"{item} added to crafting box.")
        else:
            renpy.notify("You can only combine two items.")

    def remove_crafting_item(item):
        if item in crafting_items:
            crafting_items.remove(item)
            renpy.notify(f"{item} removed from crafting box.")

    def select_item(item):
        if item not in selected_items and len(selected_items) < 2: # Limit to 2 for combining
            selected_items.append(item)

    def combine_items():
        global selected_items, inventory, liquid_inventory
        if len(selected_items) != 2:
            renpy.notify("You need exactly two items to combine.")
            return

        item_tuple = tuple(sorted(selected_items))
        if item_tuple in crafting_recipes:
            recipe = crafting_recipes[item_tuple]
            holding_item = recipe["holding_item"]

            # Check for holding item (e.g., Glue, Screwdriver)
            if holding_item == "Glue":
                glue_available = any(liquid["name"] == "Glue" and liquid["amount"] > 0 for liquid in liquid_inventory)
                if not glue_available:
                    renpy.notify("You need Glue to hold the items together.")
                    return
            elif holding_item not in inventory:
                renpy.notify(f"You need {holding_item} to hold the items together.")
                return

            # Craft the item
            new_item = recipe["result"]
            inventory.append(new_item)
            for item in selected_items: inventory.remove(item)

            if holding_item == "Glue":
                for liquid in liquid_inventory:
                    if liquid["name"] == "Glue":
                        liquid["amount"] -= 10
                        if liquid["amount"] <= 0: liquid_inventory.remove(liquid)
                        break

            renpy.notify(f"You crafted: {new_item} using {holding_item}.")
            selected_items.clear()
        else:
            renpy.notify("These items cannot be combined.")

    def deconstruct_item(item):
        global inventory
        if item in deconstruction_recipes and item in inventory:
            components = deconstruction_recipes[item]
            for component in components: inventory.append(component)
            inventory.remove(item)
            renpy.notify(f"You deconstructed {item} into: {', '.join(components)}.")
        else:
            renpy.notify(f"{item} cannot be deconstructed or is not in inventory.")        