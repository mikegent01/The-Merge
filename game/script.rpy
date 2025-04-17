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
default selected_item = None
define MEO = Character("Meowbahh")
define MIK = Character("Mike")
define MAR = Character("Marc")
define EMA = Character("Emma")
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
define co = Character("Commanding Officer Miller",color="#0000FF")
default head_item = None  # Item equipped on the head
default body_item = None  # Item equipped on the body
default left_hand_item = None  # Item equipped in the left hand
default right_hand_item = None  # Item equipped in the right hand
default left_leg_item = None  # Item equipped on the left leg
default right_leg_item = None  # Item equipped on the right legdefault left_arm_item = None
default right_arm_item = None
default hud_visible = True  # Start with the HUD visible
default slot_count = 1
default roll = 0
default intelligence_values = [0, 0, 0, 0, 0]
default rolltf = 0
default collected_tapes = []

#Quests
#default quests = [ #this was retarded so i made it an array
 #  {
 #      "name": "New Uniform Quest",
 #      "description": "Go to the front desk to order a new uniform.",
 #      "completed": False,
 #      "condition": "uniform_ordered"
 #  },
 #  {
 #      "name": "Projector Quest",
 #      "description": "Get a new projector and bring it to the projector room.",
 #      "completed": False,
 #      "condition": "projector_obtained"
 #  }
#]
default minigame_active = False
default minigame_time = 10
default minigame_problem = ""
default minigame_answer = 0
default minigame_bonus = 0
default player_answer = ""
default base_chance = 30  
default total_bonuses = 0  
default nice = 0
default mean = 0
default soft_skills = ["speech","intelligence","luck","pain_tolerance","mental_resilience" ]
default hard_skills = [ "strength","medical" , "speed"]
default selected_category = "soft"  # Initial selection
default title_screen_set = ""
#
default emotions = {
    "Authenticity": {"value": 50, "bonus": {"speech": 5, "luck": -2,"mental_resilience": -6,"pain_tolerance": -5}},
    "Authority": {"value": 60, "bonus": {"strength": 6, "intelligence": -5}},
    "Composure": {"value": 20, "bonus": {"speech": 5, "strength": 3, "intelligence": -3, "pain_tolerancEe": 3}},
    "Confidence": {"value": 15, "bonus": {"speech": -3,"intelligence": -4, "mental_resilience": 4}},
    "Dignity": {"value": 60, "bonus": {"speech": 5, "mental_resilience": 3, "luck": -2}},
    "Pride": {"value": 10, "bonus": {"intelligence": -5, "strength": 5, "mental_resilience": 6,"pain_tolerance": 5}},
}
# The game starts here.RR
default npc_name = "???"         # The default NPC name
default npc_mood = "Normal"      # The default NPC mood
default npc_attitude = "Neutral" # The default NPC attitude
default selected_tab = "Boobs"
default current_mode = "construction"
default mixing_progress = 0
default amount_input = 0
default mix_start_time = 0
default mixing_steps = ["top", "right", "bottom", "left"]
default stirring_tool = None
default stirring_progress = 0
default stirring_complete = False
default last_mouse_pos = (0, 0)
default stirring_direction = None
default stirring_count = 0#pytrhon
default expanded_entry = None    
default current_journal_section = "quests"
default selected_entry = None
default unlocked_books = []
default missions = {"active": [], "completed": []}
default journal_entries = []
default personal_notes_text = ""
default highlight_position = (-1, -1)
$ quest_filter = "all"
$ selected_quest = None
init python:
    import webbrowser
    import random   
    import time      
    import hashlib
    import threading   
    import urllib
    from http.server import SimpleHTTPRequestHandler
    from socketserver import TCPServer
    import os    
    def get_filtered_item_count(filter_type):
        """
        Returns the count of items matching the specified filter type.
        
        Args:
            filter_type (str): The type of items to count ('all', 'weapon', 'armor', 'consumable', etc.)
            
        Returns:
            int: Number of items matching the filter
        """
        count = 0
        
        # Assuming you have a inventory list or similar structure
        for item in inventory:
            if filter_type == "all" or get_item_type(item) == filter_type:
                count += 1
                
        return count
    
    def get_max_slots():
        """
        Returns the maximum number of inventory slots available to the player.
        
        Returns:
            int: Maximum inventory slots
        """
        # You can make this dynamic based on player upgrades or stats
        return 50  # Default value, adjust as needed
    
    def get_filtered_item_at_index(index, filter_type):
        """
        Returns the item at the specified index after filtering by type.
        
        Args:
            index (int): The index in the filtered list
            filter_type (str): The type of items to filter ('all', 'weapon', 'armor', 'consumable', etc.)
            
        Returns:
            item object or None: The item at the index or None if no item exists
        """
        filtered_items = []
        
        # Filter the inventory
        for item in inventory:
            if filter_type == "all" or get_item_type(item) == filter_type:
                filtered_items.append(item)
        
        # Return the item at the index if it exists
        if 0 <= index < len(filtered_items):
            return filtered_items[index]
        else:
            return None    
    if not hasattr(persistent, 'journal_entries') or persistent.journal_entries is None:
        persistent.journal_entries = []  # Ensure it's a list    
    PORT = 3000
    HTML_DIR = os.path.join(renpy.config.gamedir, "htmls")
    def unlock_book(title, text_file, preview="images/inventory/inventory_hud/default_book.png"):
        """
        Unlock a book that can be read in-game.
        text_file: Path to the text file containing the book content
        """
        # Get current game day or use a default
        current_day = getattr(store, 'day', 1)
        
        # Check if the text file exists
        if renpy.loadable(text_file):
            new_book = {
                "title": title, 
                "text_file": text_file, 
                "preview": preview, 
                "date_unlocked": "Day " + str(current_day)
            }
            
            # Check if the book is already unlocked
            for book in store.unlocked_books:
                if book["title"] == title:
                    return  # Book already exists
                    
            store.unlocked_books.append(new_book)
       #     renpy.notify("New book added to your journal: " + title)
        else:
            renpy.notify("Error: Book file not found: " + text_file)
    
    def load_book_text(text_file):
        """Load book content from a text file and split into pages"""
        try:
            with renpy.file(text_file) as f:
                content = f.read().decode("utf-8")
                
            # Split content into pages (each page is about 250 words)
            words = content.split()
            words_per_page = 250
            pages = []
            
            for i in range(0, len(words), words_per_page):
                page_words = words[i:i + words_per_page]
                pages.append(" ".join(page_words))
                
            return pages
        except:
            return ["Error loading book content. The file might be missing or corrupted."]
    
    def add_mission(title, description, objectives=None):
        if objectives is None:
            objectives = []
        # Get current game day or use a default
        current_day = getattr(store, 'day', 1)
        new_mission = {"title": title, "description": description, "objectives": objectives, "progress": 0, "date_added": "Day " + str(current_day)}
        
        # Check if mission already exists
        for mission in store.missions["active"]:
            if mission["title"] == title:
                return  # Mission already exists
                
        store.missions["active"].append(new_mission)
        renpy.notify("New mission added: " + title)
    
    def update_mission_progress(title, progress):
        """Update the progress of a mission (0-100)"""
        for mission in store.missions["active"]:
            if mission["title"] == title:
                mission["progress"] = min(100, max(0, progress))  # Clamp between 0-100
                if mission["progress"] == 100:
                    complete_mission(title)
                return True
        return False
    
    def complete_mission(title):
        for i, mission in enumerate(store.missions["active"]):
            if mission["title"] == title:
                mission["progress"] = 100
                store.missions["completed"].append(mission)
                store.missions["active"].pop(i)
                renpy.notify("Mission completed: " + title)
                return True
        return False
    
    def add_journal_entry(title, content):
        # Get current game day or use a default
        current_day = getattr(store, 'day', 1)
        entry = {"title": title, "content": content, "date": "Day " + str(current_day)}
        store.journal_entries.append(entry)
        renpy.notify("New journal entry added")
    def add_mission(title, description, objectives=None):
        if objectives is None:
            objectives = []
        # Get current game day or use a default
        current_day = getattr(store, 'day', 1)
        new_mission = {"title": title, "description": description, "objectives": objectives, "progress": 0, "date_added": "Day " + str(current_day)}
        
        # Check if mission already exists
        for mission in persistent.missions["active"]:
            if mission["title"] == title:
                return  # Mission already exists
                
        persistent.missions["active"].append(new_mission)
        renpy.notify("New mission added: " + title)
    
    def complete_mission(title):
        for i, mission in enumerate(persistent.missions["active"]):
            if mission["title"] == title:
                mission["progress"] = 100
                persistent.missions["completed"].append(mission)
                persistent.missions["active"].pop(i)
                renpy.notify("Mission completed: " + title)
                return True
        return False
    
    def add_journal_entry(title, content):
        # Get current game day or use a default
        current_day = getattr(store, 'day', 1)
        entry = {"title": title, "content": content, "date": "Day " + str(current_day)}
        persistent.journal_entries.append(entry)
        renpy.notify("New journal entry added")
    minhealth = 0
    maxhealth = 100
    full_weight = 0
    total_health = 0
    total_cleanliness = 0
    total_temperature = 0
    current_selected_character = "Ben"
    current_strength = random.randint(16,20)  
    max_space = 10 + current_strength     
    current_sanity = 100
    crafting_items = []
    selected_items = []
    mixed_liquids = []    
    inventory = []
    left_arm_item = None
    right_arm_item = None    
    selected_liquids = []   
    holding_items = ["Tape", "Glue", "Screwdriver"]
    liquid_inventory = [
        {"name": "Water", "amount": 100},    # 100 units of water
        {"name": "Ethanol", "amount": 50},   # 50 units of ethanol
        {"name": "Oil", "amount": 30},       # 30 units of oil
        {"name": "Glue", "amount": 30}
    ]   
    
    default_status = {
    "head": {"status": "fine", "health": 100, "conditions": [], "temperature": 70, "cleanliness": 74},
    "body": {"status": "fine", "health": 100, "conditions": [], "temperature": 70, "cleanliness": 70},
    "left_arm": {"status": "fine", "health": 100, "conditions": [], "temperature": 70, "cleanliness": 74},
    "right_arm": {"status": "fine", "health": 100, "conditions": [], "temperature": 70, "cleanliness": 70},
    "left_leg": {"status": "fine", "health": 100, "conditions": [], "temperature": 70, "cleanliness": 73},
    "right_leg": {"status": "fine", "health": 100, "conditions": [], "temperature": 70, "cleanliness": 72}
    }

    def get_top_emotion_bonuses(emotions):
        # Sort emotions by value in descending order
        sorted_emotions = sorted(emotions.items(), key=lambda x: x[1]["value"], reverse=True)

        # Get the top emotion
        top_emotion = sorted_emotions[0][0] if sorted_emotions else None

        # Get the bonuses for the top emotion
        if top_emotion and top_emotion in emotions:
            return top_emotion, emotions[top_emotion]["bonus"]
        else:
            return None, {}
    def get_reduced_bonuses(bonuses):
        reduced_bonuses = {}
        for stat, bonus in bonuses.items():
            reduced_bonuses[stat] = bonus // 2  # Reduce bonus by half (integer division)
        return reduced_bonuses
    def get_top_emotions(emotions):
        sorted_emotions = sorted(emotions.items(), key=lambda x: x[1]["value"], reverse=True)
        top_emotions = sorted_emotions[:3]
        other_emotions = sorted_emotions[3:]

        return top_emotions, other_emotions    


    def update_stirring_progress():
        global stirring_progress, last_mouse_pos, stirring_direction, stirring_count, stirring_complete

        # Get current mouse position
        current_mouse_pos = renpy.get_mouse_pos()

        # Calculate the direction of movement
        if last_mouse_pos != (0, 0):
            dx = current_mouse_pos[0] - last_mouse_pos[0]
            dy = current_mouse_pos[1] - last_mouse_pos[1]

            # Determine the direction of movement
            if abs(dx) > abs(dy):
                if dx > 0:
                    new_direction = "right"
                else:
                    new_direction = "left"
            else:
                if dy > 0:
                    new_direction = "down"
                else:
                    new_direction = "up"

            # Check if the direction has changed in a circular pattern
            if stirring_direction:
                if (stirring_direction == "right" and new_direction == "down") or \
                   (stirring_direction == "down" and new_direction == "left") or \
                   (stirring_direction == "left" and new_direction == "up") or \
                   (stirring_direction == "up" and new_direction == "right"):
                    stirring_count += 1
                    if stirring_count >= 4:  # One full circle
                        stirring_progress += 10
                        stirring_count = 0
                        if stirring_progress >= 100:
                            stirring_progress = 100
                            stirring_complete = True
                            renpy.notify("Stirring complete!")
                            mix_liquids(selected_container, selected_liquids)

            stirring_direction = new_direction

        # Update the last mouse position
        last_mouse_pos = current_mouse_pos

