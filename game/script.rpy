# name of the character.
#extra
default rng = random.randint(1,100)
default menu_initialized = False
transform half_size: 
    zoom 0.5 
image bootcampinsideprojectorroomstartm = Movie(size=(1280, 755),zoom = 1,play="images/movie_background.webm")
# Chara
define BAG = Character("Bagman",color="#b66c12")
define BAL = Character("Baldi")
define BEN = Character("Benjamin")
define BON = Character("Bonehead")
define DAV = Character("David")
define DEE = Character("Deerik")
define DOM = Character("Domonic")
define DRI = Character("Drill Sarg",color="#12a3b6")
define JES = Character("Jesus")
define MAR = Character("Marc")
define MEO = Character("Meowbahh")
define MIK = Character("Mike")
define MAR = ("Marc")
define MYS = Character("Mystery Man")
define PLA = Character("Placeholder")
define PRE = Character("President")
define SAM = Character("Samuel",color="#b66c1261")
define SIM = Character("Sim")
define SUL = Character("Sultan",color="#aeadb7")
define ZUN = Character("Zundamon",color="#B9D08B")
define Q = Character ("?????",color="#0000FF")
define Q2 = Character ("?????",color="#8fe406ff")
define Q3 = Character ("??????",color="#14a122")
define Q4 = Character ("???????",color="#97239e")
define k =Character("Keemstar",color="#0000FF")

# Default inventory with some items as string names
default left_arm_item = None
default right_arm_item = None
default title_screen_set = False
default body_armor_item = None  
default hud_visible = True  # Start with the HUD visible
default talked_to_labatory = False
default slot_count = 1
default current_character_index = 0 
#Quests
default new_uniform_quest = False #quest to get new uniform
default projectorquest = False
default uniform_ordered = False
default projector_obtained = False
#Relations
default bagman_r = 0
default sultan_r = 0
default samuel_r = 0
#Room Triggers
default visted_outside_projector_room = False
default visted_outside_closet_room = False
default visited_elevator = False

default visited_stairwell = False
default skiped_samuel = True

# The game starts here.RR
default npc_name = "???"         # The default NPC name
default npc_mood = "Normal"      # The default NPC mood
default npc_attitude = "Neutral" # The default NPC attitude

#jump bootcampinsideprojectorroomstart
#radio
# Variables to track stats and experience (to be defined in init or elsewhere)

#pytrhon
init python:
    import webbrowser
    import random   
    import time      
    minhealth = 0
    maxhealth = 100
    full_weight = 0
    current_selected_character = "Ben"
    current_strength = random.randint(36,45)  
    max_space = 10 + current_strength     
    current_sanity = 100
    crafting_items = []
    selected_items = []
    mixed_liquids = []    
    selected_liquids = []   
    holding_items = ["Tape", "Glue", "Screwdriver"]
    liquid_inventory = [
    #   {"name": "Water", "amount": 100},    # 100 units of water
    #   {"name": "Ethanol", "amount": 50},   # 50 units of ethanol
    #   {"name": "Oil", "amount": 30},       # 30 units of oil
    # {"name": "Glue", "amount": 30}
    ]   
    default_status = {
        "head": {"status": "fine", "health": 100, "conditions": [], "temperature": 70},
        "body": {"status": "fine", "health": 100, "conditions": [], "temperature": 70},
        "left_arm": {"status": "fine", "health": 100,  "conditions": [], "temperature": 70},
        "right_arm": {"status": "fine", "health": 100,  "conditions": [], "temperature": 70},
        "left_leg": {"status": "fine", "health": 100,  "conditions": [], "temperature": 70},
        "right_leg": {"status": "fine", "health": 100,  "conditions": [], "temperature": 70}
    }

    stats = {
        "intelligence": {"level": 2, "current_xp": 0, "max_xp": 77, "current_value": 10},
        "speech": {"level": 3, "current_xp": 0, "max_xp": 131, "current_value": 14},
        "strength": {"level": 5, "current_xp": 0, "max_xp": 230, "current_value": current_strength},
        "luck": {"level": 1, "current_xp": 0, "max_xp": 50, "current_value": 15},
        "speed": {"level": 2, "current_xp": 0, "max_xp": 87, "current_value": 14},
        "pain_tolerance": {"level": 2, "current_xp": 0, "max_xp": 90, "current_value": 10},
        "mental_resilience": {"level": 1, "current_xp": 0, "max_xp": 50, "current_value": 10},
        "medical": {"level": 1, "current_xp": 0, "max_xp": 50, "current_value": 10},
        "sanity": {"current_sanity": current_sanity}
        }    
     
    container_inventory = [
    #    {"name": "Water Bottle", "capacity": 500, "current_amount": 0, "contents": []},  # Empty bottle
    ]      
    selected_holding_item = None
    selected_container = None       
    liquid_mix_recipes = {
        "Cleaning Solution": {"Water": 90, "Ethanol": 10},
        "Emulsion": {"Oil": 50, "Water": 50},
        "Slime": {"Water": 100, "Glue": 30},
    }
    def has_level(stat_name, level):
        if stat_name in stats:
            return stats[stat_name]["level"] == level
        return False  

    # Crafting Recipes
    crafting_recipes = {
        ("Laser range finder", "Tactical flashlight"): {"result": "Laser Tactical Kit", "holding_item": "Glue"},
        ("Compass", "radio"): {"result": "Navigation Radio", "holding_item": "Screwdriver"}
    }
    def add_crafting_item(item):
        if len(crafting_items) < 2:
            crafting_items.append(item)
            renpy.notify(f"{item} added to crafting box.")
        else:
            renpy.notify("You can only combine two items.")
#    
    def check_all_containers_for_liquid(liquid_name):
        found = False  # Flag to indicate if the liquid was found
        for container in container_inventory:
            # Check if the container has any contents
            if container["contents"]:
                for content in container["contents"]:
                    if content["name"] == liquid_name:
                        renpy.notify(f"{container['name']} contains {liquid_name} ({content['amount']} ml).")
                        found = True
                        # Specific check for cleaning solution
                        if liquid_name == "Cleaning Solution":
                            renpy.notify("Clean in the console.")
            else:
                renpy.notify(f"{container['name']} is empty.")

        # If the liquid was not found in any container
        if not found:
            renpy.notify(f"No containers contain {liquid_name}.")

#

    def remove_crafting_item(item):
        if item in crafting_items:
            crafting_items.remove(item)
            renpy.notify(f"{item} removed from crafting box.")
#
    def drop_item(item):
        global crafting_items
        if len(crafting_items) < 2:  # Allow only two items to be dropped
            crafting_items.append(item)
            renpy.notify(f"{item} added to crafting box.")
        else:
            renpy.notify("You can only craft with two items.")
#
    def remove_item(item):
        if item in selected_items:
            selected_items.remove(item)
#
    def select_item(item):
        if item not in selected_items and len(selected_items) < 2:  # Allow only two selections
            selected_items.append(item)
