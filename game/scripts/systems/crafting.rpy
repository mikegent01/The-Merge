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