# Function to reset stirring progress
    def reset_stirring():
        global stirring_tool, stirring_progress, stirring_complete, last_mouse_pos, stirring_direction, stirring_count
        stirring_tool = None
        stirring_progress = 0
        stirring_complete = False
        last_mouse_pos = (0, 0)
        stirring_direction = None
        stirring_count = 0
    def get_emotion_value(emotions_dict, emotion):
        return emotions_dict.get(emotion, 0)

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
    deconstruction_recipes = {
        "Laser Tactical Kit": ["Laser range finder", "Tactical flashlight", "Glue"],
        "Navigation Radio": ["Compass", "Radio", "Screwdriver"],
        "First Aid Kit": ["Bandage", "Antibiotics", "Acetaminophen", "SOFT-T"],
        "Flashlight": ["Bulb", "Battery", "Reflector"],
        "radio": ["Antenna", "Battery", "Circuit Board"]
        # Add more items as needed
    }
    def handle_mixing_click(direction):
        global current_mixing_step, mixing_attempts

        if direction == mixing_steps[current_mixing_step]:
            current_mixing_step += 1
            if current_mixing_step >= len(mixing_steps):
                current_mixing_step = 0
                mixing_attempts += 1
                if mixing_attempts >= 2:
                    renpy.notify("Mixing complete!")
                    mix_liquids(selected_container, selected_liquids)
                    reset_mixing()
                else:
                    renpy.notify(f"Step {mixing_attempts + 1}: Continue mixing!")
        else:
            renpy.notify("Wrong direction! Start over.")
            reset_mixing()
    def perform_roll(base_chance, skill_level, skill_name, total_bonuses):
        skill_data = stats.get(skill_name, {})
        skill_value = skill_data.get("current_value", 0)
        total_chance = base_chance + (skill_level * 5) + skill_value + total_bonuses
        roll_result = renpy.random.randint(1, 100)
        # Determine success
        if roll_result <= total_chance:
            return True
        else:
            return False

    def reset_mixing():
        global current_mixing_step, mixing_attempts
        current_mixing_step = 0
        mixing_attempts = 0    
    def deconstruct_item(item):
        global inventory  # Only need inventory for this function

        # Check if the item can be deconstructed
        if item in deconstruction_recipes:
            # Get the list of components required for this item
            components = deconstruction_recipes[item]

            # Add the components back to the inventory
            for component in components:
                inventory.append(component)

            # Remove the deconstructed item from the inventory
            inventory.remove(item)

            # Notify the player of successful deconstruction
            renpy.notify(f"You deconstructed {item} into: {', '.join(components)}.")
        else:
            # Notify the player if the item cannot be deconstructed
            renpy.notify(f"{item} cannot be deconstructed.")

    def calculate_averages():
        total_health = 0
        total_cleanliness = 0
        total_temperature = 0
        body_part_count = len(default_status)

        for part, status in default_status.items():
            total_health += status['health']
            total_cleanliness += status['cleanliness']
            total_temperature += status['temperature']

        average_health = round(total_health / body_part_count)
        average_cleanliness = round(total_cleanliness / body_part_count)
        average_temperature = round(total_temperature / body_part_count)

        return average_health, average_cleanliness, average_temperature
    def is_highest_emotion(emotions_dict, emotion):

        if emotion not in emotions_dict:
            return False  
        highest_emotion = max(emotions_dict, key=emotions_dict.get)
        return highest_emotion == emotion
    def update_emotion_value(emotions_dict, emotion, new_value):
        if emotion in emotions_dict:
            emotions_dict[emotion] = new_value
            return True
        return False
    relationships = {
        "Samuel": {
            "met": False,
            "trust": 80,
            "friendship": 54,
            "hostility": 1,
        },
        "Dan": {
            "met": False,
            "trust": 60,
            "friendship": 60,
            "hostility": 10,
        }
    }