#
    def add_liquid(liquid_name):
        for liquid in liquids:
            if liquid["name"].lower() == liquid_name.lower():
                liquid["amount"] += 10  # Change this value as needed
                renpy.notify(f"You added 10 {liquid_name}.")
                return
        renpy.notify(f"{liquid_name} not found.")
#
    def drain_liquid(container, liquid_name):
        """
        Drain 10 ml of the specified liquid from the container.
        """
        for content in container["contents"]:
            if content["name"] == liquid_name:
                if content["amount"] >= 10:
                    content["amount"] -= 10
                    container["current_amount"] -= 10
                    if container["current_amount"] < 0:
                        container["current_amount"] = 0
                    renpy.notify(f"Drained 10 ml of {liquid_name}.")
                else:
                    renpy.notify(f"Not enough {liquid_name} to drain. Current amount: {content['amount']} ml.")
                return
        renpy.notify(f"{liquid_name} is not in the container.")

#
    def remove_holding_item(holding_item):
        global holding_items, selected_holding_item  # Ensure global access to holding_items

        # Only remove if the holding_item is the selected one
        if holding_item == selected_holding_item and holding_item in holding_items:
            holding_items.remove(holding_item)  # Remove the item from the holding items list
            renpy.notify(f"You have removed {holding_item} from holding items.")
            selected_holding_item = None  # Clear selection after removal
        else:
            renpy.notify("You need to select an item to remove.")
    def adjust_liquid_amount(liquid_name, adjustment):
        # Find the liquid in the player's available liquids inventory
        for liquid in liquids:
            if liquid["name"] == liquid_name:
                new_amount = liquid["amount"] + adjustment
    
                # Ensure the new amount doesn't exceed available or go below 0
                if adjustment > 0:
                    if new_amount > liquid["amount"]:
                        new_amount = liquid["amount"]  # Limit to available amount
                elif adjustment < 0:
                    if new_amount < 0:
                        new_amount = 0  # Prevent negative amounts
    
                # Update the selected amount in `selected_liquids`
                for selected in selected_liquids:
                    if selected["name"] == liquid_name:
                        selected["amount"] = min(new_amount, liquid["amount"])
                        break
                else:
                    # If liquid is not yet selected, add it with the new amount
                    if new_amount > 0:
                        selected_liquids.append({"name": liquid_name, "amount": new_amount})
    
                # Update the player's inventory with the new available amount
                liquid["amount"] = max(liquid["amount"] - adjustment, 0)
                break
    
    def check_mix_recipe(container):
        """
        Check if the container's contents match any mix recipe.
        Returns the name of the created item if a match is found, otherwise returns None.
        """
        # Create a dictionary to store the container's current liquid composition
        container_composition = {liquid["name"]: liquid["amount"] for liquid in container["contents"]}

        # Iterate through the mix recipes to find a match
        for result_item, recipe in liquid_mix_recipes.items():
            match = True
            for liquid_name, required_amount in recipe.items():
                if liquid_name not in container_composition or container_composition[liquid_name] != required_amount:
                    match = False
                    break

            # If all conditions of the recipe are met, return the result
            if match:
                return result_item
            
        # If no match is found, return None
        return None
    def initialize_stats():
        for stat in stats:
            if stat != "sanity":
                stats[stat]["current_value"] = calculate_stat_value(stats[stat]["level"])
                stats[stat]["current_xp"] = calculate_stat_value(stats[stat]["level"])

    def calculate_stat_value(level):
        for stat in stats:
            return level * random.randint(1, 4) + random.randint(1, 4) + stats[stat]["current_value"] 

    initialize_stats()

    def add_liquid_to_selected(liquid):
        """
        Add liquid to the selected_liquids list for combining.
        """
        if liquid["amount"] > 0:
            selected_liquids.append({"name": liquid["name"], "amount": liquid["amount"]})
            renpy.notify(f"Added {liquid['name']} to mix.")
        else:
            renpy.notify(f"No {liquid['name']} available.")
    def combine_liquids(container, selected_liquids):
        """
        Combine selected liquids into a container and check if any mix recipes are satisfied.
        """
        # Check if a container is selected
        if not container:
            renpy.notify("Please select a container.")
            return

        # Calculate the total amount of liquid being added
        total_liquid = sum(liquid["amount"] for liquid in selected_liquids)
        available_space = container["capacity"] - container["current_amount"]

        # Check if the container has enough space for all selected liquids
        if total_liquid > available_space:
            renpy.notify(f"Not enough space in {container['name']}. Only {available_space} units left.")
            return

        # Add each liquid to the container
        for liquid in selected_liquids:
            if liquid["amount"] > 0:
                # Check if the liquid is already present in the container
                liquid_exists = False
                for content in container["contents"]:
                    if content["name"] == liquid["name"]:
                        content["amount"] += liquid["amount"]
                        liquid_exists = True
                        break

                # If the liquid is not in the container, add it
                if not liquid_exists:
                    container["contents"].append({"name": liquid["name"], "amount": liquid["amount"]})

                # Reduce the liquid amount in the inventory
                for inv_liquid in liquid_inventory:
                    if inv_liquid["name"] == liquid["name"]:
                        inv_liquid["amount"] -= liquid["amount"]
                        if inv_liquid["amount"] < 0:
                            inv_liquid["amount"] = 0

                # Update the current amount in the container
                container["current_amount"] += liquid["amount"]

        # Check if the contents match a recipe
        result_item = check_mix_recipe(container)
        if result_item:
            # Clear the contents and replace it with the new item
            container["contents"].clear()
            container["current_amount"] = 0
            container["contents"].append({"name": result_item, "amount": container["capacity"]})
            add_experience("intelligence", 1)
            renpy.notify(f"Success! You created {result_item} in the {container['name']}.")
        else:
            renpy.notify(f"You can not mix these together.")

        # Clear the selected items after combination
        selected_liquids.clear()

    def add_liquid_to_mixture(liquid_name, amount):
        amount = int(amount)
        if amount <= 0:
            renpy.notify("Please enter a valid amount.")
            return

        for liquid in liquids:
            if liquid["name"] == liquid_name and liquid["amount"] >= amount:
                selected_liquids.append({"name": liquid["name"], "amount": amount})
                renpy.notify(f"Added {amount} of {liquid_name} to the mixture.")
                return

        renpy.notify("Not enough liquid or invalid amount.")

    def combine_items():
        global crafting_items, selected_items, liquid_inventory  # Include liquid_inventory
    
        # Check if exactly two items are selected
        if len(selected_items) != 2:
            renpy.notify("You need exactly two items to combine.")
            return
        
        item_tuple = tuple(sorted(selected_items))  # Sort to match recipe keys
        print(f"Combining items: {item_tuple}")  # Debugging: print the item_tuple
    
        if item_tuple in crafting_recipes:
            holding_item = crafting_recipes[item_tuple]["holding_item"]
            print(f"Holding item: {holding_item}")  # Debugging: print the holding item
    
            # Check if glue is being used as the holding item
            if holding_item == "Glue":
                # Ensure that glue is in inventory if it is required
                glue_amount = next((liquid["amount"] for liquid in liquid_inventory if liquid["name"] == "Glue"), 0)
    
                if glue_amount > 0:
                    new_item = crafting_recipes[item_tuple]["result"]
                    inventory.append(new_item)  # Add new item to inventory
    
                    # Remove items from inventory that were used in crafting
                    for item in selected_items:
                        inventory.remove(item)  # Remove the used items
    
                    # Decrease glue amount without removing it unless it's empty
                    for liquid in liquid_inventory:
                        if liquid["name"] == "Glue":
                            liquid["amount"] -= 10  # Decrease glue amount by 10 (or the required amount)
                            if liquid["amount"] <= 0:
                                inventory.remove("Glue")  # Remove glue from inventory if amount is zero
                                renpy.notify("You have used your last Glue.")
                            break
    
                    renpy.notify(f"You crafted: {new_item} using Glue.")
                    selected_items.clear()  # Clear selected items after successful crafting
                else:
                    renpy.notify("You need Glue to hold the items together.")
            else:
                # If glue is not the holding item
                if holding_item in inventory:
                    new_item = crafting_recipes[item_tuple]["result"]
                    inventory.append(new_item)  # Add new item to inventory
    
                    # Remove items from inventory that were used in crafting
                    for item in selected_items:
                        inventory.remove(item)  # Remove the used items
    
                    renpy.notify(f"You crafted: {new_item} using {holding_item}.")
                    selected_items.clear()  # Clear selected items after successful crafting
                else:
                    renpy.notify(f"You need {holding_item} to hold the items together.")
        else:
            renpy.notify("These items cannot be combined.")
            print(f"Item tuple {item_tuple} not found in crafting recipes.")  # Debugging: recipe not found
    
