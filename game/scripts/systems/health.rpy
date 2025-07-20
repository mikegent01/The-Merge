# This is the full and final class definition file.
# It contains all necessary data and logic for characters and inventories.

init python:
    import random

    # ==============================================================================
    # 1. GLOBAL GAME DATA (Databases that don't belong to a single character)
    # ==============================================================================

    # The master database of all items that can exist in the game.
    items_database = {
        "MG41": {"type": "weapon", "weight": 10, "description": "A powerful machine gun..."},
        "Tissue": {"type": "junk", "weight": 2, "description": "A Tissue to wipe away your sorrows.."},
        "Wet Tissue": {"type": "junk", "weight": 2, "description": "A Wet Tissue...yuck!"},
        "Laser range finder": {"type": "tool", "weight": 1, "description": "Used to measure the distance..."},
        "Compass": {"type": "tool", "weight": 1, "description": "A military grade compass..."},
        "radio": {"type": "tool", "weight": 2, "description": "A military grade radio..."},
        "Classified Mission Sheet": {"type": "tool", "weight": 2, "description": "A sheet I should not have..."},
        "First aid kit": {"type": "consumable", "weight": 1, "description": "Used to heal minor injuries."},
        "Tactical flashlight": {"type": "tool", "weight": 1, "description": "This light can survive explosions..."},
        "Water Bottle": {"type": "consumable", "weight": 1, "description": "Used to hold water..."},
        "sissor": {"type": "tool", "weight": 1, "description": "Used to cut things."},
        "Report 001": {"type": "document", "weight": 300, "description": "A report of something..."},
        "Pistol": {"type": "weapon", "weight": 2, "description": "A standard issue sidearm..."}
    }

    # The master database of what medkit items can do.
    medkit_contents = {
        "Bandage": {"conditions": ["bleeding", "cut"], "healing": 10},
        "Phenergan": {"conditions": ["nausea"], "healing": 5},
        "Antibiotics": {"conditions": ["infection"], "healing": 20},
        "Morphine": {"conditions": [], "healing": 30},
        "Water Gel": {"conditions": ["burn"], "healing": 15},
        "Acetaminophen": {"conditions": [], "healing": 10},
        "Diphenhydramine": {"conditions": ["pain"], "healing": 10},
        "SOFT-T": {"conditions": ["hemorrhage", "fracture", "bleeding"], "healing": 10},
        "Naproxen": {"conditions": ["headache"], "healing": 10}
    }

    # A global utility function for adding new items to the medkit database.
    def add_item_to_medkit(item_name, healing_info):
        medkit_contents[item_name] = healing_info
        renpy.notify(f"{item_name.capitalize()} has been added to your medkit!")


    # ==============================================================================
    # 2. INVENTORY CLASS (Must be defined BEFORE GameCharacter)
    # ==============================================================================