# Function to determine relationship description
    def get_relationship_description(trust, friendship, hostility):
        if trust > 80 and friendship > 80:
            return "Best Friend"
        elif trust > 70 and friendship > 70:
            return "Close Friend"
        elif trust > 60 and friendship > 60:
            return "Good Friend"
        elif trust > 50 and friendship > 50:
            return "Trusted Friend"
        elif friendship > 50 and trust > 30:
            return "Friend"
        elif friendship > 50 and trust <= 30:
            return "Associate"
        elif trust > 50 and friendship <= 30:
            return "Trusted Associate"
        elif hostility > 70:
            return "Enemy"
        elif hostility > 50:
            return "Adversary"
        elif hostility > 30 and trust <= 30 and friendship <= 30:
            return "Rival"
        elif trust > 30 and friendship > 30:
            return "Neutral Acquaintance"
        else:
            return "Stranger"
    container_inventory = [
        {"name": "Regular Bottle", "capacity": 100, "current_amount": 0, "contents": []},  # Empty bottle
        {"name": "Water Bottle", "capacity": 500, "current_amount": 0, "contents": []},  # Empty bottle
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
#
    def is_container_empty():
        for item in container_inventory:
            if item["current_amount"] == 0 and not item["contents"]:
                return True
            return False
#


#
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
        global selected_item
        if item in inventory:  # Assuming 'inventory' is your list of items
            inventory.remove(item)
        if item == selected_item:  # Clear the selected item if it's the one being removed
            selected_item = None
        renpy.restart_interaction()  # Refresh the screen to reflect changes

#
    def select_item(item):
        if item not in selected_items and len(selected_items) < 10:  # Allow only two selections
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
# Function to pour liquid from one container to another or the ground
    def pour_liquid(source_container, target_container):
        if source_container["contents"]:
            content = source_container["contents"][0]  # Assuming only one type of liquid per bottle
            if target_container:
                if target_container["current_amount"] + content["amount"] <= target_container["capacity"]:
                    target_container["contents"].append({"name": content["name"], "amount": content["amount"]})
                    target_container["current_amount"] += content["amount"]
                    source_container["contents"].remove(content)
                    source_container["current_amount"] -= content["amount"]
                    renpy.notify(f"Poured {content['name']} from {source_container['name']} to {target_container['name']}.")
                else:
                    renpy.notify("Not enough space in the target container!")
            else:
                # Pour to ground
                source_container["contents"].remove(content)
                source_container["current_amount"] -= content["amount"]
                renpy.notify(f"Poured {content['name']} from {source_container['name']} to the ground.")

    def drain_liquid(container):
        if container["contents"]:
            for content in container["contents"][:]:  # Iterate over a copy of the list
                content["amount"] = max(0, content["amount"] - 10)
                container["current_amount"] = max(0, container["current_amount"] - 10)
                if content["amount"] <= 0:
                    container["contents"].remove(content)
                    renpy.notify(f"Removed {content['name']} from {container['name']}.")
            renpy.notify("Drained 10 ml of each liquid from the bottle.")
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
        # Get the contents of the container
        contents = container["contents"]

        # Create a dictionary to store the amounts of each liquid in the container
        container_liquids = {}
        for content in contents:
            container_liquids[content["name"]] = content["amount"]

        # Compare the container's contents with each recipe
        for recipe_name, recipe_ingredients in liquid_mix_recipes.items():
            match = True
            for ingredient, amount in recipe_ingredients.items():
                if ingredient not in container_liquids or container_liquids[ingredient] < amount:
                    match = False
                    break
            if match:
                return recipe_name  # Return the name of the matching recipe
            
        return None  # No matching recipe found
    def initialize_stats():
        for stat in stats:
            if stat != "sanity":
                stats[stat]["current_value"] = calculate_stat_value(stats[stat]["level"])
                stats[stat]["current_xp"] = calculate_stat_value(stats[stat]["level"])

    def calculate_stat_value(level):
        for stat in stats:
            return level * random.randint(1, 4) + random.randint(1, 4) + stats[stat]["current_value"] 

    initialize_stats()
    def handle_mixing_motion():
        global mixing_progress, is_mixing, mix_start_time
        if is_mixing:
            # Increase mixing progress based on time
            mixing_progress += renpy.random.randint(1, 3)
            if mixing_progress >= 100:
                mixing_progress = 100
                is_mixing = False
                renpy.notify("Mixing complete!")
                # Perform the actual mixing logic here
                mix_liquids(selected_container, selected_liquids)
        return    
    def mix_liquids(container, liquids):
        # Check if the container's contents match a recipe
        recipe_name = check_mix_recipe(container)
        if recipe_name:
            # Perform the mixing logic
            renpy.notify(f"Successfully created {recipe_name}!")

            # Clear the container's contents and add the new mixture
            container["contents"] = [{"name": recipe_name, "amount": sum(content["amount"] for content in container["contents"])}]
            container["current_amount"] = sum(content["amount"] for content in container["contents"])
        else:
            renpy.notify("No valid recipe found for the current mixture.")
            drain_liquid(selected_container)
            selected_container["contents"] = [{"name": "Sludge", "amount": selected_container["current_amount"]}]

# Function to add liquid to the selected bottle
    def add_liquid_to_selected(liquid):
        if selected_container:
            amount = 10  # Fixed amount to add
            if selected_container["current_amount"] + amount <= selected_container["capacity"]:
                if amount <= liquid["amount"]:
                    # Check if the liquid already exists in the container
                    found = False
                    for content in selected_container["contents"]:
                        if content["name"] == liquid["name"]:
                            content["amount"] += amount
                            found = True
                            break
                    if not found:
                        selected_container["contents"].append({"name": liquid["name"], "amount": amount})

                    selected_container["current_amount"] += amount
                    liquid["amount"] -= amount
                    renpy.notify(f"Added {amount} ml of {liquid['name']} to {selected_container['name']}.")
                else:
                    renpy.notify("Not enough liquid available!")
            else:
                renpy.notify("Not enough space in the container!")
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

    def check_temperature(part):
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
    def check_cleanliness_and_adjust_temp(part):
        cleanliness = default_status[part]['cleanliness']

        if cleanliness > 90:
            default_status[part]['temperature'] -= 2  # Clean parts may be cooler
        elif cleanliness > 75:
            default_status[part]['temperature'] -= 1
        elif cleanliness < 50:
            default_status[part]['temperature'] += 1  # Dirty parts may be warmer
        elif cleanliness < 25:
            default_status[part]['temperature'] += 2

    def modify_cleanliness(part, amount):
        global default_status
        default_status[part]['cleanliness'] += amount

        default_status[part]['cleanliness'] = max(0, min(100, default_status[part]['cleanliness']))

        check_cleanliness_and_adjust_temp(part)

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
        modify_cleanliness(part, -1)
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
    class CustomHandler(SimpleHTTPRequestHandler):
        # --- ADJUSTED translate_path ---
        def translate_path(self, path):
            """Translate a URL path (expected to start with /game/htmls/) to the local filesystem path."""
            # Decode URL-encoded characters (like %20 for space)
            decoded_path = urllib.parse.unquote(path)

            # Define the expected prefix in the URL path
            url_prefix = "/game/htmls/"
            disk_prefix_to_remove = "game/htmls/" # The part to strip to get the path relative to HTML_DIR

            # Get the path component after the domain, removing leading slash
            path_component = decoded_path.lstrip('/') # e.g., "game/htmls/006.html" or "radio.css"

            # Check if the path component starts with the expected disk prefix
            if path_component.startswith(disk_prefix_to_remove):
                # If it does, remove the prefix to get the path relative to HTML_DIR
                relative_file_path = path_component[len(disk_prefix_to_remove):] # e.g., "006.html"
            else:
                # If it doesn't (e.g., CSS, JS, audio files referenced relatively in the HTML),
                # assume the path component is already relative to HTML_DIR.
                relative_file_path = path_component # e.g., "radio.css", "audio/0.wav"

            # Prevent directory traversal attacks (important!)
            safe_relative_path = os.path.normpath(relative_file_path).lstrip(os.sep)

            # Join the HTML directory (base) with the safe relative path component
            fullpath = os.path.join(HTML_DIR, safe_relative_path)

            # --- Debugging ---
            # print(f"Requested path (URL): {path}")
            # print(f"Decoded path component: {path_component}")
            # print(f"Relative file path used: {relative_file_path}")
            # print(f"Attempting to serve (Disk): {fullpath}")
            # print(f"File exists: {os.path.exists(fullpath)}")
            # --- End Debugging ---

            return fullpath # Return the absolute disk path

        # Override directory listing (keep this)
        def list_directory(self, path):
            self.send_error(404, "File not found or directory listing disabled")
            return None

        # Disable logging (keep this)
        def log_message(self, format, *args):
            pass

    # --- Keep the WebServer class and server startup/stop logic the same ---
    class WebServer(threading.Thread):
        # ... (rest of WebServer class is unchanged) ...
        def __init__(self):
            super().__init__()
            self.daemon = True
            self.server = None

        def run(self):
            if not os.path.isdir(HTML_DIR):
                renpy.notify(f"Error: HTML directory not found at {HTML_DIR}")
                print(f"Error: HTML directory not found at {HTML_DIR}")
                return
            try:
                self.server = TCPServer(("localhost", PORT), CustomHandler)
                print(f"Web server started on http://localhost:{PORT} serving from {HTML_DIR}")
                self.server.serve_forever()
            except OSError as e:
                renpy.notify(f"Failed to start server on port {PORT}: {str(e)}")
                print(f"Failed to start server on port {PORT}: {str(e)} - Is another application using it?")
            except Exception as e:
                renpy.notify(f"Failed to start server: {str(e)}")
                print(f"Failed to start server: {str(e)}")

        def stop(self):
            if self.server:
                self.server.shutdown()
                self.server.server_close()
                print("Web server stopped")

    web_server = WebServer()
    web_server.start()
    def stop_server():
        web_server.stop()
    config.quit_action = stop_server
    # --- End Server Logic ---


    # --- ADJUSTED open_html function ---
    def open_html(name, label_value):
        """Opens the specified HTML file, including /game/htmls/ in the URL."""
        safe_label = urllib.parse.quote(label_value if label_value else "Unknown")
        # Construct the URL *with* /game/htmls/ included
        url = f"http://localhost:{PORT}/game/htmls/{name}.html?lastLabel={safe_label}"
        print(f"Opening URL: {url}") # Debugging output
        webbrowser.open(url)


    def has_item(item):
        return item in inventory
    def has_stirring_tool(tool):
        return tool in inventory    
    def add_item(item_name):
        """
        Add an item to the inventory if there is space and the item exists in the items dictionary.
        """
        global inventory, max_space

        # Check if the item exists in the items dictionary
        if item_name not in items:
            return f"Item '{item_name}' does not exist."

        # Check if there is space in the inventory
        if len(inventory) >= max_space:
            return "Inventory is full. Cannot add more items."

        # Check if adding the item would exceed the weight limit (if applicable)
        # Assuming max_weight is a global variable defining the maximum weight capacity
        if calculate_total_weight() + items[item_name]["weight"] > max_weight:
            return "Adding this item would exceed the weight limit."

        # Add the item to the inventory
        inventory.append(item_name)
        return f"Added '{item_name}' to the inventory."
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
    def start_minigame():
        global minigame_time, minigame_active, minigame_problem, minigame_answer, player_answer
        minigame_time = 10  # 10 seconds for the mini-game
        minigame_active = True
        minigame_problem, minigame_answer = generate_problem()
        player_answer = ""  # Reset player's answer


    def check_minigame_answer():
        global minigame_active, minigame_bonus, minigame_problem, minigame_answer, player_answer

        # Debug: Print the player's answer
        print(f"Player's answer: {player_answer}")

        # Check if the player's answer is correct
        if player_answer.isdigit() and int(player_answer) == minigame_answer:
            minigame_bonus += 1
            renpy.notify("Correct! Well done.")  # Notify the player
        else:
            minigame_bonus -= 1
            renpy.notify(f"The correct answer was {minigame_answer}.")  # Notify the player

        # Generate a new problem
        minigame_problem, minigame_answer = generate_problem()
        player_answer = ""  # Reset player's answer



    def generate_problem():
        problem_types = ["addition", "multiplication"]
        problem_type = random.choice(problem_types)
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)

        if problem_type == "addition":
            problem = f"{num1} + {num2}"
            answer = num1 + num2
        elif problem_type == "multiplication":
            problem = f"{num1} * {num2}"
            answer = num1 * num2

        return problem, answer  # Return both the problem and the answer
    def calculate_total_weight():
        """Calculate the total weight of items in the inventory."""
        total_weight = sum(get_item_weight(item) for item in inventory)
        return total_weight
    def get_remaining_space():
        return max_space - len(inventory) 
    def ToggleScreenVisibility():
        global hud_visible
        hud_visible = not hud_visible  # Toggle between True and False

    def prompt_for_removal(message):
        """Prompt the player to remove an item."""
        renpy.notify(message)
        renpy.call_innew_context("prompt_remove_item")  # Call a new screen to handle item removal

    def calculate_total_bonus(skill, sorted_emotions):
        total_bonus = 0

        top_emotion = sorted_emotions[0][0] if sorted_emotions else None

        if top_emotion:
            main_emotion_data = sorted_emotions[0][1]
            if skill in main_emotion_data["bonus"]:
                total_bonus += main_emotion_data["bonus"][skill]

        for emotion, data in sorted_emotions[1:2]:
            if skill in data["bonus"]:
                reduced_bonus = get_reduced_bonuses(data["bonus"]).get(skill, 0)
                total_bonus += reduced_bonus

        return total_bonus

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