#
    def get_liquid_amount(liquid_name):
        for liquid in liquids:
            if liquid["name"].lower() == liquid_name.lower():
                return liquid["amount"]
        return 0

    # Function to use a specific amount of liquid
    def use_liquid(liquid_name, amount):
        for liquid in liquids:
            if liquid["name"].lower() == liquid_name.lower():
                if liquid["amount"] >= amount:
                    liquid["amount"] -= amount
                    return True
                else:
                    return False  # Not enough liquid
        return False  # Liquid not found

#
    def select_holding_item(item):
        global holding_item
        holding_item = item
        renpy.notify(f"You selected {item} as the holding item.")
    def remove_item_by_name(inventory, item_name):
        inventory[:] = [item for item in inventory if item.get("name") != item_name]

   
    def update_status(default, new):
        for key in new:
            if key in default:
                default[key] = new[key]    
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
    def change_temperature(body_part, new_temperature):
        if body_part in default_status:
            default_status[body_part]['temperature'] = new_temperature


    def level_up(stat_name):
        if stat_name in stats:
            stats[stat_name]["level"] += 1

            stats[stat_name]["current_xp"] = 0
            stats[stat_name]["max_xp"] = round(stats[stat_name]["max_xp"] + random.randint(10, 35) ) 
            stats[stat_name]["current_value"] += random.randint(1, 8)
    def set_random_title_screen():
        global title_screen_set  

        if not title_screen_set:
            title_screen_set = True  
            play_title_screen_music(selected_screen)
            return selected_screen["image"]
        else:
            return selected_screen["image"]
    def play_title_screen_music(selected_screen):
        global title_screen_set  

        if title_screen_set:
            return  
        if selected_screen["music"]:
            selected_music = random.choice(selected_screen["music"])
            renpy.music.play(selected_music, loop=True)

        if selected_screen.get("fade_out"):
            renpy.pause(2)  
            renpy.hide(selected_screen["image"], transition=dissolve)

    def add_temperature(part, amount):
        """Increase the temperature of a specified body part."""
        if part in default_status:
            default_status[part]['temperature'] += amount
            check_temperature(part)
        else:
            print(f"'{part}' is not a valid body part.")

    def remove_temperature(part, amount):
        """Decrease the temperature of a specified body part."""
        if part in default_status:
            default_status[part]['temperature'] -= amount
            check_temperature(part)
        else:
            print(f"'{part}' is not a valid body part.")

    def check_temperature(part):
        """Check the temperature of a specified body part and update status if needed."""
        temp = default_status[part]['temperature']
        if temp > 90:
            default_status[part]['status'] = "overheated"
            add_condition(part, "overheating")
        elif temp < 45:
            default_status[part]['status'] = "hypothermia"
            add_condition(part, "hypothermia")
        else:
            default_status[part]['status'] = "fine"
            if "overheating" in default_status[part]['conditions']:
                default_status[part]['conditions'].remove("overheating")
            if "hypothermia" in default_status[part]['conditions']:
                default_status[part]['conditions'].remove("hypothermia")

    title_screens = [
        {
            "image": "images/bg/Title Screen/Title_Screen.png",
            "music": ["audio/Music/showtime.mp3"]
        },
        {
            "image": "images/bg/Title Screen/Titlescreen2.png",
            "music": ["audio/Music/openingact.mp3", "audio/Music/creep.mp3"]
        },
        {
            "image": "images/bg/Title Screen/alternatetitleone.png",
            "music": ["audio/Music/sock.mp3", "audio/Music/Introsong.wav"]
        },
        {
            "image": "images/bg/Title Screen/detailedtitle.png",
            "music": ["audio/Music/IntroTheme3.mp3", "audio/Music/IntroTheme1.mp3", "audio/Music/openingactone.mp3"]
        }
    ]
#
    selected_screen = random.choice(title_screens)      
    def is_stat_higher(stat_name, stat_to_compare, stats):
        if stat_name in stats:
            current_value = stats[stat_name]["current_value"] 
            return current_value > stat_to_compare 
        else:
            raise ValueError(f"Stat '{stat_name}' not found in stats.")