# Example of gaining experience (you can adjust this function based on game events)
    def add_experience(stat_name, amount):
        stats[stat_name]["current_xp"] += amount
        if stats[stat_name]["current_xp"] >= stats[stat_name]["max_xp"]:
            stats[stat_name]["current_xp"] = stats[stat_name]["max_xp"] # Cap XP at max if it exceeds
# Define the items dictionary
    items = {
        "MG41": {
            "type": "weapon",
            "weight": 10,
            "description": "A powerful machine gun. There are many like it but this one is mine."
        },
        "Laser range finder": {
            "type": "tool",
            "weight": 1,
            "description": "Used to measure the distance from here to a target."
        },
        "Compass": {
            "type": "tool",
            "weight": 1,
            "description": "A military grade compass used for navigation."
        },
        "radio": {
            "type": "tool",
            "weight": 2,
            "description": "A military grade radio used for communication. Is only able to communicate with military units and HQ."
        },
        "First aid kit": {
            "type": "consumable",
            "weight": 1,
            "description": "Used to heal minor injuries."
        },
        "Tactical flashlight": {
            "type": "tool",
            "weight": 1,
            "description": "This light can survive explosions and runs on solar battery."
        },
        "Water Bottle": {
            "type": "consumable",
            "weight": 1,
            "description": "Used to hold water. Can hold up to 500ml of water...or any other liquid for that matter."
        },
        "sissor": {
            "type": "tool",
            "weight": 1,
            "description": "Used to cut things."
        },
        "Report 001": {
            "type": "document",
            "weight": 300,
            "description": "A report of something? I don't remember what it is for. It's very important."
        }
    }
    def get_item_weight(item):
        """Return the weight of an item."""
        if item in items:
            return items[item]["weight"]
        return 1  # Default weight if item not found
    def get_item_description(item):
        """Return the description of an item."""
        if item in items:
            return items[item]["description"]
        return "No description available."  # Default description if item not found
    def set_room_temperature(room_temp):
        for part, attributes in default_status.items():
            if part == "body":
                temperature_variation = random.uniform(0, 2)  
                default_status[part]['temperature'] = round(room_temp + 10 + temperature_variation)  
            elif part == "head":
                temperature_variation = random.uniform(-2, 2) 
                default_status[part]['temperature'] = round(room_temp + 5 + temperature_variation)
            else:
                temperature_variation = random.uniform(-3, 3)  
                default_status[part]['temperature'] = round(room_temp + temperature_variation)

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
    def equip_item(item, slot):
        """Equip an item to the specified body slot."""
        global head_item, body_item, left_hand_item, right_hand_item, left_leg_item, right_leg_item, inventory

        # Check if the item is in the inventory
        if item not in inventory:
            renpy.notify("Item not found in inventory.")
            return

        # Get item type from the item data
        item_type = items[item]["type"]

        # Check if the item can be equipped in the selected slot
        if slot == "head" and item_type == "head":
            if head_item:
                inventory.append(head_item)  # Unequip current head item
            head_item = item
        elif slot == "body" and item_type == "body":
            if body_item:
                inventory.append(body_item)  # Unequip current body item
            body_item = item
        elif slot == "left_hand" or item_type == "weapon"  or item_type == "tool":
            if left_hand_item:
                inventory.append(left_hand_item)  # Unequip current left hand item
            left_hand_item = item
        elif slot == "right_hand" or item_type == "weapon" or item_type == "tool":
            if right_hand_item:
                inventory.append(right_hand_item)  # Unequip current right hand item
            right_hand_item = item
        elif slot == "left_leg" and item_type == "legs":
            if left_leg_item:
                inventory.append(left_leg_item)  # Unequip current left leg item
            left_leg_item = item
        elif slot == "right_leg" and item_type == "legs":
            if right_leg_item:
                inventory.append(right_leg_item)  # Unequip current right leg item
            right_leg_item = item
        else:
            renpy.notify(f"Cannot equip {item} in {slot} slot.")
            return

        # Remove the item from the inventory
        inventory.remove(item)
        renpy.notify(f"Equipped {item} to {slot} slot.")
    def unequip_item(slot):
        """Unequip an item from the specified body slot."""
        global head_item, body_item, left_hand_item, right_hand_item, left_leg_item, right_leg_item, inventory

        if slot == "head" and head_item:
            inventory.append(head_item)
            head_item = None
            renpy.notify("Unequipped item from head slot.")
        elif slot == "body" and body_item:
            inventory.append(body_item)
            body_item = None
            renpy.notify("Unequipped item from body slot.")
        elif slot == "left_hand" and left_hand_item:
            inventory.append(left_hand_item)
            left_hand_item = None
            renpy.notify("Unequipped item from left hand slot.")
        elif slot == "right_hand" and right_hand_item:
            inventory.append(right_hand_item)
            right_hand_item = None
            renpy.notify("Unequipped item from right hand slot.")
        elif slot == "left_leg" and left_leg_item:
            inventory.append(left_leg_item)
            left_leg_item = None
            renpy.notify("Unequipped item from left leg slot.")
        elif slot == "right_leg" and right_leg_item:
            inventory.append(right_leg_item)
            right_leg_item = None
            renpy.notify("Unequipped item from right leg slot.")
        else:
            renpy.notify("No item to unequip from this slot.")
    def discard_item(slot):
        """Discard an item from the specified body slot."""
        global head_item, body_item, left_hand_item, right_hand_item, left_leg_item, right_leg_item, inventory

        item_to_discard = None

        if slot == "head" and head_item:
            item_to_discard = head_item
            head_item = None
        elif slot == "body" and body_item:
            item_to_discard = body_item
            body_item = None
        elif slot == "left_hand" and left_hand_item:
            item_to_discard = left_hand_item
            left_hand_item = None
        elif slot == "right_hand" and right_hand_item:
            item_to_discard = right_hand_item
            right_hand_item = None
        elif slot == "left_leg" and left_leg_item:
            item_to_discard = left_leg_item
            left_leg_item = None
        elif slot == "right_leg" and right_leg_item:
            item_to_discard = right_leg_item
            right_leg_item = None

        if item_to_discard:
            renpy.notify(f"Discarded {item_to_discard} from {slot} slot.")
        else:
            renpy.notify("No item to discard from this slot.")
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
            renpy.notify("This area is not THAT dark, is it?")
        elif item == "radio":
            renpy.notify("*Listening to radio...*")
            renpy.sound.play("audio/radio/radio.wav")
            open_html("006", last_label) 
            if last_label == "stairwell" and not visited_stairwell and rng < 50:
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
#    $ equip_item("body", "Type 07")
#    $ inventory.append("compass")
#    $ inventory.append("Laser range finder")
#    $ inventory.append("First aid kit")
#    $ inventory.append("radio")
#    $ inventory.append("Tactical flashlight")
#    $ inventory.append("MG41")    
#    $ inventory.append("thermometer")
   # $ inventory.append("compass")
   # $ inventory.append("Laser range finder")
   # $ inventory.append("First aid kit")
   # $ inventory.append("radio")
   # $ inventory.append("Tactical flashlight")
   # $ inventory.append("MG41")    
   # $ inventory.append("thermometer")
       