#
    def set_npc(name, mood, attitude):
        global npc_name, npc_mood, npc_attitude
        npc_name = name
        npc_mood = mood
        npc_attitude = attitude
    def add_condition(part, new_condition):
        global default_status
        global maxhealth
        maxhealth = maxhealth - 10
        remove_health(part, 10)
        if part in default_status:
            if new_condition not in default_status[part]["conditions"]:
                default_status[part]["conditions"].append(new_condition)        
    def remove_health(part, amount):

        global default_status
        if part in default_status:
            default_status[part]["health"] = max(default_status[part]["health"] - amount, minhealth)

            if default_status[part]["health"] == 0 and part == "head":
                renpy.jump("gameover")  
    def set_level(stat_name, new_level):
        if stat_name in stats:
            stats[stat_name]["level"] = new_level
            print(f"{stat_name.capitalize()} level set to {new_level}")
        else:
            print(f"Stat {stat_name} does not exist.")

    # Function to set the current XP of a specific stat
    def set_current_value(stat_name, attribute_name, new_value):
        if stat_name in stats:
            if attribute_name in stats[stat_name]:
                stats[stat_name][attribute_name] = new_value
                print(f"{stat_name.capitalize()}: {attribute_name} set to {new_value}")
            else:
                print(f"Attribute {attribute_name} does not exist in {stat_name}.")
        else:
            print(f"Stat {stat_name} does not exist.")


    # Function to set the max XP of a specific stat
    def set_max_xp(stat_name, new_max_xp):
        if stat_name in stats and "max_xp" in stats[stat_name]:
            stats[stat_name]["max_xp"] = new_max_xp
            print(f"{stat_name.capitalize()} max XP set to {new_max_xp}")
        else:
            print(f"Stat {stat_name} does not exist or cannot have max XP.")

    def remove_condition(part, condition):
        global default_status
        global maxhealth
        maxhealth = maxhealth + 10
        add_health(part, 10)

        if part in default_status:
            default_status[part]["conditions"] = [c for c in default_status[part]["conditions"] if c != condition]
    def remove_health(part, amount):
        global default_status
        if part in default_status:
            default_status[part]["health"] = max(default_status[part]["health"] - amount, minhealth)
    def has_condition(part, condition):
        global default_status
        if part in default_status:
            return condition in default_status[part]["conditions"]
        return False
    def add_health(part, amount):
        global default_status
        global maxhealth
        maxhealth = maxhealth  
        if part in default_status:
            default_status[part]["health"] = min(default_status[part]["health"] + amount, maxhealth)
        renpy.notify(f"{part.replace('_', ' ').capitalize()} health restored by {amount} points.")


    def htmlopen(name):
        # Use an f-string to correctly format the file path
        renpy.notify("Your web browser has been opened.")
        html_file_path = renpy.loader.transfn(f"htmls/{name}.html")
        webbrowser.open(f"file:///{html_file_path}")
    def has_item(item):
        return item in inventory
    def get_armor_details(armor_item):
        return armor_item["description"]    
    def add_item_to_medkit(item_name, healing_info):

        global medkit_contents

        # Add the item to the medkit with its healing properties
        medkit_contents[item_name] = healing_info

        # Notify the player that the item was added
        renpy.notify(f"{item_name.capitalize()} has been added to your medkit!")

    def use_medkit_item(part, item):

        global default_status, medkit_contents , maxhealth

        # Check if the item exists in the medkit
        if item not in medkit_contents:
            renpy.notify(f"You don't have {item.capitalize()} in the medkit!")
            return

        # Get the item's healing info (conditions it heals and health recovery)
        healing_info = medkit_contents.get(item, {})
        conditions_to_heal = healing_info.get("conditions", [])
        health_recovery = healing_info.get("healing")

        # Heal specific conditions if they exist on this part
        for condition in conditions_to_heal:
            if condition in default_status[part]["conditions"]:
                default_status[part]["conditions"].remove(condition)
                if maxhealth < 100:
                    maxhealth = maxhealth + 10
        # Heal health for the part
        add_health(part, health_recovery)
        del medkit_contents[item]

        # Notify the player of the healing action
        renpy.notify(f"Used {item.capitalize()} on {part.replace('_', ' ')} and it was fuuly used...")


    current_space_taken = 0  # Tracks the total weight of items in the inventory
    inventory = []
    left_arm_item = None
    right_arm_item = None
    def calculate_total_weight():
        """Calculate the total weight of items in the inventory."""
        total_weight = sum(get_item_weight(item) for item in inventory)
        total_weight += sum(item['weight'] for item in armor_inventory if item['name'] == body_armor_item)
        return total_weight

    def get_remaining_space():
        """Get the remaining space in the inventory based on item count."""
        return max_space - len(inventory)  # Space based on the number of items

    def ToggleScreenVisibility():
        global hud_visible
        hud_visible = not hud_visible  # Toggle between True and False

    def prompt_for_removal(message):
        """Prompt the player to remove an item."""
        renpy.notify(message)
        renpy.call_innew_context("prompt_remove_item")  # Call a new screen to handle item removal

    def update_inventory(item, action):
        """Update the inventory based on adding or removing items."""
        item_weight = get_item_weight(item)
        global current_space_taken

        if action == "add":
            if len(inventory) >= max_space:
                prompt_for_removal("Your backpack is full. You need to remove an item before adding more.")
                return False

            if calculate_total_weight() + item_weight > current_strength:
                prompt_for_removal("You cannot carry more weight. You need to remove an item before adding more.")
                return False

            inventory.append(item)
            current_space_taken += item_weight  # Add the weight of the item
        elif action == "remove":
            if item in inventory:
                inventory.remove(item)
                current_space_taken -= item_weight  # Subtract the weight of the item
        return True

    def label_callback(name, abnormal):
        store.last_label = name
    config.label_callback = label_callback
    def reduce_durability(armor_name, damage):
        """Reduce the durability of a specified armor."""
        global body_armor_item  # Ensure we can modify the equipped armor item

        if body_armor_item == "No Armor":
            renpy.notify("No armor is equipped, no durability reduction applied.")
            return  # Exit the function if no armor is equipped

        for item in armor_inventory:
            if item['name'] == armor_name:
                item['durability'] -= damage  # Reduce durability by damage amount
                if item['durability'] <= 0:
                    item['durability'] = 0  # Set durability to zero
                    body_armor_item = "No Armor"  # Set equipped armor to "No Armor"
                    renpy.notify(f"{armor_name} is damaged and can no longer be equipped.")
                else:
                    # Notify about the remaining durability
                    renpy.notify(f"{armor_name} durability reduced to {item['durability']}.")
                return  # Exit the function after processing

        # If armor name is not found, you can add a notification if desired
        renpy.notify(f"{armor_name} not found in inventory.")