label gameover:
    "You have died..."
    "Why don't you try loading a save..."
label minigame:
    # Initialize mini-game variables
    $ minigame_time = 10
    $ minigame_active = True
    $ minigame_problem = generate_problem()  # Replace with your problem generation logic

    # Mini-game loop
    while minigame_time > -1:
        # Display the mini-game screen
        call screen minigame_screen

        # Decrease the timer
        $ minigame_time -= 1

        # Check if the mini-game should end
        if minigame_time == 0:
            $ minigame_active = False
            hide screen minigame_screen

    # End of mini-game
    return

label start:    
    hide screen character_selection
    $ rng = random.randint(1,100)
    $ inventory.append("Laser range finder")
    $ inventory.append("First aid kit")
    $ inventory.append("radio")    
    $ collected_tapes.append({
          "title": "Final Recording", # Give it a relevant title
          "description": "A significant audio log.", # Add a description
          "date_found": "The Last Day", # Optional: When/where it was found
          "audio_file": "audio/final.wav"  # <--- Use the relative path here
    })    
    $ set_room_temperature (72)
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
    $ set_room_temperature (72)
    $ rng = random.randint(1,100)
    $ relationships["Samuel"]["met"] = True
    $ inventory.append("radio")   
    $ inventory.append("Spoon")    
    if rng < 50:
        play music marchingon volume 0.1
    else:
        play music boot_camp volume 0.5

    show ben idle at left with dissolve
   # $ quests.append({
   #     "name": "Go to the projector room and listen to the drill sargent.",
   #     "description": "I need to report to the drill sargent for a urgent meeting. ",
   #     "completed": True,     
   # })
    $ unlock_book("Stars and Stripes", "books/poopy.txt")
    "I sit in a crowded room. There are chairs laid out in rows."
    "A soft hum comes from the projector showing multiple images of destroyed American cities on screen."
    "The whole room sits in silence as the images are shown one by one."

    "The silence is broken when drill sergeant Jones begins speaking."

    show sadbigsarg at right
    DRI "These are the stakes"
    DRI "We either make a world in which all of God's children can live, or to go into the dark"
    DRI "Approximately 0300 hours ago, an unknown event occurred near Ruckersville, Virginia, causing major power outages throughout the state."
    DRI "An Incident Relief Division was promptly sent to investigate the problem. Their team reported a several sightings of unknown creatures before we lost contact with them."
    DRI "We have a estimate of around 200 MIA and 100 dead. We must act swiftly and efficiently."
    DRI "Your job will be to find out what happened to the IRD team and to terminate all enemy threats."

    hide sadbigsarg

    "The room remains silent. I feel a slight tap on my shoulder, I sigh suspecting who it is already. My brow lowers as I prepare to deal with him. it is Private Samuel. He is sitting in the seat next to me"
    "My mind must have tried to forget this fact. He was sitting in his seat with a red book in his lap. The room being too dark to know what was on the cover."
    "I hear Samuel whisper to me."

    show samuel chill  at right

    SAM "Psst, hey Benjamin."
    SAM "I was told you would like this. It is a report on what happened today, I stole it from the supply main desk."
    hide samuel chill 
    "I take the sheet from him and look up as the drill sergeant continues. The room is too dark to read what is on the sheet of paper so I put it in my pocket for later."
    "I look back at samuel, he looks like he is waiting for something"
    BEN "Thanks, I will look through the report later."
    "He smiles and looks back at the drill instructor. It seems like that was enough to satisfy him. I look back at the drill instructor and begin listening to him once more."
    show sadbigsarg at right

    DRI "In approximately two days, we will begin our operation. You will be airlifted and tasked with the extermination of any and all anomalous entities."
    DRI "You are hereby dismissed."

    hide sadbigsarg

    scene bootcampinsideprojectorroomstartm

    "As the lights turn on and the room is no longer in darkness, military personnel start leaving the room."
    "Suddenly, a spark occurs. The projector starts heating up and smoking. The Drill Sargent looks nervous and rushes over to it."
    DRI "Shit,shit,shit!"
    "He rushes to unplug the projector. As he unplugs it, the projector stops spinning the whriling sound coming to an end."
    "He takes out the film from the projector he looks terrified. He looks up at the only standing person left in the room, me."

    show sadsargtalk at right

    DRI "You, meatbag, come over here!"

    "As I walk towards him, he looks down at me with a frown. He is trying to hide his fear, he looks at me with a scowl"

    DRI "This projector is broken. I am not sure how it broke, but it looks like you’re not doing anything of importance. Therefore, you’re in charge of fixing it."

    "I look at him, semi-annoyed. It seems like he is trying to get me to do his dirty work."

    DRI "Do you understand what you need to do?"

    menu:
        "Yes, sir!":
            $ emotions["Authority"]["value"] -= 5
            DRI "Good"
            "His frown turns into a slight smile. It seems he approves of me not acknowledging what just happened and just going along with what he says." 
            DRI "You have [rng] hours to fix this! That is when we leave for virginia."
        "Why do you need to fix this projector?":
            DRI "This film holds data on the mission you were just briefed on. It was the online onsite version of it."
            DRI "Another data request can take weeks to process. We are leaving for the mission in [rng] hours"


    DRI "You are dismissed."
   # $ quests.append({
   #     "name": "Fix the projector",
   #     "description": "The projector has important information that the drill sargent needs, it is broken and I need to fix it. ",
   #     "completed": False,     
   # })
    "As I turn around, I notice two people sitting in their seats. Perhaps I should talk to one of them and ask them for help."
    hide sadsargtalk
    show screen HUD    
    show screen tutorial_screen

    window hide # FIRST CHOICE
    $ renpy.pause(hard=True)