# Example of gaining experience (you can adjust this function based on game events)
    def add_experience(stat_name, amount):
        stats[stat_name]["current_xp"] += amount
        if stats[stat_name]["current_xp"] >= stats[stat_name]["max_xp"]:
            stats[stat_name]["current_xp"] = stats[stat_name]["max_xp"] # Cap XP at max if it exceeds

    def get_item_weight(item):
        """Return the weight of an item."""
        item_weights = {
            "MG41": 10,
            "Laser range finder": 1,
            "Compass": 1,
            "radio": 2,
            "First aid kit": 1,
            "Tactical flashlight": 1,
            "Water Bottle": 1,
            "sissor": 1,
            "Report 001": 300
        }
        return item_weights.get(item, 1)  # Default weight if not specified
    armor_inventory = [
        {'name': 'Type 07', 'description': 'Lightly Worn.', 'weight': 3,"durability": 150 },
        {'name': 'No Armor', 'description': 'No Effects.', 'weight': 0,"durability": maxhealth }
        ]
    def get_item_description(item):
        """Return the description of an item."""
        item_descriptions = {
            "Report 001": "A report of something? I don't remember what it is for. It's very important.",
            "MG41": "A powerful machine gun. There are many like it but this one is mine.",
            "Laser range finder": "Used to measure the distance from here to a target.",
            "Compass": "A military grade compass used for navigation.",
            "radio": "A military grade radio used for communication. Is only able to communicate with military units and HQ.",
            "First aid kit": "Used to heal minor injuries.",
            "Tactical flashlight": "This light can survive explosions and runs on solar battery.",
            "sissor": "Used to cut things.",
            "Water Bottle": "Used to hold water. Can hold up to 500ml of water...or any other liquid for that matter."
        }
        return item_descriptions.get(item, "No description available.")
    def equip_item(arm, item):
        """Equip an item to the specified arm, with checks for inventory space and weight."""
        global left_arm_item, right_arm_item, body_armor_item, current_strength, current_space_taken, max_space

        if get_remaining_space() < 0:
            renpy.notify("Your inventory space is negative.. How did you even do this?")
            return

        if calculate_total_weight() > current_strength:
            renpy.notify("You cannot carry more weight. Remove some items to reduce the weight.")
            return

        # Equip items if conditions are met
        if item in ["MG41", "Laser range finder"]:  # Two-handed items
            if left_arm_item or right_arm_item:
                renpy.notify("Both arms must be free to equip a two-handed item.")
            else:
                left_arm_item = item
                right_arm_item = item
        else:
            if arm == "left":
                left_arm_item = item
            elif arm == "right":
                right_arm_item = item
            elif arm == "body":  
                body_armor_item = item

        renpy.hide_screen("item_select")
    def unequip_item(arm):
        """Unequip an item from the specified arm."""
        global left_arm_item, right_arm_item
        if arm == "left":
            if left_arm_item == right_arm_item:
                left_arm_item = None
                right_arm_item = None
            else:
                left_arm_item = None
        elif arm == "right":
            if right_arm_item == left_arm_item:
                left_arm_item = None
                right_arm_item = None
            else:
                right_arm_item = None
        renpy.restart_interaction()
    def discard_item(arm):
        global left_arm_item, right_arm_item, inventory, container_inventory
        item_to_discard = None

        if arm == "left":
            item_to_discard = left_arm_item
            left_arm_item = None  # Clear left arm item after deciding
        elif arm == "right":
            item_to_discard = right_arm_item
            right_arm_item = None  # Clear right arm item after deciding

        # Check if the item to discard is valid
        if item_to_discard:
            # Remove from player's inventory if it exists
            if item_to_discard in inventory:
                inventory.remove(item_to_discard)

            # Check against container_inventory and remove if found
            for container_item in container_inventory:
                if container_item["name"] == item_to_discard:
                    container_inventory.remove(container_item)  # Remove the item from container_inventory
                    break  # Exit the loop after removing the item

        renpy.restart_interaction()  # Restart the interaction after discarding the item

    # Function to add liquid to the inventory
    def add_liquid(liquid_name, amount):
        for liquid in liquid_inventory:
            if liquid["name"] == liquid_name:
                liquid["amount"] += amount
                break

    def remove_liquid(liquid_name, amount):
        for liquid in liquid_inventory:
            if liquid["name"] == liquid_name:
                if liquid["amount"] >= amount:  
                    liquid["amount"] -= amount
                else:
                    renpy.notify("Not enough liquid available.")
                break
    def use_item(item):
        """Handle the use of an item from the inventory."""
        global inventory, last_label

        if item == "First aid kit":
            renpy.show_screen("heal_menu")   
            inventory.remove("First aid kit")
        elif item == "Cleaning Solution":
            renpy.notify("Nothing to clean.")
        elif item == "Oil":
            renpy.notify("You cover yourself with oil.")        
        elif item == "Tactical flashlight":
            renpy.notify("This area is not THAT dark is it?")
        elif item == "radio":
            renpy.notify("*Listening to radio...")
            renpy.sound.play("audio/radio/radio.wav")

        if item == "radio" and last_label == "stairwell" and not visited_stairwell and rng < 50:
            renpy.notify("*Signal Received Replaying..*")
            renpy.sound.play("audio/radio/radio02.mp3")
        elif item == "Laser range finder":
            renpy.notify("Nothing to measure here.")
        elif item == "MG41":
            if last_label == "laboratory":
                renpy.notify("It is not nice to use weapons in the laboratory.")
            else:
                renpy.notify("You probably shouldn't use this here.")
        elif item == "compass":
            if last_label == "laboratory":
                renpy.notify("You use the compass and it spins. It seems like there is some electromagnetic interference here.")
            elif last_label == "outsideprojectorroom":
                renpy.notify("The compass points north.")
            elif last_label == "outsideclosetroom":
                renpy.notify("The compass points west.")  
            elif last_label == "outsidecaferoom":
                renpy.notify("The compass points south west.")                     
            else:
                renpy.notify("You use the compass, but it doesn't seem to give any useful information in this place.")
#    $ remove_condition(head, concussion)
#    $ remove_condition(head, Amnesia)    
#    $ add_condition("head", "concussion")
#    $ add_condition("head", "minor brain damage")
#    $ inventory.append("MG41")    
#    $ inventory.append("compass")
#    $ inventory.append("Laser range finder")
#    $ inventory.append("First aid kit")
#    $ inventory.append("radio")
#    $ inventory.append("Tactical flashlight")
#    if is_stat_higher("intelligence", 4, stats):
#       "Intelligence is higher than 4!"   
#     $ add_condition ("head", "headache")
#    $ inventory.append("compass")
#    $ inventory.append("Laser range finder")
#    $ inventory.append("First aid kit")
#    $ inventory.append("radio")
#    $ inventory.append("Tactical flashlight")
#    $ inventory.append("MG41")
#    $ inventory.append("Medical Dictionary")
label gameover:
    "You have died..."
    "Why don't you try loading a save..."
label start:
    hide screen character_selection
    $ rng = random.randint(1,100)
    show screen HUD    
    $ add_experience("mental_resilience", 9999)
    $ equip_item("body", "Type 07")
    jump bootcampinsideprojectorroomstart
    scene bg mayor
    play sound buzzer
    Q "Come in."
    play sound door
    pause 4
    show bg mayormeeting
    Q "You must be the courier..."  
    play sound slide
    show bg mayorhandoff
    pause 0.3
    scene bg mayorframe1
    pause 0.3
    scene bg mayorframe2
    pause 0.3
    scene bg mayorframe3
    pause 0.3
    scene bg mayorframe4
    pause 0.3
    show bg mayormeeting

    Q "I assume you know why you are here..."
    Q "Hand over the report. Than leave.."
    menu:
        "Hand Over The Report":
            scene bg mayormeeting
            $ inventory.remove("Report 001")
            Q "Thank you."
            Q "That is all, you are dismissed."
            Q "..."
            Q2"..."
            Q "Is there something else you need?"
            Q2 "....actually..." 
            jump bootcampinsideprojectorroomstart 
        "Refuse to hand over item":
            "You look down at the report.."
            $ htmlopen("004")
            "You feel like your we browser opened..."
            Q "I see..."
            Q "I don't think you understand the rules of this place."
            Q2 "..."
            Q "Hand it over!"
            Q2 "..."
            Q "Gaurds! Get over here!"
            $ inventory.remove("Report 001")
            jump bootcampinsideprojectorroomstart 
label bootcampinsideprojectorroomstart:
    scene bootcampinsideprojectorroomstartm

    if rng < 50:
        play music marchingon volume 0.1
    if rng > 50:
        play music boot_camp volume 0.5
    show ben idle at left with dissolve 
    $ slot_count = 1 
    BEN "Reporting in sir!"
    BEN "..."
    BEN "..."
    BEN "Who the hell called me here anyway?"    
    label choicesbootcampprojectorroom:
        scene bootcampinsideprojectorroomstartm
        hide ben idle
        menu:
            "Talk to the drill sargent":
                if projectorquest == False:
                    show drillsarg normal at right
                    show ben idle at left
                    $ set_npc("Sargent Briggs", "Stern", "Unkown")
                    show screen conversation_screen
                    DRI "Ah you are finally here!"
                    BEN "I came as soon as I heard the announcement sir!"
                    DRI "I need your help fixing this damn thing"
                    BEN "..."
                    DRI "Here take a look"
                    show projector at truecenter
                    BEN "It is sparking"
                    DRI "You will not speak unless asked to you understand that dirtbag!"
                    hide projector
                    BEN "SIR! YES SIR!"
                    DRI "You will get a replacement projector from the supply closet and you will return to me!"
                    $ add_experience("speech", 1)
                    menu:
                        "SIR YES SIR":
                            $projectorquest = True
                            hide drillsarg normal
                            hide screen conversation_screen
                            jump choicesbootcampprojectorroom
                        "I am on it!":
                            $projectorquest = True
                            DRI "What the fuck did I just say to you private! Your lucky I don't beat your ass!"
                            hide drillsarg normal
                            hide screen conversation_screen
                            jump choicesbootcampprojectorroom
                if projectorquest == True:
                    show drillsarg normal at right
                    $ set_npc("Sargent Briggs", "Bold", "Unkown")
                    show screen conversation_screen
                    show ben idle at left
                    DRI "Did you get the projector?"
                    BEN "No sir"
                    DRI "Than get your ass down to the closet and get it out!"
                    BEN "Yes sir!"
                    hide drillsarg normal
                    hide screen conversation_screen
                    jump choicesbootcampprojectorroom

            "Talk to the man in the back seat":
                $ set_npc("Bag Man", "Neutral", "Angry")
                show ben idle at left
                show screen conversation_screen
                if bagman_r < 0: #talked to
                    show bag maskamn at right
                    BAG "Fuck off"
                    hide bag maskamn
                    BEN "Guess he is in a bad mood"
                    hide screen conversation_screen
                    jump choicesbootcampprojectorroom
                show bag maskamn at right
                BAG "What!"
                BEN "Calm down I did not even say anything yet."
                BAG "I lost my watch, do you have it?"
                BEN "Did you call me here?"
                BAG 'No!'
                BEN "Why would I have your watch?"
                BAG "Can you look for it, in your backpack?"
                BEN "My backpack?"
                BAG "Just go in it, click the backpack icon in the top left corner!"
                BEN "What the hell are you talking about?"
                BAG "Just give me your backpack!"
                BEN "What the hell, no!"
                BAG "If you don't want to help me, just go away..."
                hide bag maskamn
                hide ben idle
                BEN "He was friendly..."
                $ bagman_r = bagman_r - 1
                hide screen conversation_screen                
                jump choicesbootcampprojectorroom
            "Talk to the man in the front seat":
                $ set_npc("Bag Man", "Neutral", "Neutral")
                show ben idle at left
                show screen conversation_screen
                show sultan talking at right
                if sultan_r < -2:
                    SUL "..." 
                    hide sultan right    
                    hide screen conversation_screen                
                    jump choicesbootcampprojectorroom                    
                if sultan_r > 2:
                    SUL "You should be able to get a new uniform on the second level."
                    hide sultan right                    
                    hide screen conversation_screen                
                    jump choicesbootcampprojectorroom                    
                if sultan_r < 0: 
                    SUL "Hey sorry bro about the comment from earlier..."
                    $ add_experience("speech", 1)
                    menu:
                        "It is alright":
                            $sultan_r = sultan_r + 5
                            $ set_npc("Bag Man", "Neutral", "Normal")
                            hide sultan right
                            hide screen conversation_screen                
                            jump choicesbootcampprojectorroom     
                        "I am sorry too":
                            $sultan_r = sultan_r + 10
                            $ set_npc("Bag Man", "Neutral", "Calming Down")
                            SUL 'It is alright we all get pissed off sometimes bro.'
                            hide sultan right
                            hide screen conversation_screen                
                            jump choicesbootcampprojectorroom 
                        "Nah fuck off":
                            SUL 'Alright fuck you too bro.'
                            $sultan_r = sultan_r - 5
                            $ set_npc("Bag Man", "Neutral", "Very Angry")
                            hide sultan right         
                            hide screen conversation_screen                
                            jump choicesbootcampprojectorroom
                $ set_npc("Bag Man", "Angry", " Angry")
                SUL "So what do you need bro?"
                BEN "Was it you who called me here? The announcement said come to the projector room..."
                SUL "Nope, If it was anyone here it would be the sarg bro."
                BEN "Why are you not wearing any military uniform while on duty?"
                if body_armor_item != "No Armor":
                    SUL "Look at what your wearing. Do you really think that is the right uniform bro?"
                    BEN '...'
                    BEN "Your right, what the hell is this commie uniform!"
                    BEN "This has to be a mistake!"
                    SUL "Maybe you are just stupid bro."
                    BEN "..."
                    SUL "Yeah you are pretty stupid if you just put it on wihtout thikning bro."
                    SUL "Take it off right now! Go to your inventory and click on Equip Armor and equip no armor."
                    if body_armor_item = "No Armor":
                        SUL "Thank god, I got really upset there..."
                        SUL "Sorry about that"
                        BEN "Yeah..."
                        $ sultan_r = sultan_r + 1
                        hide screen conversation_screen                
                        jump choicesbootcampprojectorroom
                    if body_armor_item not "No Armor":
                        BEN "No Fuck off"
                        SUL "Fuck you too bro"
                        BEN "(I should order a new uniform at the desk.)"
                        $ sultan_r = sultan_r - 1
                        $ new_uniform_quest == True
                        hide sultan right
                        hide screen conversation_screen                
                        jump choicesbootcampprojectorroom 
                else:               
                    SUL "..."
                    SUL "I know bro..."
                    SUL "My shirt kinda got ripped up bro..."
                    BEN "How did it get ripped up?"
                    SUL "In my barracks it got caught on the bed railings bro."
                    SUL "I had to cut it off when I woke up bro."
                    BEN "You ripped off your shirt?"
                    SUL "No, I just cut it off. It is not fully ripped off bro"
                    SUL "I snuck some sissor into the barracks last night. I don't need them anymore bro"
                    BEN "You snuck in some sissor?"
                    SUL "Yeah I was going to get back at eric for messing up yesterday bro"
                    BEN "I can imagine..."
                    SUL "Here you go bro"
                    BEN "Huh- I don't need these"
                    SUL "Nah it is fine you can keep them bro"
                    $ inventory.append("sissor")
                    hide sultan right
                    hide screen conversation_screen                
                    jump choicesbootcampprojectorroom          
            "Leave" if projectorquest == True:
                jump outsideprojectorroom       