label FrontSeat:
    show sultan talking at left
    window show
    hide screen HUD
    "I walk up to the man; he seems like he is distracted with something."
    "As I peer closer to see what he is doing, I realize he is trying to light a cigar."
    "I think of keeping quiet for a moment but realize that I can use this as an opportunity to get him to help me fix the projector."
    "So, I finally speak up and ask, 'What are you doing?"

    SUL "Huh?"

    "He looks up at me with his mouth open and quickly looks down, putting his cigar away."
    "He looks embarrassed and quickly says, 'Nothing bro, don't worry about it."

    "I smirk."

    BEN "Really, if it is nothing, you wouldn't mind if I checked your pockets, would you?"

    SUL "Look bro, I barely even know you. What do you want, money?"

    "I smirk again; my plan had worked. I continue."

    BEN "Just don’t tell anyone what you saw, okay?"

    SUL "Fine, whatever."

    "I need you to go and help me out with something."

    BEN "What is it, bro?"

    "Do you have any idea how to fix a projector?"

    SUL "Really, bro? You'd rat me out to help with some pet project of yours?"

    "He sighs."

    SUL "Let me take a look, bro."

    "He walks up to the smoking projector and pulls the plug on it. It stops smoking."
    "He picks the film out and puts it down on the table next to it."

    SUL "You got a screwdriver, bro?"

    BEN "No, I don’t. Why would I carry one with me?"

    SUL "Look, bro, I can't fix this problem without a screwdriver. I’m already doing a lot by helping you out. Can you please just get me a screwdriver, bro? It's the least you can do for me."

    "I deliberate on whether I should just tell him to do it himself. The most logical thing to do was to have him do it for me, so I ask."

    BEN "Can't you just do it? You know how to fix this kind of stuff, right?"

    SUL "No, it's either you get me a screwdriver or I don't fix this thing for you, bro."

    "I roll my eyes and turn towards the exit."

    BEN "So, what is it, bro? Are you leaving or getting the screwdriver?"
    "As I exit the door, I say, 'I will be back in a few. Don't move from there."

    scene outsideprojector

    "As I walk outside, I feel the cool stale air from the indoor air conditioning."
    "I smile as the meeting is finally over until I hear someone call my name."

    SAM "Hey, Ben! Check it out!"

    "My smile quickly fades into a frown as I look up to see a face I did not want to see."

    BEN "Hello, Samuel."

    "As I look towards him, my eyes narrow. I notice the book in his hands. It appears to be a picture book."
    "Not wanting to ask, I continue walking until he calls out to me again."

    SAM "W-wait, check it out!"

    BEN "Uncle Ben is a bit busy right now. Can we play later?"

    SAM "Stop joking around. This book is really cool. It's like a story about this guy that collects items and puts them in a summoning circle, creating a rift in the world, and the worlds start to me-"

    BEN "That sounds great, do you have a screwdriver by any chance?"

    SAM "Ohh, I can finally be useful to you, I see. Just follow me, I know where we can get one!"

    "He runs over to the right."

    "As he runs away, I consider to myself just how I got into this position and if it is really worth following him, as it will undoubtedly lead to nothing."
    "Looking back into the projector room, I can see the man from earlier standing idly by, staring back at me."
    "As I look back at him, I realize I never asked for his name."
    "Shrugging it off, I stand at a crossroads. I can either ignore Samuel and look for someone else or follow him to wherever he decides to go, undoubtedly going on another goose chase leading to nowhere."

    menu:
        "Follow him":
            jump keepsamuel
        "Go on my own":
            jump abandonsamuel