label outsideprojectorroom: #outside projector room
    hide movie
    if samuel_r == 0:
        "(If you have not figured it out already you can access your inventory on the top left.)"
        scene outsideprojector
    elif visted_outside_closet_room == True:
        scene outsideprojectorroomnosamuel
    else:
        scene outsideprojectorroomnosamuel
    
    if visted_outside_projector_room == False:
        stop music        
        play music eos volume 0.5 loop
    $ visted_outside_projector_room = True
    if samuel_r == 0:
        menu:
            "Move to the left":
                jump elevator
            "Move to the right":
                jump outsideclosetroom
            "Talk to Samuel" if samuel_r == 0:
                $ skiped_samuel = False
                scene outsideprojectorroomnosamuel
                show ben idle at left
                show samuel redbook at right
                $ set_npc("Samuel", "Neutral", "Tiered")
                show screen conversation_screen                
                BEN "What are you doing?"
                SAM "Huh?"
                BEN "Aren't you supposed to on mess duty?"
                SAM "Oh that, right. I was searching through that supply closet over there and this book fell on me. Figured id ask the sarg about it."
                BEN "Why the hell where you going through the supply closet?"
                SAM "Than I realized I was on mess duty so if I told him I would get scolled for it."
                SAM "I should probably go return it and than sneak back before anyone notices."
                BEN "..."
                SAM "Yeah so ill go do that, see ya!"
                BEN "..."
                $ samuel_r = samuel_r - 1
                $ set_npc("Samuel", "Angry", "Annoyed")
                hide samuel redbook
                hide screen conversation_screen                
                jump outsideprojectorroom
            "Go inside the projector room":
                hide screen conversation_screen                
                jump choicesbootcampprojectorroom
    else:
        label outsideprojectorroomns:
            menu:
                "Move to the left":
                    jump elevator
                "Move to the right":
                    jump outsideclosetroom
        label outsideclosetroom:
            scene storageroom
            if samuel_r != 0:
                show samuel redbook at right
            if visted_outside_closet_room == True:
                jump passcodemenuc1
                            
            BEN "I think this is were the projector film is located."
            BEN "I guess I should try opening the door."
            $ visted_outside_closet_room = True
            
            if samuel_r != 0:
                $ set_npc("Samuel", "Bored", "Annoyed")                
                show screen conversation_screen                
                SAM "What the hell is this?!"
                SAM "The door has a passcode, is this some kind of prank?"
                if skiped_samuel == True:
                    BEN "What are you doing here shouldn't you be on mess duty?"
                    SAM "Huh? Oh right, I was on mess duty. Anyway I need help opening this door"
                    BEN "(I need to get a projector inside of this room, I might as well help him.)"
                    BEN "Alright, I will see what I can do."
                    SAM "Thanks."
                if skiped_samuel == False:
                    BEN "You had to enter the password to open the door before didn't you?"
                    SAM "Nah it was left open..."
                hide screen conversation_screen
            label passcodemenuc1:  
                show ben idle at left  
                menu:
                    "Enter passcode":
                        $ psswrd = renpy.input("ENTER PASSCODE:")
                        $ psswrd = psswrd.strip()
                        if psswrd == "4596837":
                            BEN "It opened"
                        if psswrd == "800815" and samuel_r != 0:
                            $ set_npc("Samuel", "Bored", "Annoyed")                
                            show screen conversation_screen                               
                            SAM "Did you just type boobies as the password?"
                            BEN "I thought it was worth a shot"
                            hide screen conversation_screen
                        if psswrd == "43314" and samuel_r != 0:
                            $ set_npc("Samuel", "Bored", "Annoyed")                
                            show screen conversation_screen                                 
                            SAM "Did you just type hello? Can you actually try and saerch for the password"  
                            BEN "Alright ill go look for something.."
                            hide screen conversation_screen
                        if psswrd == "12345" and samuel_r != 0:
                            $ set_npc("Samuel", "Bored", "Annoyed")                
                            show screen conversation_screen                                 
                            SAM "This is getting annoying at this point. If your not taking this seriously you should just leave."
                            hide screen conversation_screen
    
                        if psswrd == "696969" and samuel_r == 0:
                            $ set_npc("Samuel", "Bored", "Annoyed")                
                            show screen conversation_screen                                 
                            SAM "..."
                            hide screen conversation_screen

                        else:
                            if talked_to_labatory == True:
                                $ set_npc("Samuel", "Bored", "Timid")
                                SAM "I got good news."
                                BEN "Huh?"
                                SAM "I got wifi access!"
                                BEN "Wifi Password? Don't they change that every week"
                                SAM "Yeah, check it out!"
                                show sam phonejack
                                "The number 136.228.116.222 is the IP address shown on screen"
                                BEN "Didn't you show me this before? Thanks..."

                            BEN "Looks like the password was wrong..."
                            if samuel_r != 0:
                                $ set_npc("Samuel", "Bored", "Annoyed")                
                                show screen conversation_screen                                   
                                SAM "I have been trying passwords ever since I got here, I don't think brute forcing the password will work."                          
                                hide screen conversation_screen
                                jump outsideclosetroom
                            jump outsideclosetroom
                    "Move To The Left":
                        hide screen conversation_screen
                        jump outsideprojectorroom
                    "Move To The Right":   
                        hide screen conversation_screen
                        jump outsidecaferoom
        label outsidecaferoom:
            scene bg outsidecafe
            show ben idle at left
            BEN "The cafe should be closed now..."
            menu:
                "Move To The Left":
                    jump outsideclosetroom
                "Move To The Right":   
                    jump laboratory
                "Enter Cafe":   
                    BEN "It's locked..."
                    jump outsidecaferoom                
        label laboratory:
            scene apple
            show ben idle at left    
                    
            if new_uniform_quest == True:
                BEN "The people at this desk probably can order me a replacement uniform too."
                BEN "Hello, I would like to order a new uniform, this one is not up to code."
                Q4 "Not up to code?"
                BEN "..."
                Q4 "Looks fine to me"
                BEN "..."
                Q4 "..."
                BEN "Just put in the order for a new one."
                Q4 "Alright, I will phone up... It's going on your tab though. (Your usually sposed to ask the main desk this not us)"
                BEN "Fine."
                Q4 "Go upstairs to pick up your new uniform. It should be their by the time you get upstairs."
                pause 1
                $ uniform_ordered = True
            if talked_to_labatory == False:
                $ samuel_r = samuel_r + 1
                BEN "Finally, the research and devlopment desk, they might have a projector like the sargent asked for."
                BEN "I better go closer to them so they can hear me better."
                hide ben idle
                show ben idle at center
                BEN "Do you have the keycard to the supply closet?"
                Q3 "Face us while you speak please."
                hide ben idle at center
                show ben back at center   
                Q4 "Can you come closer to us while you talk?" 
                BEN "Alright."
                Q3 "No no its fine, the farther you stand from here the less of your stupid face I have to see. Out with it."
                BEN "Do you have the password for the supply closet, it is locked."
                Q4 "Which Supply Closet? There a dozens on this site alone. You don't expect me to know which one you are talking about, do you?"
                BEN "The one to the hall on the left"
                Q3 "I might have some papers relating to the new password, I don't know it off the top of my head. Let me go find it."
                scene laboneman
                show ben back at center            
                Q4 "While my friend is gone do you have anything else to ask?"
                if rng < 50:
                    BEN "(I feel like I am missing something...)"
                    BEN "(Maybe I should talk to someone..)"
                BEN "Nothing else to do here"   
                pause 1
                scene apple
                show ben back at center            
                Q3 "Okay I am back, I got a few papers here."
                Q3 "Let me just sort through them."
                BEN "..."
                BEN "...."
                BEN "....."
                Q3 "Yeah I can't find anything..."
                BEN "Nothing?"
                Q3 "Yes. I will go but them back now."
                $ add_experience("speech", 1)
                menu:
                    "Ask to check them":
                        BEN "Can I see the papers anyway?"
                        Q3 "Sure let me lay them out for you."
                        $ htmlopen("003")                    
                        BEN "Thanks"
                        Q3 "Let me take these papers back, I would check upstairs they might have what you are looking for."
                    "Don't ask":
                        BEN "Nevermind"
                        Q3 "Okay.."
                        Q3 "I would check back upstairs, they might have a override password."
                BEN "Alright"
            $ talked_to_labatory = True
            if talked_to_labatory == True:
                BEN "I got everything done that I had to do here..."
                menu:
                    "Move To The Left":
                        jump outsidecaferoom
                    "Move To The Right":
                        jump stairwell
        label stairwell:
            scene bg staircase
            show ben idle at left
            if rng < 50:
                BEN "Huh? My radio is buzzing."
            BEN "I arrived at the loading and offloading site"
            if visited_stairwell == False:
                if talked_to_labatory == False:
                    BEN "It seems like there is construction going on here."
                    BEN "I could use the stairwell to go upstairs."
                    BEN "But why would I do that?"
                if talked_to_labatory == True:
                    BEN "They said to go upstairs, that someone else might have the password..."
                    BEN "Who the hell am I going to ask for a password?"
                    jump insidestairwell
                $ visited_stairwell = True
            if visited_stairwell == True:
                menu:
                    "Go Upstairs" if talked_to_labatory == True:
                        jump insidestairwell
                    "Move To The Left":
                        jump laboratory
                    "Move To The Right":
                        jump elevator
        label elevator:
            scene bg elevator
            if visited_elevator == False:
                BEN "This building only has two floors."
                BEN "The elevator is mainly for disabled people."
                BEN "Not that I ever saw someone use it for themselves..."
                if rng >= 75:
                    BEN "Lazy bastards."
            if talked_to_labatory == False:
                BEN "I should really work on getting the projector before going up stairs.."
                BEN "Although id be nice to get some sunlight here."
                $ liquid_inventory.append({"name": "Water", "amount": 300})
            menu:
                "Go Up Elevator" if talked_to_labatory == True:
                    "*Click*"
                    if visited_elevator == False:
                        BEN "Nothing happened"
                        BEN "I guess I should take the stairs."
                        $ remove_item_by_name(liquid_inventory, "Water")
                        $ visited_elevator = True
                    jump elevator
                "Move To The Right":
                    $ visited_elevator = True
                    $ remove_item_by_name(liquid_inventory, "Water")
                    jump outsideprojectorroom
                "Move To The Left":
                    $ visited_elevator = True
                    $ remove_item_by_name(liquid_inventory, "Water")
                    jump stairwell
                   
        label insidestairwell:
            scene bg storewaystairwellfixed
            BEN "Did I forget anything?"
        #  $ check_all_containers_for_liquid("Oil")
            BEN "Did I ask everyone I coud?" 
            menu:
                "Go back":
                    jump stairwell
                "Go Upstairs" if talked_to_labatory == True:
                    jump upstairsmilitaryentrance
        label upstairsmilitaryentrance:
                scene bg militaryentrance
                BEN "Finally some fresh air."
                BEN "Once I fix the projector we can finally get breifed on this mission."
                if uniform_ordered == True:
                    BEN "I should go to the left firsr."
                    
    return

#    $ inventory.append("MG41")
#    $ inventory.append("Broccoli")
#    $ inventory.append("Cabbage")
#    $ inventory.append("Pear")
#    $ inventory.append("Pepper")
#    $ inventory.append("Potato")
#    $ inventory.append("Pumpkin")
#    $ inventory.append("Lemon")
#    $ inventory.remove("Lemon")
#    "$ inventory.remove('Lemon')"

#    return
#label Forest:
#    show Forest
#    "Alright, let's put our newfound inventory wisdom to the test in this lush forest setting."
#    "Imagine you're designing a game, and your player is wandering through a forest when, out of the blue, they stumble upon a valuable item – an 'Apple'! That's a score!"
#    $ inventory.append("Apple")
#
#    "Now we have added this mystery apple to our inventory"
#    "This is where your game design skills shine. You've given your player a life-changing reward that's sure to make their gaming experience better."
#    "Not only did they receive it from the benevolent forest goddess, but they've also earned some extra love points. It's like hitting three birds with one stone!"
#
#    "Now, let's get back to the tutorial. In simple terms, here's what we're doing: we're checking if your inventory contains a specific item. If it does, something special will happen in your game."
#
#    if "Apple" in inventory:
#        "You're nailing this game design thing! The apple is safely tucked in their inventory, and your player is in for a treat."
#        "Now let's add 1000 gold and a mystical compass. Trust me; it'll come in handy!"
#        $ gold += 1000
#        $ inventory.append("Compass")
#        "Take a quick look at the inventory in the HUD screen."
#    else:
#        "Oops, it seems the apple slipped away this time. No worries, we've got a backup plan."
#        "Behold, a fish! Think of it as a consolation prize. But next time, don't forget to stock up on those apples."
#        $ inventory.append('Fish')
#
#    hide Forest
#
#    jump End
#
#return
#
#return
# 