label keepsamuel:
    scene outsideprojectorroomnosamuel
    show ben idle at left
    show samuel redbook at right

    "As I deliberate, I feel a tug on my arm."
    SAM "Don't worry, it will be fun!"
    scene storageroom 
    show ben idle at left
    show samuel redbook at right  
    "Before I can respond, I'm forcibly pulled down the hallway. He finally stops and lets go of my arm."
    "I put my hand on my arm and look at where he twisted it, then look up."
    "I see him jumping up and down, pointing to an electric door. To the right of it is a keypad with letters and numbers."
    "He puts on a big grin and starts inputting a passcode."

    "As he starts typing, I hear a loud buzz and the light above the keypad turns red."
    "He laughs a bit and enters it again—another buzz. He tries again, it buzzes again."
    "He continues this for two more tries before I have enough."

    BEN "Are you sure the screwdriver is in there?"
    SAM "There was a screwdriver in there, I am sure of it. The door was open before—that's how I got this book."

    "Before I can ask about him reading a picture book, he shoves it in my face."
    scene bookfullscreen1
    "I realize that while the cover looked like a picture book, there are words inside."
    "I grab it from his hands as he weakly tries to hold onto it."

    SAM "Give me that, hey!"
    "As he tries to grab it back from me, I take a look at the book."
    BEN "Did you rip out a page? Did you damage this book?"
    SAM "No, of course not! I found it in the storage room like this, I swear."
    scene bookfullscreen1

    "Unable to tell if he’s lying or not, I flip through the rest of the book, seeing crude writings and pictures, with text describing a fictional event."
    BEN "Is this a fan fiction? What are you, thirteen?"
    scene storageroom 
    show ben book at left
    show samuel at right
    
    "Before he answers my question, I interrupt him again."
    BEN "You know what, never mind, I don’t need to know or want to know."
    
    "He’s about to cry."
    SAM "Just stay here while I figure out the passcode to that door."
    
    "I don’t wait for a response; instead, I begin to walk away."
    "I find myself alone once again at a crossroads in the hallway, unsure of where to go."
    "As I’m walking, I consider going to get a bite to eat but decide against it. I continue down the hallway until I reach one of the main desks."

    scene apple
    show ben idle at left

    "As I approach the main desk, I smell a murky scent in the air. My eyes tear up as I approach the two shadowy figures."

    BEN "You wouldn’t happen to have a screwdriver, would you?"

    "They both look at each other and nod silently in slow motion. One of them speaks up in a raspy, old voice."
    Q2 "There should be a screwdriver in the storage closet, but you need a password to enter it."

    "My eyes narrow."
    BEN "You wouldn’t happen to have a password, would you?"
    
    "He stares at me blankly, like I just asked something shocking."
    Q2 "No... I do not. This may be the main desk of this building, but our building is not equipped with the modern amenities the other buildings have. This building is the oldest in the camp."
    hide ben
    "As I walk past him, I head to the right, noticing the maintenance hallway. Maybe there’s a screwdriver in here."

    scene bg staircase
    show ben idle at left

    "I quickly search around the hallway, only finding empty storage containers."
    "I see a stairway behind an opened door, and as I approach it, I hear someone running toward me at fast speed."
    "I quickly spin around to see Samuel, book in hand. Standing there with that stupid smile he always puts on."
    "The red book in his hands looking at it.  I see the bright and cheery image in front of a sun shining, it's image contrasted with the bleak reality I am living in."
    
    show samuel redbook at right

    "I try my best to blend in with the environment, but with me being the only other person here, I sigh and prepare to find out what he wants. I think to myself the sooner I talk to him the faster he will leave"
    SAM "What do you want? Didn’t I tell you to wait there?"
    "He looks at me with a sad face."
    SAM "I wanted to show you this."
    "He pulls out the book he was holding and opens it, and something falls out."
    "I bend down and pick up the slip of paper."
    $ htmlopen("003")                    
    "I rip up the note."
    SAM "H-hey, why did you do that?"
    "He tries to grab the scraps of paper."
    BEN "It said to discard it after we read it, so..."
    "I shrug."
    SAM "That note looked new! Like it was put in the notebook not too long ago."

    "He picks up the scraps of paper and looks like he’s about to cry again."
    BEN "You sure are sensitive."

    "I sigh and ask him to look for a screwdriver in this room, since he’s here."
    scene bg storewaystairwellfixed

    "I bend down and pick up the green container on the floor. As I try to lift it up, I realize it’s too heavy. As I try to sit it upright, I hear an annoying sound in my ear."
    
    SAM "Hey, what made you join the force?"
    
    "I drop the box I’m working on, and it almost crushes my leg. before I am able to stablize it"
    $ emotions["Confidence"]["value"] -= 5    
    $ emotions["Pride"]["value"] -= 5    

    "I look over and back up a bit. Samuel is standing there with that big, stupid smile of his."
    BEN "What made you ask that? Can you help me out here?"

    SAM "I was just curious, that’s all."
    "A moment of silence fills the room. As he rushes over to grab the other side of the box and help me place it down, I try to think of something to say, but I can’t think of anything."
    "I feel my face heating up as the box finally rests on the floor and finally say..."
    
    BEN "I joined for myself, that’s all."

    SAM "Really? That’s boring!"
    "He sticks out his tounge as I try to open the locked box."
    SAM "Let me help you out."
    "He starts clawing at the sides of the container. He grabs a pen out of his pocket and starts nudging it in between the boxs opening."
    BEN "H-hey, let go of that, you’re going to bre-"
    "I rush to grab his hand before it is too late.The container pops open, dust flying out all over the room."
    "As the dust clears, I frown, looking down at the container.It looks like a makeup kit and a female soldier uniform.It seems they are storing uniforms of soldiers here not screwdrivers."

    scene mirrorstorage
    $ inventory.append("Broken Hand Mirror")   

    "I stare into the mirror seeing a blank face stare back at me. I have worked my way up to this position, I should be proud. I should be happy but my face says otherwise."
    "As I put down the mirror. I look back at samuel he is staring at the container he has a somber experession, he looked like he was reminiscing on something from the past that has long been forgotten. At least that is what I thought." 
    show ben idle at left
    show samuel redbook at right    
    "A moment of silence fills the room. I try to think of something to say, but I can’t think of anything."
    "I put the mirror back in the box and close the container."
    
    BEN "Can you help me put this back?"
    SAM "S-Sure.."
    "He grabs the other end of the box. He helps me place it down where it was before."
    BEN "Come on, there might be something upstairs."
    "He regains his smile and runs to catch up behind me as I walk up the stairs."

    scene bg militaryentrance
    show ben idle at left

    "As I step upstairs, I feel the temperature drop, but I don’t mind it."
    
    "I glance at the sign on the wall and walk to the left. I feel him yank my arm."
    scene bg maindeskentrance
    show ben idle at left

    show samuel redbook at right    

    SAM "H-hey, where do you think you’re going? You can’t just walk away without telling me!"

    "As I walked up to the main desk, I saw a note on the table."
    "It read: 'Out to lunch. If nessary, use key."
    SAM "Come on we can just buy a screwdriver at the store, there is not a toolbox back their. It will just waste time."
    menu:
        "Use key":
            if rng > 35:   
                "I look down at my watch 10:41 AM. They must be out for an early lunch. I look down at the table and notice a guest list."
                "The list is populated with names none of which I recognize. Except for one. J.J R Jones, the drill instructor, looking at the sheet he is placed an order for item #65912 (A blue toolbox)."
            "I open the gate and pick up the key on the table, I slot the key into the keyhole quickly. Looking back I see samuel looking back at me disapprovingly. I enter the room."
            BEN "There might be a toolbox back here, you never know. I am just checking"
            "I enter the backroom and look around, there are file cabinets, each labled with people’s names. I shrug there dosen't seem to be a screwdriver here. As I am leaving I notice a folder on the ground labled Erika."
            "I pick it up and a coin falls out, picking it up I check the folder for more. As I flip through the pages in the foldera statsfing sound is made as I pull a page out"
            if rng < 20:   
                "MEDICAL RECORDS:"
                "NAME: {s}Erika{/s} Emma"
                "AGE: 28"
                "HEIGHT: 5'5"
                "WEIGHT: 98"
                "SEX: Female"
                "Eye: Blue"
                "Prescriptions: Gabapentin,Amlodipine,Omeprazole,(F)Amnestic,Prednisone"
            else:
                "DEBRIEF:"
                "DATE 2XXX/XX/XX"
                "NAME: Emma Smith"
                "AGE: 28"
                "CAUSE OF DEATH: Suicide"
                "REPORT:The subject was found lifeless while conducting duties in ██████. Agent ██████████ discovered the body at 20:41 with several lacerations to there Carpal region. █████ will be given to family and friends of the victim or on request from onsite personnel."
                "No further investigation will be required."
            "I stare at the page realizing what I am doing. I quickly put the folder back into the shelf. I shouldn't be looking at dead people's stuff I should be focusing on the screwdriver.My thoughts are intrupted by a voice."
    SAM "We can just go to the military store area to get one, you shouldn't be going into random rooms looking for tools."
    "I feel a hand touch my back as I walk past him, but I make it downstairs."
    
    scene bootcampinsideprojectorroomstartm
    "I reach the projector room with Samuel following close behind after a few minutes of walking."
    "The automatic door opens, revealing that the person I told to wait there is no longer there."
    "Thinking back, I never even asked his name, not that it was important anyway."
    "I look at the unplugged projector on the table. I unscrew the film from the projector and put it on the table."
    "Looking to Samuel, I think to myself maybe he isn’t the best person to help me fix this. I press on either way."
    menu:
        "Ask Samuel for help":
            "Samuel looks at me and smiles."
            SAM "Sure, I’ll help. I’ve done this before."
            "He runs over next to me and grabs the screwdriver from my hand."
            "Samuel unscrews the film, takes it out, and puts it on the table. He then unscrews the back of the projector, letting it fall onto the table."
            "I sit back in the chair and watch him as he works. Before I realize it, I doze off."
            "When I wake up, I see the projector is fixed, and Samuel is sitting on a chair reading his book."
            "I honestly didn’t expect him to know how to fix a projector, but I won’t question it."
            "I look at my watch and realize that I need to get ready to move out."
            "I wake Samuel up. He looks visibly shaken."
            SAM "H-huh?"
            "He talks in a groggy voice and looks up at me."
            BEN "We’re going."
            "I say as I start walking out of the room. Samuel follows me as we leave the building."
            return
        "Start removing the projector film (Intelligence roll 40 chance)":
            $ intelligence_level = stats["intelligence"]["level"]
            $ sorted_emotions = sorted(emotions.items(), key=lambda x: x[1]["value"], reverse=True)
            $ base_chance = 30 
            $ skill_level = stats["intelligence"]["level"]
            $ total_bonuses = calculate_total_bonus("intelligence", sorted_emotions)
            call screen roll_screen(base_chance, skill_level, "intelligence", total_bonuses)
            "I kneel down while Samuel sits nearby, reading his picture book. I carefully inspect the projector."
            
            menu:
                "Look at the front of the projector" if _return == True:
                    "I look at the front of the projector. The film is slotted into the projector and being held by a screw."
                    "The film seems like it is still intact and can still be used."
                    "I carefully unscrew the film and place it on the table next to the projector."
                    "With the film removed, I move onto the back of the projector."
                    "I begin to work on the back of the projector..."
                    "Hours later..."
                    "I finish my work and look up from my project only to learn that samuel is no where to be found."
                    "I should show this to the drill instructor anyway I think to myself as I rise from my seat."
                    "I do some streches from sitting down so long and head out the door alone to show the sargent my work..."
                    return

                "Look at the back of the projector" if not _return == True:
                    "I look at the back of the projector. There are four screws holding it in place."
                    "I sit the projector on its side and begin to unscrew the screws."
                    "As I start unscrewing the second screw, Samuel runs over and grabs the projector, sitting it upright."
                    "There’s concern on his face as he says—"
                    SAM "You almost damaged the film. You have to be careful with this."
                    "He begins to help me take the film out of the projector, and we both work on fixing it together."
                    $ add_experience("intelligence", 20)
                    "After two hours, we manage to fix the projector. Samuel seems happy with it."
                    "He then begins to clean everything up and, with a smile, says—"
                    SAM "Let’s go show the Sergeant this!"
                    "After he cleans up the table, I follow him upstairs and out of the building."
                    return

label abandonsamuel:
    "s"

label BackSeat:
    show person_back idle at left
    hide screen HUD

    # Add dialogue and interaction for the person in the back seat
    "You decide to talk to the person in the back seat."
    return

