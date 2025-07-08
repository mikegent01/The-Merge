# name of the character.
#extra
default preferences.text_cps = 30 
default rng = random.randint(1,100)
default menu_initialized = False
transform half_size: 
    zoom 0.5 

image ani1_background:
    Animation(
        "images/bg/Starting_Room/2/satgescene1.png", 0.1,
        "images/bg/Starting_Room/2/satgescene2.png", 0.1,
        "images/bg/Starting_Room/2/satgescene3.png", 0.1,
        "images/bg/Starting_Room/2/satgescene4.png", 0.1,
        "images/bg/Starting_Room/2/satgescene5.png", 0.1,
        "images/bg/Starting_Room/2/satgescene6.png", 0.1,
        "images/bg/Starting_Room/2/satgescene7.png", 0.1,
        "images/bg/Starting_Room/2/satgescene8.png", 0.1,
        "images/bg/Starting_Room/2/satgescene9.png", 99999999.1 # Holds on the last frame
    )
    xysize (config.screen_width, config.screen_height)


default test_room = 0
default benx = 100
default minbenx = -50
default maxbenx = 1300
default beny = 450
default minbeny = 450
default maxbeny = 5000
default walk_frame = 4
default facing_left = False
default jumping = False
default jump_velocity = 0
default gravity = 2
default jump_strength = -15
screen checkKey():
    key "repeat_K_RIGHT" action [SetVariable("benx", benx+25), SetVariable("facing_left", False), SetVariable("walk_frame", (walk_frame + 1) % 5), Jump("walk")]
    key "repeat_K_LEFT" action [SetVariable("benx", benx-25), SetVariable("facing_left", True), SetVariable("walk_frame", (walk_frame + 1) % 5), Jump("walk")]
    key "keyup_K_RIGHT" action [SetVariable("walk_frame", 4), Jump("walk")]
    key "keyup_K_LEFT" action [SetVariable("walk_frame", 4), Jump("walk")]
    key "K_SPACE" action [If(beny >= minbeny, [SetVariable("jumping", True), SetVariable("jump_velocity", jump_strength)]), Jump("walk")]

label walk:
    if facing_left:
        show smolbenwalk:
            xpos benx
            ypos beny
            xzoom -1.0
    else:
        show smolbenwalk:
            xpos benx
            ypos beny
            xzoom 1.0
    jump loop

label loop:
    if jumping:
        $ beny += jump_velocity
        $ jump_velocity += gravity
        if beny >= minbeny:
            $ beny = minbeny
            $ jumping = False
            $ walk_frame = 4
            $ jump_velocity = 0
    $ beny = max(min(beny, maxbeny), 0)
    $ benx = max(min(benx, maxbenx), minbenx)
    
    $ renpy.pause(0.1, hard=True)
    jump loop

image smolbenwalk:
    "images/char/Benjerman/walk/smolbenwalk[walk_frame + 1].png"
image drillsargpickup:
    xysize (config.screen_width, config.screen_height)
    "images/bg/Starting_Room/3/drillsargpickupstart1.png"
    pause 0.6
    "images/bg/Starting_Room/3/drillsargpickupstart2.png"
    pause 0.1
    "images/bg/Starting_Room/3/drillsargpickupstart3.png"
    pause 0.1
    "images/bg/Starting_Room/3/drillsargpickupstart4.png"
    pause 0.1
    "images/bg/Starting_Room/3/drillsargpickupstart5.png"
    pause 0.1
    "images/bg/Starting_Room/3/drillsargpickupstart6.png"
    pause 0.1
    "images/bg/Starting_Room/3/drillsargpickupstart7.png"
    pause 0.1
    "images/bg/Starting_Room/3/drillsargpickupstart8.png"
    pause 0.1
    "images/bg/Starting_Room/3/drillsargpickupstart9.png"
    pause 0.1
    "images/bg/Starting_Room/3/drillsargpickupstart10.png"
    pause 0.1
    "images/bg/Starting_Room/3/drillsargpickupstart11.png"
    pause 0.1
    "images/bg/Starting_Room/3/drillsargpickupstart11.png" # Duplicate frame
    pause 0.1
    "images/bg/Starting_Room/3/drillsargpickupstart13.png"
    # This frame will hold indefinitely as it's the last in the ATL block

# Removed malformed image definition that was here,
# as its content is now part of ani2_background's loop.



image 0drillsargpickupstart0:
    "images/bg/Starting_Room/4/0drillsargpickupstart10.png" #projector on table image
    xysize (config.screen_width, config.screen_height)

image 0drillsargpickupstart:
    "images/bg/Starting_Room/3/0drillsargpickupstart.png" # empty room image
    xysize (config.screen_width, config.screen_height)

image satgescene9:
    "images/bg/Starting_Room/2/satgescene9.png" #standing next to projector
    xysize (config.screen_width, config.screen_height)

image ani2_background:
    xysize (config.screen_width, config.screen_height)
    # Part 1: Initial sequence (plays once)
    "images/bg/Starting_Room/1/ani2stagescene1.png" # Hesitates
    pause 0.4
    "images/bg/Starting_Room/1/ani2stagescene2.png" # Hesitates
    pause 0.4
    "images/bg/Starting_Room/1/ani2stagescene1.png" # Loop once - Hesitates
    pause 0.4
    "images/bg/Starting_Room/1/ani2stagescene2.png" # Loop once - Hesitates
    pause 0.4
    "images/bg/Starting_Room/1/ani2stagescene3.png" # Normal speed
    pause 0.1
    "images/bg/Starting_Room/1/ani2stagescene4.png" # Normal speed
    pause 0.1
    "images/bg/Starting_Room/1/ani2stagescene5.png" # Takes step
    pause 0.2
    "images/bg/Starting_Room/1/ani2stagescene6.png" # Jumps onto chair part 1
    pause 0.15
    "images/bg/Starting_Room/1/ani2stagescene7.png" # Jumps onto chair part 2 / lands
    pause 0.25
    "images/bg/Starting_Room/1/ani2stagescene8.png" # Moves hand
    pause 0.3
    "images/bg/Starting_Room/1/ani2stagescene9.png" # Settles into chair (plays briefly)
    pause 0.1

    # Part 2: Looping idle animation
    Animation(
        "images/bg/Starting_Room/3/3_sitting/sittinganistagescene3.png", 5.8,
        "images/bg/Starting_Room/3/3_sitting/sittinganistagescene4.png", 0.1,
        "images/bg/Starting_Room/3/3_sitting/sittinganistagescene5.png", 0.1,
        "images/bg/Starting_Room/3/3_sitting/sittinganistagescene6.png", 0.1,
        "images/bg/Starting_Room/3/3_sitting/sittinganistagescene3.png", 5.8,
        "images/bg/Starting_Room/3/3_sitting/sittinganistagescene9.png", 0.1,
        "images/bg/Starting_Room/3/3_sitting/sittinganistagescene10.png", 0.1,
        "images/bg/Starting_Room/3/3_sitting/sittinganistagescene3.png", 5.8,
        "images/bg/Starting_Room/3/3_sitting/sittinganistagescene13.png", 0.1,
        "images/bg/Starting_Room/3/3_sitting/sittinganistagescene14.png", 0.1,
        "images/bg/Starting_Room/3/3_sitting/sittinganistagescene15.png", 0.1  # Last frame of the loop
    )

image anistagescene:
    Animation(
        "images/bg/Starting_Room/4/0drillsargpickupstart1.png", 0.3,
        "images/bg/Starting_Room/4/0drillsargpickupstart2.png", 0.3,
        "images/bg/Starting_Room/4/0drillsargpickupstart3.png", 0.3,
        "images/bg/Starting_Room/4/0drillsargpickupstart4.png", 0.3,
        "images/bg/Starting_Room/4/0drillsargpickupstart5.png", 0.3,
        "images/bg/Starting_Room/4/0drillsargpickupstart6.png", 0.3,
        "images/bg/Starting_Room/4/0drillsargpickupstart7.png", 0.3,
        "images/bg/Starting_Room/4/0drillsargpickupstart8.png", 0.3,
        "images/bg/Starting_Room/4/0drillsargpickupstart9.png", 0.3,
        "images/bg/Starting_Room/4/0drillsargpickupstart10.png", 0.3,
        "images/bg/Starting_Room/4/0drillsargpickupstart0.png", 99999.0  # Hold on this frame
    )
    xysize (config.screen_width, config.screen_height)

image projector_hum_animation:
    xysize (config.screen_width, config.screen_height) 
    "images/bg/Starting_Room/5/projector_on1.png"
    pause 0.5
    "images/bg/Starting_Room/5/projector_on2.png"
    pause 0.5
    "images/bg/Starting_Room/5/projector_on3.png"
    pause 0.5
    "images/bg/Starting_Room/5/projector_on4.png"
    pause 0.5
    "images/bg/Starting_Room/5/projector_on5.png"
    pause 0.5
    "images/bg/Starting_Room/5/projector_on6.png"
    pause 0.5
    "images/bg/Starting_Room/5/projector_on7.png"
    pause 0.5
    Animation(
        "images/bg/Starting_Room/5/projector_on8.png", 0.5,
        "images/bg/Starting_Room/5/projector_on9.png", 0.5,
        "images/bg/Starting_Room/5/projector_on10.png", 0.5,
        "images/bg/Starting_Room/5/projector_on11.png", 0.5,
        "images/bg/Starting_Room/5/projector_on12.png", 0.5,
        "images/bg/Starting_Room/5/projector_on13.png", 0.5, 
        "images/bg/Starting_Room/5/projector_on12.png", 0.5, 
        "images/bg/Starting_Room/5/projector_on13.png", 0.5, 
        "images/bg/Starting_Room/5/projector_on12.png", 0.5, 
        "images/bg/Starting_Room/5/projector_on13.png", 0.5, 
        "images/bg/Starting_Room/5/projector_on18.png", 0.5,
        "images/bg/Starting_Room/5/projector_on12.png", 0.5  
    )
image dim_overlay:
    xysize (config.screen_width, config.screen_height)
    Solid("#000000") 
    alpha 0.0      
    linear 1.0 alpha 0.6 

image light_turning_on_effect:
    Solid("#FFFFFF") 
    alpha 0.0
    xysize (config.screen_width, config.screen_height)
    linear 0.05 alpha 0.6 
    pause 0.1
    linear 0.2 alpha 0.0

#######chara images 
image side ben = "images/inventory/inventory_hud/head.png"
image side sarg = "images/char/head/sarg_head.png"
image side sam = "images/char/head/sam_head.png"
# Chara
define BAG = Character("Bagman",color="#b66c12")
define BAL = Character("Baldi")
define BEN = Character("Benjamin", image = "ben")
define BON = Character("Bonehead")
define DAV = Character("David")
define DEE = Character("Deerik")
define DOM = Character("Domonic")
define DRI = Character("Drill Sarg",color="#12a3b6", image = "sarg")
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
define LT = Character("Lieutenant", color="#c4a74a") # Added Lieutenant
define SAM = Character("Samuel",color="#b66c1261", image = "sam")
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
    import pygame
    import threading   
    import urllib
    import urllib.parse # Make sure this is imported
    from http.server import SimpleHTTPRequestHandler
    from socketserver import TCPServer
    import os    
    if 'dimming_layer' not in config.layers:
        try:
            master_index = config.layers.index('master')
            config.layers.insert(master_index + 1, 'dimming_layer')
        except ValueError:
            config.layers.append('dimming_layer')

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
            "met": True,
            "trust": 80,
            "friendship": 54,
            "hostility": 10,
        },
        "Srg.Jones": {
            "met": True,
            "trust": 100,
            "friendship": 0,
            "hostility": 0,
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
    WEBSERVER_PORT = 3000
    PORT = 3000
    # Construct the absolute path to the htmls directory
    HTML_SERVE_DIR = os.path.abspath(os.path.join(renpy.config.gamedir, "htmls"))

    # --- Sanity Check ---
    if not os.path.isdir(HTML_SERVE_DIR):
        print(f"[Web Server Error] HTML directory not found or is not a directory: {HTML_SERVE_DIR}")
        # Optionally, raise an error or notify the user
        # raise Exception(f"Required HTML directory not found: {HTML_SERVE_DIR}")
    else:
        print(f"[Web Server] Serving files from: {HTML_SERVE_DIR}")

    # --- Custom Request Handler ---
    class RenpyHTTPRequestHandler(SimpleHTTPRequestHandler):
        # Override the base class directory to our specific HTML_SERVE_DIR
        # This simplifies path handling significantly. The server will *only*
        # look for files within this directory.
        def __init__(self, *args, **kwargs):
            # Python 3.7+ way to change directory for the handler
            if sys.version_info >= (3, 7):
                 kwargs['directory'] = HTML_SERVE_DIR
            super().__init__(*args, **kwargs)
            # Python 3.6 fallback (less common now)
            # if sys.version_info < (3, 7):
            #    self.directory = HTML_SERVE_DIR # Note: This might need adjustment for 3.6

        # --- Security & Functionality Enhancements ---
        def translate_path(self, path):
            """
            Translate a URL path to a filesystem path within HTML_SERVE_DIR.
            Includes security checks.
            """
            # Decode URL encoding (e.g., %20 -> space)
            path = path.split('?', 1)[0]  # Remove query string
            path = path.split('#', 1)[0]  # Remove fragment
            decoded_path = urllib.parse.unquote(path)

            # --- Path Cleaning & Security ---
            # Make the path relative by removing leading slashes
            relative_path = decoded_path.lstrip('/')
            # Normalize the path (collapses .., handles separators)
            safe_relative_path = os.path.normpath(relative_path)

            # **Crucial Security Check**: Prevent escaping the HTML_SERVE_DIR
            # After normalization, the path should not start with '..' or be absolute
            if safe_relative_path.startswith('..') or os.path.isabs(safe_relative_path):
                print(f"[Web Server Security] Blocked potentially unsafe path: {path}")
                # Return a path deliberately outside the serve dir or non-existent
                # This will likely lead to a 404 naturally by the base handler.
                # We return just the 'unsafe' part to let the base handler fail.
                return "ACCESS_DENIED_INVALID_PATH" # Or just an empty string ""

            # Join the *base serving directory* with the safe relative path
            full_path = os.path.join(HTML_SERVE_DIR, safe_relative_path)

            # --- Debugging (Uncomment to see path translation) ---
            # print(f"[Web Server Debug] Request Path: {path}")
            # print(f"[Web Server Debug] Decoded Path: {decoded_path}")
            # print(f"[Web Server Debug] Safe Relative Path: {safe_relative_path}")
            # print(f"[Web Server Debug] Calculated Full Path: {full_path}")
            # print(f"[Web Server Debug] Full Path Exists: {os.path.exists(full_path)}")
            # ---

            # Return the calculated *absolute* filesystem path
            # The base SimpleHTTPRequestHandler expects this.
            return full_path



        def log_message(self, format, *args):
            """Optional: Suppress logging to console."""
            # Comment out the next line to see default HTTP request logs
            pass

    # --- Web Server Thread ---
    class WebServerThread(threading.Thread):
        def __init__(self, port):
            super().__init__()
            self.daemon = True  # Allows Ren'Py to exit even if this thread is running
            self.port = port
            self.server = None
            self._stop_event = threading.Event()

        def run(self):
            # Check again if the directory exists right before starting
            if not os.path.isdir(HTML_SERVE_DIR):
                print(f"[Web Server Thread Error] HTML directory gone or invalid before start: {HTML_SERVE_DIR}")
                return

            try:
                # Create the server, binding to localhost only on the specified port, using our custom handler
                self.server = TCPServer(("localhost", self.port), RenpyHTTPRequestHandler)
                print(f"[Web Server Thread] Server starting on http://localhost:{self.port}")
                # Start serving requests until stop() is called
                self.server.serve_forever()
                # This line is reached after shutdown() is called
                print("[Web Server Thread] Server stopped.")

            except OSError as e:
                print(f"[Web Server Thread Error] Failed to start server on port {self.port}: {e}")
                print(f"[Web Server Thread Error] Is another application (or game instance) already using port {self.port}?")
                renpy.notify(f"Error: Could not start internal web server on port {self.port}. Port possibly in use.")
            except Exception as e:
                print(f"[Web Server Thread Error] An unexpected error occurred: {e}")

        def stop(self):
            if self.server:
                print("[Web Server Thread] Shutting down server...")
                # Shutdown the server loop (must be called from a different thread)
                self.server.shutdown()
                # Close the server socket
                self.server.server_close()
                self.server = None # Clear the reference
                print("[Web Server Thread] Server shutdown complete.")

    # --- Global Server Instance & Control Functions ---
    _web_server_instance = None

    def start_web_server():
        global _web_server_instance
        if _web_server_instance is None or not _web_server_instance.is_alive():
            if os.path.isdir(HTML_SERVE_DIR): # Only start if dir is valid
                print("[Web Server Control] Starting web server...")
                _web_server_instance = WebServerThread(WEBSERVER_PORT)
                _web_server_instance.start()
            else:
                print(f"[Web Server Control] Cannot start server, HTML directory is invalid: {HTML_SERVE_DIR}")
                renpy.notify(f"Error: Cannot start web server. HTML folder missing or invalid.")
        else:
            print("[Web Server Control] Server already running.")

    def stop_web_server():
        global _web_server_instance
        if _web_server_instance and _web_server_instance.is_alive():
            print("[Web Server Control] Stopping web server...")
            _web_server_instance.stop()
            _web_server_instance.join(timeout=2.0) # Wait briefly for thread to finish
            if _web_server_instance.is_alive():
                print("[Web Server Control Warning] Server thread did not stop cleanly.")
            _web_server_instance = None
        else:
            print("[Web Server Control] Server not running or already stopped.")

    start_web_server()


    config.quit_action = stop_web_server


    def open_html(filename_no_ext, last_label=None):

        if _web_server_instance is None or not _web_server_instance.is_alive():
             print("[Open HTML Error] Web server is not running. Cannot open HTML.")
             renpy.notify("Internal web server is not running.")
             return

        # We *construct* the URL to *include* /game/htmls/ because that's what
        # the browser will request. The server handler will then map it correctly.
        # VVVVV THIS LINE IS NOW CORRECT VVVVV
        base_url = f"http://localhost:{WEBSERVER_PORT}/{filename_no_ext}.html" # Use WEBSERVER_PORT

        query_params = {}
        if last_label:
            query_params['lastLabel'] = last_label

        # Add query parameters if any
        if query_params:
            encoded_params = urllib.parse.urlencode(query_params)
            full_url = f"{base_url}?{encoded_params}"
        else:
            full_url = base_url

        print(f"[Open HTML] Opening URL: {full_url}")
        try:
            success = webbrowser.open(full_url)
            if not success:
                print("[Open HTML Warning] webbrowser.open() reported failure. Is a browser available?")
                renpy.notify("Could not open web browser.")
        except Exception as e:
            print(f"[Open HTML Error] Failed to open browser: {e}")
            renpy.notify(f"Error opening browser: {e}")

    def open_html(name, label_value):
        """Opens the specified HTML file, including /game/htmls/ in the URL."""
        safe_label = urllib.parse.quote(label_value if label_value else "Unknown")
        # Construct the URL *with* /game/htmls/ included
        url = f"http://localhost:{PORT}/{name}.html?lastLabel={safe_label}"
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
        "Tissue": {
            "type": "junk",
            "weight": 2,
            "description": "A Tissue to wipe away your sorrows.."
        },     
        "Wet Tissue": {
            "type": "junk",
            "weight": 2,
            "description": "A Wet Tissue...yuck!"
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
        "Classified Mission Sheet": {
            "type": "tool",
            "weight": 2,
            "description": "A sheet I should not have given to me by a friend."
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
        },
        "Pistol": { # Added Pistol
            "type": "weapon",
            "weight": 2,
            "description": "A standard issue sidearm. Reliable in a pinch."
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
        elif item == "Tissue":
            renpy.notify("You blow your nose")
            remove_item("Tissue")
            add_item("Wet Tissue")
        elif item == "Wet Tissue":
            renpy.notify("You place the wet tissue on the floor carefully.")
            remove_item("Wet Tissue")
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
        elif item == "Classified Mission Sheet":
            open_html("001", last_label)
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
    $ set_room_temperature(72)
    $ add_item("Classified Mission Sheet")
    $ inventory.append("Classified Mission Sheet")
    $ inventory.append("radio")
    play music "audio/Music/Boot Camp/boot_camp.mp3" volume 0.5 # Assuming 'boot_camp' is the correct filename
    scene ani1_background with None
    show screen stagecurtians
    BEN "I can only feel excitement, as I finally go to sit down."
    scene satgescene9 with None
    BEN "We are going on a real mission, no more training, no more drills. I finally can put my skills to good use."
    BEN "I have accepted my fate long before I woke up this morning knowing what this job entailed"
    BEN "and I intend to make this mission a success by myself."
    scene ani2_background with None
    "I sit down on a wooden chair."
    "people around me muttering and talking."
    "The dampness from the old moldy brick walls."
    scene drillsargpickup with None
    "And the sweat of the soldiers who just got back from training."
    scene 0drillsargpickupstart with None
    "Almost distracts me from the fact that I forgot to put on my uniform this morning."
    "The soldiers all sit in rows of chairs, laid out in a linear sequence, ridged but not sturdy."
    "The room is packed with soldiers and people."
    scene anistagescene
    "A thud sound is made from the front of the room. A metallic box item is placed on the table"
    "the box having a single lens at the front of it and two films atop of it."
    scene 0drillsargpickupstart0
    "The box is dusty; it looks familiar but it is alien to me. As I deliberate on this"
    "a clicking sound plays, and after a moment the room goes quiet."
    "a soft hum starts emanating from the machine."
    scene projector_hum_animation 
    "The box whirls to life, it clicks for a second, and then for only a second there was nothing. Another hitch and there was light."
    show dim_overlay onlayer dimming_layer
    "The light in the room dims, the creaking of the chairs stop" 
    "a familiar figure stands directly infront of the light. Ridged and firm"
    "the familiar figure stands at attention,"
    "and another hitch is herd from the box."
    "The light shines bright as the box shows multiple images of destroyed suburban cities" 
    "the images are shown one by one, ending on the statue of liberty."
    "The silence is broken when drill sergeant Jones begins speaking "

  #  show drill_sarg_talk at right
    DRI "Men, these are the facts as I understand them: approximately 5 hours ago a class A event occurred near Ruckersville Virginia."
    DRI "We promptly sent a Incident Relief Division to investigate the scene and received reports of a rift in the earth opening up "
    DRI "and several sightings of unknown creatures before we lost contact due to power outages."
    DRI "You will have two jobs: one team's job will be to find out what happened to the team and to terminate every threat,"
    DRI "and the other team will be in charge of securing a suspected target that caused this mess."
    DRI "This is not simply a security problem anymore as fellow members of the army and civilians lives are at stake."
    DRI "I have full confidence in all of you; you are the best unit in the force and I expect you will be ready."
  #  hide drill_sarg_talk

    "The room remains silent with no one but me moving there eyes from the Sargent as he talks" 
    "there is a tense anticipation for what he will say next."
   # show drill_sarg_talk at right
    DRI "This box here is a projector, here is of upmost importance, while it may look mundane and normal…"
    "he takes out the tape and a sound begins playing"
    DRI "But These tapes it plays are capable of playing sounds at a higher decibel frequency than humans can hear."
    DRI "These tapes right here do contain image data, but they also contain data that will play sounds at high decibels" 
    "that are able to plug these rifts."
    DRI "I am not to well versed in the science behind it, but I am told if this tape is played at the center of one of these rifts,"
    DRI "they may close and return to normal. Therefore this tape will be designated as a class A important object."

    "As I look at the projector I notice a hitch in it."
    "The projector seems to stall for a second before starting up again."
    DRI "We are to deploy to a nearby military base tonight. We won’t close these rifts tonight"
    "as we still need a key component to making this technology work."
    DRI "You will be briefed further on this situation during the beginning of the mission tonight."
    DRI "You will also receive authorization to classified information.If you are unable to keep a secret please see me." 
    "That is all You are hereby dismissed."
    hide dim_overlay onlayer dimming_layer 
    show light_turning_on_effect 

    "As the lights turn on and the room so does the sound, people start talking amongst themselves"
    "some personal start leaving the room."
    "I feel a slight tap on my shoulder it is from one of my “friends” private Samuel."
    SAM "Psst hey Benjerman"
    "he then hands me a sheet of paper"
    SAM "I was told you would like this it is a report on what happened, there is some stuff in there that I can’t even understand."
    "I feel the sheet fall on my lap as he places it there."

    "I look up at the projector it hitches again as the drill Sargent messes with the plug trying to unplug it."
    "He moves it back and forth in a wiggling motion but it seems to be stuck."
    "It eventually pops out and a spark occurs at the outlet and the projector starts heating up and smoking."
    DRI "..."
    "The drill sargent looks visibly concerned and than looks directly at me staring at him."
    DRI "You, meatbag your just who I need!"

    "I arrive at his location he looks down at me with a scowl."
    DRI "This projector is broken, I am not sure how it broke and it looks like your not doing anything of importance" 
    "therefore your in charge of fixing it"
    "I look at him semi annoyed, he looks back"
    DRI "do you understand what you need to do?"
    BEN "yes sir!"
    DRI "sound off like you got a pair"
    BEN "SIR YES SIR"
    DRI "good you are dismissed."

    "As I turn around I notice two people sitting in there seats, prehaps I should talk to one of them and ask them for help."
    show screen HUD
    show screen tutorial_screen
    show screen checkKey   
    show smolbenwalk:
        xpos benx
        ypos beny
        xzoom -1.0

    window hide 
    $ renpy.pause(hard=True)

label FrontSeat:
    hide screen HUD
    hide screen tutorial_screen
    hide screen checkKey    
    window show     
    scene bootcampinsideprojectorroomstartm # Or appropriate scene
    show ben neutral at left
    "Although I much rather do this myself I have no other options, I walk up towards the front seat the man is small in stature the only defining trait about him I can notice is his turban."
    show sultan_talking_pose at right
    SUL "..."
    "Regrettably walking up to him he doesn’t notice me I decide to observe what has taken so much of his attention."
    "As I peer closer at him to find out what he is fiddling with I realize he is trying to light a cigar, he is unable to get the match to light."
    "I wait another few seconds before questioning him"
    BEN "What are you doing?"
    hide sultan_talking_pose
    show sultan_talk_pose at right
    SUL "Nothing bro don't worry about it"
    BEN "You know there is a fire sensor above your seat right?"
    SUL "Look bro I barely even know you; you don’t talk to anyone and now you decide to talk to me? What do you want money?"
    "I wait for him to continue feeling the paper that Samuel gave me crumple in my hand."
    SUL "Look” He holds out a $10 bill giving it to me “Just don't tell anyone what you saw okay?"
    BEN "I refuse to take the money instead asking him to help me."
    BEN "I need you to go and help me out with something."
    SUL "What is it bro?"
    BEN "Do you have any idea on how to fix a projector?"
    SUL "P-Projector? You mean that thing the sarg was showing off bro you broke it?”"
    "He gets up quickly and begins packing up his stuff"
    SUL "N-no no I wouldn’t know anything about the projector."
    "He wips has bag around and puts it on his back. He begins to walk out"
    BEN "Wait! Listen to me"
    "he continues to walk out before I run up to him and place a hand on his shoulder."
    BEN "We are both on the same side here it’s the drill sergeants fault listen."
    "A quiet spark is heard only for a moment and smoke comes out from in front of the man he stops and takes a deep breath and says"
    SUL "I would stay away from that projector but If you can’t fix it yourself I would ask Samuel for advice. He seems to follow you around anyway for some reason."
    "He walks out of the room."
    hide sultan_talk_pose

    "As I walks up to the projector I look at the pulled out plug and the electrical residue next to the outlet, I pick up the film the projector left on the desk and look at it"
    "there is crossed out text on it AAXA SCP-A01 I put the film down and pick up the projector itself feeling the hard and bumpy texture looking at the back of it there appears to be a panel held in with screws"
    "as I look at the projector I feel a tap"
    show drill_sarg_talk at right
    "the drill Sargent is still standing there staring at me, I think to myself how long could he have been there waiting before asking him for a screwdriver."
    DRI "I have a very important meeting to attend to, once I am back the mission will begin. Id recommend looking for it yourself,"
    DRI "you need a specialty screwdriver for this and I am not too sure were we keep them. Why don’t you go ask the people at the main desk maybe they can help."
    hide drill_sarg_talk
    hide ben neutral

    jump OutsideAfterScrewdriverAdvice

label BackSeat:
    hide screen HUD
    hide screen tutorial_screen
    hide screen checkKey    
    window show    
    scene bootcampinsideprojectorroomstartm
    show ben neutral at left
    "I head towards the backseat, the person in the backseat seems to have something over there head, it looks like a paper bag."
    show bagman_default at right
    BAG "..."
    "There is a brief moment of hesitancy before I recoil once than I tap the tall man with the bagged head on his shoulder."
    "He turns around shocked revealing there to be a crudely cut out face on the bag."
    BAG "..."
    "I couldn’t tell the emotion on his face but I could feel it. I could feel the heat coming out of his mask. I can hear his heavy breathing,"
    "the bag motioning in and out slowly and rhythmically. I took a slight step back but than he no it spoke up, the bag made a slight ruffling sound"
    "and a gruff and heavy voice came out of what was constraining it."
    BAG "yes c-can I he-help you"
    "the man voice cracks I with an ear pinching tone, there is a slight squeak in his tone."
    "I do a silent sigh of relief at him in the eyes"
    BEN "The projector is broken and the sarge wanted me to fix it. Do you have any advice or knowledge on how to fix this."
    "I wait my response until he speaks up"
    BAG "y-you will need a specialty screwdriver and t-to be careful that thing is dangerous…."
    "He takes another deep breath but not as deep as before he continues on with"
    BAG "I-if I were you I wouldn’t even touch that thing, I-…"
    "He deliberates on his words for a moment; as he does the feeling of unease returns from before the air becomes thicker and the bag on his head becomes more animated he continues on"
    BAG "I can’t say any more…. I-I have to go."
    "He quickly continues packing up his supplies and rushes out, I don’t stop him."
    hide bagman_default

    "With that advice I decide that I shouldn’t touch the projector and I should look for the screwdriver instead as I am leaving I hear the drill Sargent call out to me."
    "I realize he is still standing. He is observing me, I think to myself how long could he have been there waiting before asking him for the specialized screwdriver."
    show drill_sarg_talk at right
    DRI "I have a very important meeting to attend to, once I am back the mission will begin. Id recommend looking for it yourself,"
    DRI "Why don’t you go ask the people at the main desk maybe they can help."
    hide drill_sarg_talk # Corrected from drill_s_talk
    hide ben neutral

    jump OutsideAfterScrewdriverAdvice

label OutsideAfterScrewdriverAdvice:
    scene bg_outside_projector_room
    show ben neutral at center
    "Having no other choice I walk outside."
    "As I walked outside I felt the cool stale air from the indoor air conditioner, I smile as the meeting is finally over."
    "I feel the drill sargent rush past me as he heads to his meeting. I watch him run off to the left in a hurry from waiting for me for this long"
    "until I look to the right seeing someone I recgonize. My smile quickly fades into a frown as I look up to see a face I did not want to see."
    "It is Samuel, I think to myself if it is really worth it talking to him."
    show samuel_redbook at right
    "It could lead me into more trouble than its worth I finally decide"
    menu:
        "follow him":
            jump keepsamuel
        "go on my own":
            jump abandonsamuel

label keepsamuel:
    scene bg_outside_projector_room_no_samuel
    hide ben neutral
    show ben neutral at left
    show samuel_redbook at right
    "As I contemplate on my life choices, I finally decide I should go up to him. I approach him as he seems to be reading a book."
    "I glance at the book he is reading it is a red book with a strange symbol on the front of it, it appears to be put in the middle of other shapes making a sun shape."
    "There is text on the book, I don’t understand what it means but it is another language perhaps italian it reads “Nitimur in vetitum”."
    "I start to have second thoughts of my decision to talk to him as I am certain Samuel can’t read Italian. I decide to speak up anyway."
    "I clear my throat and clearly say"
    BEN "Can you help me with something?"
    SAM "This isn’t about another girl is it."
    BEN "What are you talking about?"
    SAM "Oh don’t worry I won’t tell anyone ill help you out."
    "He quickly puts his book in his spare hand and asks"
    SAM "So what is the problem."
    BEN "I need to fix the projector from the meeting we just had."
    SAM "..."
    BEN "It apparently broke down and the sarg blamed it on me."
    SAM "Did you actually not break it, this isn’t like last time is it?"
    BEN "Last time something broke wasn’t my fault either, you just got to trust me on this."
    SAM "Fine but I am leading this time"
    hide samuel_redbook
    hide ben neutral
    scene bg_storage_room
    show ben_idle at left
    show samuel_normal_pose at right
    "I am forcably pulled down the hallway until he stops and lets go of my arm. I feel a slight pain as he twisted my arm when grabbing it. Looking back up I see him approaching a electric door."
    SAM "all spare parts and supplies should be in here"
    "He approaches a keypad next to the door and starts inputting in a passcode. As he starts typing I hear a loud buzz and a red light appears above the keypad."
    "He laughs a bit and enters the code again another buzz but this time it opens."
    "I follow him inside the storage room, it is pitch black inside the room but with a click the light turns on."
    "A single fluorescent light is shining down lighting up the whole room my attention is drawn to the center of the room there is a box with a paper note attached to it."
    "However I am quickly distracted as it seems Samuel has other ideas. I follow him as he starts opening up draws presumably looking for the screwdriver."
    "He is going all over the room making a mess he bumps into me and a loud crash is heard as boxes fall ontop of us."
    "I try to get up but he is too heavy, I annoyingly shout"
    BEN "Your making a mess can you stop!"
    "He pushes the boxes off of him and looks down at me his face slightly red "
    SAM "I-I took it too far, I just got excited I haven’t done something this fun in a while. I was too forceful I am sorry."
    "He offers me his hand and I accept it as he helps me up."
    BEN "y-yeah why don’t you check out that box over there and I will clean this place."
    "I start to pick up the boxes from the floor and put them back into place, luckily most of them were empty."
    "I hear a slight rip from behind me but i ignore it, I hear him walk towards me and say"
    SAM "yeah there was nothing in here but a stupid red pen and this."
    "I place the box down were it was before and I see him holding I note the text on the note reads “Property of DARPA”."
    BEN "well this was a failure."
    "He closes the door and re-enables the lock as we both leave"
    SAM "Maybe we can check out the main desk, they might have a screwdriver"
    "I reluctantly agree and follow him to the main desk."
    hide samuel_normal_pose
    hide ben_idle

    scene bg_main_desk_area
    show ben_neutral at left
    show samuel_normal_pose at right
    "As I approach the main desk I can smell a murky smell in the air, my eyes tear up as I approach the two shadowy figures."
    "Looking down at the floor it seems there is a wet floor sign and a weird liquid substance on the floor."
    "I recently head towards the two shadowy figures until I can see them in plain view there true form."
    "The two shadowy figures are cardboard cutouts with a speaker and microphone attached to it. A advanced drive through so workers can sit inside in nice cool air conditioning lazing around while also take orders."
    "I am startled as I hear a fuzzy voice come out from one of the figures speakers."
    Q2 "What do you wAnT, mAk- it qu-ck."
    BEN "YOU WOULDN”T HAPPEN TO KNOW WERE A SCREWDRIVER IS WOULD YOU? ONE TO REPEAR THE PROJECTOR."
    "The cardboard cutouts remain motionless but a response is heard"
    Q2 "Y-u don- have to scream, what projector?"
    "I explain to the cutouts the whole story in my normal voice, they eventually understand and say"
    Q2 "No I do not, This may be the main desk of this building but our building is not ready and equipped with many of the modern amenities the other buildings have.”"
    "Me and Samuel turn around and he suggests we check upstairs next, we begin walking , I continue to listen to the sound of the speaker as we walk farther away"
    Q2 "This building is the oldest in the camp. We would have to go through dozens of folders and bi--------"
    "The sound fades out as we continue onwards we reach the maintenance hallway, Samuel suggests we take a detour in there to check if a screwdriver is there in the maintenance hall, having no real other leads I agree and follow him inside"

    scene bg_storage_stairwell_fixed
    show ben_idle at left
    show samuel_book_pose at right
    "I quickly search around the hallway only finding empty storage containers."
    "I see a stairway to upstairs I see it is blocked by a green container, it seems like It feel from the shelf it was one as I approach it to pick it up,"
    "I hear Samuel heading towards me, I quickly spin around to see samual book in one hand and paper in the other."
    SAM "Did you find something interesting?"
    "he looks at me and proudly presents it"
    SAM "check this out"
    "he hands me a paper, it seems to be a note of some kind."
    SAM "It was on the main desk I was able to snatch it."
    BEN "how didn’t they notice?"
    SAM "I was able to tell they were too far to do anything and they couldn’t actually see anything from those cardboard cutouts. If the sarg were to see that liquid on the floor he would lose his shit."
    "Well either way if they saw it or not I read the paper"
    BEN "Please discard and shread this message after reading this. The only way I am able to access these files at work is with a FTP setup,"
    BEN "connecting to this address is 136.228.116.222 through one of the computers should redirect to the main server. Only use this for file transfer once the worm is on the system you can power down."
    BEN "Well at least it is something"
    "I say as I bend down and pick up the green container on the floor, As I try to lift it up I realize it is too heavy, I decide the best option is to sit it upright I hear a loud sound in my ear"
    SAM "Hey, what made you join the force?"
    "I drop the box and it almost crushes my leg. I look over and back up a bit, samuel is standing there aloof."
    BEN "Be careful will you, this thing is heavy?"
    SAM "I was just curious thats all."
    "A moment of sclince fills the room I try to think of something to say but I can't think of anything... I feel my face heating up as I remember something and I finally say"
    BEN "I joined for myself thats all."
    SAM "Really that's boring"
    "he walks over to me as I continue trying to open the box."
    SAM "Let me help you out"
    "he starts grabbing at the sides of the container."
    BEN "H-hey let go of remember what I said befor-"
    "the container pops open dust flying out all over the room."
    "As the dust clears I frown looking down at the container it looks like an old computer is inside it, There is a makeup kit inside the box along with a female soldier uniform."
    "I pick up the mackeup kit and inspect I see a broken hand mirror inside."
    $ inventory.append("Broken Hand Mirror")
    "I pick it up and stare back at myself for a good few seconds. I sigh"
    BEN "I told you to be careful. Your breaking other peoples stuff, look what you did to this mirror!"
    "I yell showing him the broken mirror. The room goes silent as I put the mirror in my pocket."
    "I begin walking upstairs, I hear Samuel quickly follow behind me, I think to myself about the mirror I can't fix something that is broken, even if I could nothing would change anyway."
    hide ben_idle
    hide samuel_book_pose

    scene bg_military_entrance
    show ben_neutral at center
    "as I step upstairs I feel the cool AC and an exit to the sweaty basement I feel the tempature drop and the wind hit my face. I don't give it a second thought though."
    "I glance at the sign on the wall there are two ways to go left and right. Reading the signs one says armory to the left and the other says loading bay to the right."
    "I start walking to the right but I just remembered something. I need to pick up my new uniform and weapons for the mission."
    "If the mission is starting tonight I should probably pick them up soon as processing should take around an hour."
    "However if I go now I may not have enough time to fix the projector as fixing it seems like an impossible task already and I already spent a long time just looking for a stupid screwdriver."
    "I need to decide what is more important the sergeants order or my own safety"
    menu:
        "Get Army Uniform":
            jump getuniformwithsamuel
        "Go get screwdriver":
            jump getscrewdriverwithsamuel

label getuniformwithsamuel:
    scene bg_military_entrance
    show ben_neutral at left
    show samuel_normal_pose at right
    BEN "Safety always comes first I think to myself as I turn around heading towards the supply depo."
    "I hear Samuel quickly follow behind me as he starts trying to make conversation."
    SAM "You know the two guys that run the stands where we are headed right? I spoke to them this morning they were kind of depressed. The sarg has been calling them heady and army,"
    SAM "it seems it caught on with some of the recruits. I would try to keep it easy on them."
    "I mentally take a note of what  as we pass by a door that takes my attention it has a paper that has the text COMPUTER LAB drawn onto it."
    "The text is slopply written and in blank sharpie marker ink. The paper is ripped a part of it torn off and on the floor."
    "It also seems like someone or something dented the door. The door is dented enough to see a small crater where the impact was it was about as big as my head."
    "I see that Samuel is getting farther from me and I rush ahead to catch up to him, he seems to notice that I was looking at the door and asks"
    SAM "Do you want to check it out? I think we still have time."
    BEN "No, duty is more important. Maybe if we ever have down time after this we can go check it out together."
    SAM "Your loss."
    "and we both continue. There is a maintenance door that leads into a damp garage area."

    scene bg_elevator
    show ben_neutral at left
    show samuel_normal_pose at right

    "The room is pretty empty aside from two stands setup opposite to an elevator. The room is cold and dark only illuminated by the lights of the elevator and stands."
    "The two people stand there staring into nothingness the sound of a cheerful tune coming from the stand on the left."
    "The stand on the left labeled weapon stand has a bill board on it with the text “Todays menu” and a list of guns ranging from small pistols to large machine guns I can only dream of using."
    "The person manning the stand stands flamboyantly a unmoving smile, his eyes beat red in medieval knight armor, its shine contrasting the painted on pastel background behind him."
    "He seems to be breathing in and out waiting patiently for the next person to arrive at his stand. His most notable feature being his hands."
    "His hands seem to unusually contort at the wrists and his hands are stuck in twisted positions almost like his hands have no bones at all."
    "I feel a slight tap on my shoulder I choose to remain focused on what lay before me looking to the right there is at least some semblance of normalcy as I see a hooded man in all red robes."
    "The stand looks normal enough until I took a closer look first the red hood masking his face, there is something perduring out of his face. It is way too big to be a simple bump there has to be something more."
    "Second what’s behind him, its not a pastel wallpaper but products. He has many products behind him some seemingly unrelated to armor. There are some strange devices I am unable to recognize."
    "Questions pass through my mind like were did he get these from? why did he choose to display them so publicly?"
    "Finally that music, it is slow and methodical yet cheery. It is being played from a old stereo, the tone is almost hypnotic with how slow and droning the loop is."
    "I feel a tap on my shoulder and see Samuel he looks concerned"
    SAM "Are you alright? You have been staring into space for a few minuets , I can order the armor if your scared."
    BEN "No, I am fine. I was just a bit spaced out."
    SAM "You sure, maybe we should go back?"
    "I ignore his question and decide which stand I should approach."
    hide samuel_normal_pose
    show knight default at center
    KNIGHT "..."
    "As I approach the man he seems to grow. His shadow looming over me, he has turned into a giant. his armor shining in the low light of the room, his smile getting wider, a slight mumble coming from it."
    "I was not sure how a face can even look like this he was no man he was a monster."
    "I feel another tap and finally give in looking behind me samuel put his hands on my shoulder almost as a comforting motion to tell me its going to be okay."
    show samuel_sholder_pose at right
    "I take a deep breath and begin the conversation"
    BEN "I am here to place an order in for a new uniform"
    "its face doesn’t move he stands there eyes unblinking almost like he is judging me, asking me “why did you come here”."
    "I almost take a step back but Samuel walks in front of me and loudly states"
    SAM "my friend is here to pick up a new gun!."
    "As I realized my mistake from earlier I notice Its eyeballs move quickly homing in on Samuel almost like they are locking on to a new target."
    "I prepare for impact before I see the monster come to life its bright smile turns into a frown, his eyes slowly start blinking and his hands, his broken hands move up to his face and pull something out."
    "It is small by I see and hear it quite clearly, a pair of earphones the volume so loud I can make out it was playing some k-pop music."
    KNIGHT "What was that you said again."
    "The façade has vanished this was no monster, it was a man a broken tired man."
    "Samuel repeats his question and the man replies in a now defeated still raspy, monotone voice with"
    KNIGHT "I will put in a order for you it should be done before your mission starts."
    "He flips a small switch and a tube comes down from the ceiling."
    KNIGHT "So what kind of weapon do you want to use?"
    menu choice_of_weapons:
        "Pistol":
            $ player_weapon_choice = "Pistol"
            jump process_weapon_choice
        "Rifle":
            $ player_weapon_choice = "Rifle"
            jump process_weapon_choice
        "Shotgun":
            $ player_weapon_choice = "Shotgun"
            jump process_weapon_choice
        "Grenade Launcher (Dream Big)":
            $ player_weapon_choice = "Grenade Launcher"
            jump process_weapon_choice

label process_weapon_choice:
    KNIGHT "Good choice, I wouldn’t personally go for that one but oh well."
    "He places the paper back in the tube and flicks a switch. I watch as the paper quickly goes up into the unknown."
    KNIGHT "Anything else?"
    BEN "..."
    "he than grabs his headphones and puts them back in his ears."
    hide knight default
    hide samuel_sholder_pose
    show ben_neutral at left
    show samuel_normal_pose at right

    "Perhaps I was overthinking everything and this would go more smoothly than I have previously thought, as we walk over to the next stand I look over to Samuel and he gives me the thumbs up."
    "We than head over to the next stand [right stand]"
    show red_hood default at center
    RED_HOOD "..."
    "I take a deep breath as I approach the stand, the hooded man seems to notice me his head moves up and  in a low voice"
    RED_HOOD "Hello you two, you must be benjamin right? Today’s reading said you would come."
    BEN "Who told you I would come?"
    RED_HOOD "No matter, I have the order you were about to place ready."
    "He hands me a new uniform the right one."
    $ inventory.append("New Uniform")
    SAM "Alright, lets get you out of that uniform, lets head to the bathroom."
    BEN "I can’t accept this, what just happened is just too convenient. I have an urge a pulse even I need to figure out how this happened no matter the cost."
    BEN "hold up a second"
    "I put my hand up to Samuel as I face the man I say"
    BEN "How the hell did you know what I was going to order!"
    RED_HOOD "You best not seek knowledge that you are unprepared to learn about for the truth is far worse than what you should know."
    SAM "..."
    BEN "Cut the bullshit, who told you?"
    RED_HOOD "..."
    BEN "Tell me! Tell me now!"
    "and sighs he lifts his hood up a tiny amount revealing for only a second a single horn sticking out of his head before he puts the robe back down."
    RED_HOOD "Both of you mustn’t come back here for I have revealed some of my inner self."
    "we both walk backwards my uniform in hand until he are a safe enough distance from him."
    SAM "we will talk about this later."
    hide red_hood default
    hide samuel_normal_pose
    hide ben_neutral

    scene bg_main_desk_area
    show ben_neutral at center
    "Me and Samuel head to the bathroom. I tell Samuel to wait outside as I enter the bathroom and begin to undress."
    "First my shirt comes off than my pants fall down, I grab the new uniform feeling how it was perfectly, I feel as the stiff fabric stretches with my skin as I pull my new pants up"
    "the pants almost being too big for me if it wasn’t for the belt holding them in place, I think about how dirty this uniform will get after the mission how this may be the only one time I see it clean and in prefect condition."
    "I feel the shirt slip on next as I slide it down my muscular body looking in the mirror I see myself and hype myself up for the mission to come."
    "I feel the polyester touch across my body as it rigidly comes into place. Next comes on the shoes they are heavy put reliable I than grab my helmet putting it on my head"
    "seeing the pointy metal come out of the top I think to myself it may be able to be used as a tool."
    "I than take one last look at myself in the mirror and leave the changing room."
    hide ben_neutral

    scene bg_elevator
    show drill_sarg_talk at center
    show samuel_normal_pose at right
    "As I leave I see the drill Sargent talking to Samuel outside he looks disappointed"
    DRI "So you were unable to fix this old thing? Well I hope you find a mechanic during the mission because we are getting ready to leave the base."
    DRI "Follow me outside you two maggots we are already late as is."
    "His frown worsens"
    "He looks to Samuel and chuckles"
    DRI "I know you two like chatting so I am separating you into different squads. This mission is important and I wouldn’t want you to screw this up. You will follow me do you understand"
    BEN "sir yes sir!"
    SAM "sir yes sir!"
    "and begin to follow him outside as the garage door opens up lighting up the room we see a line of soldiers waiting outside all rigid in form waiting for there orders."
    "We both head into our respective squads…"
    jump outsidewithuniform

label getscrewdriverwithsamuel:
    scene bg_military_entrance
    show ben_neutral at left
    show samuel_redbook at right
    BEN "Contemplating my options I figure that I might as well start this pointless search for my screwdriver, I try to forget about the screwdriver."
    "I head to the right as me and Samuel walk to the right he begins to start some small talk"
    SAM "that book from earlier –"
    BEN "Yeah don’t worry about it, I won’t tell anyone you read picture books."
    SAM "Hey! Its not a picture book."
    "He moves the book back into both hands and begins reading"
    SAM "There exists two states in this world, the is and isn’t."
    BEN "I already told you, I won’t tell anyone you don’t need to make this worse than it already is"
    SAM "Once the lost artifacts are bought into one place…"
    "I move my hand and close the book myself as we walk and say"
    BEN "look man, I know that story is probably great and all but we have bigger problems we need to solve. Like getting that screwdriver!"
    SAM "This has to be connected to the mission, those scenes on the projector there similar to what is written in this book."
    "I dismiss his claim and we both continue onwards towards a giant window."

    scene bg_city_freedom
    "We both stop a bit and admire the outside, The window reveals open roads going into other buildings that look smaller from here than they actually are."
    "We can see trucks and military cars driving on the paved cement. We watch as two people in a jeep make hand motions talking to each other there car driving off into other facilities and the unknown."
    "We can see the calm sky seeing the morning sun come up over the horizon the clouds shapes are uniform."
    "We are at peace until the ground starts shaking, looking up the clouds disperse and open a fleet of osprey aircraft come whirling in and head towards the front of the building we are in."
    "We both can see and feel the aircraft fly above us disrupting the peace."
    "I hear someone stand, looking behind me I see the turban man from earlier getting up from his seat."
    hide ben_neutral
    hide samuel_redbook
    show sultan_talking_pose at center
    RAM "You never got my name did you?"
    "Looking at him with his lit cigar in his mouth  staring at me with tired eyes"
    RAM "You can call me the ram."
    "He takes another puff of his cigar."
    show ben_neutral at left
    show samuel_normal_pose at right
    "Me and Samuel stare at him for a few seconds processing that odd sounding name before he looks at my hands and looks back up at me and says"
    RAM "So you really are going to fix that projector bro?"
    "He gives me a side eye before sitting down again"
    RAM "I dealt with something similar on a previous mission."
    "Me and Samuel decide to sit down and listen to his story, he continues"
    RAM "I was in charge of protecting a audio device, it would play a simple lullaby it was meant to calm someone known as the giant . My squad was a team of four, but we lost one during the mission."
    RAM "The mission started off poorly. We were all ill equipped. Me and red hood were in charge of recon while the knight and private p were supposed to play that damn device."
    SAM "what happened to the other two people"
    RAM "That is their story to tell not mine."
    RAM "The damn thing ran out of battery” His face scrunches up and his anger builds “The main fucking device meant to save us ran on double a batteries"
    "he coughs cigar smoke coming out of his mouth he seems to be less tense than before as "
    RAM "This place is a joke. I wouldn’t trust that projector for a second."
    BEN "We were given orders to fix this projector and we will fulfill them"
    RAM "..."
    "I watch as the smoke cloud rises from his cigar it slowly rising up and disappearing into the air. He shakes his head"
    RAM "This is why I stayed in the military, to prevent people like you from dying"
    "he sighs looking defeated"
    RAM "This stress has been getting to me recently that this mission may be another failure, that we may not come back alive again."
    SAM "We won’t let that happen."
    RAM "I almost started a small fire in the storage room."
    "Me and samuel look at each other we both have been their earlier today and didn’t see him there he continues"
    RAM "I was smoking a cigar and I tossed it on the floor carelessly I was going to let it stay their but once I heard you two trying the combination to the storage room; I stomped it out and picked it back up quickly. Luckly, you got the code wrong at first."
    "I look at Samuel he is slightly embarrassed, ram notices this but does not say anything"
    RAM "I was able to sneak out of the room but I felt really guilty after about what I have done. I don’t know what would have happened if I let it go."
    RAM "I wasn’t in a good mental state earlier, after this smoke break I cooled off. Here hold out your hands"
    " as he swings his bag over and goes through it.” I hold out my hands as he asked and he pulls something out of has backpack and puts it in my hands he holds it tightly he whispers to me"
    RAM "Thanks for listening to me bro. This saved me once before maybe it can save you."
    "and he releases it from his hand and runs off."
    hide sultan_talking_pose

    "Looking down I see a screwdriver in my hand It seems to have an irregular shape it looked like it had two screwdriver heads bolted into it. They were both labeled with white text saying “single” and “double” on it."
    $ inventory.append("Special Screwdriver")
    "I look at samuel and he gives me the thumbs up and we both grin."
    SAM "Lets head back and fix that projector, we wouldn’t want to keep the sargent waiting would we?"
    "We both lined up with each other as we did many time before and I give him the signal to start counting he started counting down from three and than we sprinted back to the projector room."
    "He was in the lead till we reached the staircase, he almost feel and tripped over his own shoelace and I caught his hand and helped him back up saying"
    BEN "Be careful, if we go too fast we can get into trouble."
    "We both walk slowly down the stairs and start the race back up again after we leave the previous room as we reach the projector room we catch our breach I say in between my breaths"
    BEN "I think….I won."
    SAM "Not…a….chance..."
    hide ben_neutral
    hide samuel_normal_pose

    scene bootcampinsideprojectorroomstartm
    show ben_idle at left
    show samuel_normal_pose at right
    "We both agree that this was a tie and we head over to the projector after some time, I look at the projector as a whole seeing both films in there proper places"
    "I read the labels on the big tape reading the label it says AAXA SCP-A01 on the right gear and AAXA SCP-A02 on the left."
    BEN "I ask Samuel about these"
    SAM "I have no idea, maybe that is the manufacturing label or something?"
    "looking down I see the back of the projector there are four nuts. I look at the single screwdrivers in my hand and get to work."
    "I use the screwdriver head labeled single, the first screw comes out fine and than the second and the third until the back finally plops out onto the floor."
    "Looking inside the device I see many gears and knobs some of them labeled. Also a strange compartment requiring two screws to be removed."
    "These screws were attached to each other, I have never seen anything like this before, their oblique angels making it hard to find out what to do."
    "I ask samuel what this is he looks at it confused than asks me for my screwdriver, I hand it over it him and he picks it up."
    "He thinks for a bit than moves the screwdriver head into place so the one labeled “double” is in line with the one labeled “single” and presses it in."
    "As he presses it in there is a moment of silence before it properly clicks the satisfying sound of the click in my ears brightens my mood a bit as he begins to turn it."
    "Two of the screws pop out at once it seems like they were meant for this specific screwdriver."
    "I switch the screwdriver back to the single mode and I unscrew the last screw the final piece coming out revealing what looks to be a singular burnt out light bulb."
    "I begin to unscrew it but I feel a large shock as I pull my hand back I notice a small prick in my hand, I pull what looks like a small piece of red glass out"
    "it seems to be a glass shard as I start to bleed. I than watch as the lightbulb suddenly turns on as if it was not broken at all it shining a bright red color."
    "Me and Samuel look at each other as he is holding the unplugged power cord to the projector confused”."
    "The tapes start spinning and it makes a loud screeching sound enough for everyone in the base to hear."
    "Me and Samuel cover our ears, the sound still blasting through it. I watch as samuel quickly goes over and plugs the projector in and the sound stops."
    "A red light coming from the projector shows on the wall revealing text on a blue background it has a title that reads“ The unstable darkness” reading the text below"
    "“There exists many artifacts in this world lost to time. Some are secured and contained while others remain lost or stolen to time."
    "One of these affects the two states in this world, the is and isn’t. Combining both into one making fiction into reality, making the false into the true.”"
    "I look at the screen staring at it for a few seconds before I hear I click and a screech come from the projector as the projector light turns white and the slide changes to the next slide revealing what was in the slideshow from earlier today"
    "I pick up the screwdriver and pocked it while responding"
    BEN "Hey I was reading that!"
    "Samuel is about to respond when we hear footsteps behind us looking back we see the drill Sargent walk into the room smiling"
    hide ben_idle
    hide samuel_normal_pose
    show drill_sarg_very_happy at center
    DRI "Well you too really did an exceptional job."
    "He walks up to the projector and unplugs it picking it up as he does, "
    DRI "Your just in time too, we are loading up and preparing to start the mission, lets move out you two!."
    BEN "Sir yes sir!"
    SAM "Sir yes sir!"
    "I grunt as I feel a weight put onto my hand as he plops the projector into my now empty hands and we follow behind him"
    jump outsidewithoutuniform

label abandonsamuel:
    scene bg_outside_projector_room
    show ben_neutral at center
    "I look to the left of the door seeing Samuel standing there reading a book, I pay less attention to him as I head towards the first place I think a screwdriver would be the storage room."
    scene bg_storage_room
    show ben_neutral at center
    "As I approach the storage room I notice a keypad next to the door I head towards the door and examine the keypad."
    "It has letters on it instead of numbers it seems I am spoused to enter a passphrase."
    "I quickly look to my left and look to my right and enter a random passphrase I thing in my head “Butts2012” after a few seconds of nothingness a buzz and a light red glow appear."
    "I stand there staring at the keypad watching the light fade back into place I laugh a bit to myself realizing that my journey ended as fast as it started."
    "I am startled as I hear someone walk up to me a soldier must have overheard me laughing."
    "Looking closer they seem familiar, I realize that they were in the meeting from before, it was the person sitting in the front seat."
    show sultan_talking_pose at right
    RAM "(if not met yet He reaches his hand out to me “want a cig bro?” I am caught off guard by this and instantly deny him)"
    RAM "So what are you laughing about bro?"
    "I watch as the smoke comes out of the lit cigar making little clouds go up into the sky and I respond with"
    BEN "I am [still] (if talked before) looking for a specialty screwdriver do you have any idea were one would be?"
    "He takes the cigar out of his mouth and walks up to the locked door, I watch him enter the passcode with ease almost like he has done this many times before"
    "I follow him inside the storage room and he walks of to a storage draw and slides it open revealing what must be a dozen screwdrivers."
    BEN "I thank him and head back to the projector room to grab the projector to fix, once I come back projector in hand I notice he is still standing in there"
    "using the closet as a place to hide his smoking habits from the public. I look at the projector as a whole seeing both films in there proper places I read the labels on the big tape reading the label"
    "it says AAXA SCP-A01 on the right gear and AAXA SCP-A02 on the left looking down I see the back of the projector there are four nuts."
    "I look at the screwdrivers laid out before me and get to work picking up the screwdriver that fits, the first screw comes out fine and than the second and the third"
    "until the back finally plops out onto the floor. Looking inside the device I see many gears and knobs some of them labeled. Also a strange compartment requiring two screws to be removed."
    "These screws were attached to each other, I have never seen anything like this before, their oblique angels making it hard to find out what screwdriver was needed."
    "After going through each screwdriver one by one I was unable to find out what was needed."
    "As I look at the gears trying to find out what was wrong I hear a flick almost like someone is tossing something and than a burst sound."
    "Looking behind me I see a bright light and than feel a intense heat, the cardboard boxes caught fire!"
    RAM "It wasn’t me bro, I don’t know how this could have happened."
    "He then begins to walk out of the room as the fire spreads not bothering to look back."
    hide sultan_talking_pose
    "The fire spreads from box to box as if it was a chorus singing a song, some big boxes some small boxes the room was quickly getting hotter the white smoke turned to black smoke and the fire soon engulfed the room."
    "I rush towards the projector and pick it up. I quickly run out of the room behind the man, I grab onto his shoulder before the adrenaline wears of and my hand slips"
    "I have to place the heavy projector back down. I kneel down and place it down, I am out of breath… I look up at him as he casually lights his next cigar."
    show sultan_talking_pose at right
    "The world spins around me as I hear beeping and screaming, the smoke creeping out of the storage cabinet into the main hall."
    "I hear a slight creak and feel as it starts raining. With the last bit of my energy I stand up in a turtle position and cover the projector with my body"
    "making sure it does not get soaked as I hear the chaos around me, I hear footsteps and screaming and feel the intense heat hit my back as the fire spread, I start to wince from the pain"
    "and decide it is best that I should just close my eyes and open them back up when this is all over, so I do I revert inwards thinking about my life decisions that bought me here."
    BEN "Maybe if I chose Samuel this wouldn’t have happened. Maybe I should have never joined the army. Maybe if I took action earlier she-."
    BEN "I stop myself no, it is my duty to complete this task, this mission. I chose to serve this country no one else did, no one else would. I take a deep breath and prepare to protect this projector with my life."
    "The few minutes felt like a blur to me, I feel as if my instincts have kicked in and I am unable to move, I feel my legs quiver and the water drip down my shirt."
    "I stayed in that position making sure the projector didn’t get wet like my life depended on it, until my legs finally gave in and I fell onto the floor avoiding the projector."
    "I lay there motionless for many more minuets as I catch my breath, I look up at the ceiling the sprinklers turning off and than looking straight ahead at the man that caused all of this."
    "As I regain my energy I sit back up and stand up I slap the cigar out of his hands, I step on it no I stomp on it as hard as I can putting out the bud until it is fully out."
    hide sultan_talking_pose
    "Looking around I notice a crowd of at least 5 people has gathered around us undoubtedly coming here due to the fire."
    "I ignore them though and return to the projector, it seems like the back piece of the projector was still in the room from when I took it off."
    "However aside from some burn marks on the front the projector seems fine, I look inside the room I was just in most of the floor is flooded, there are various tools and trinkets floating in the water and some ash"
    "the back plate of the projector is nowhere in site if I wanted to get it back on id have to search the room for it."
    "There are two people in fire retardant suits in the room assessing the damages they don’t look particularly happy about it and I am sure ill see them again once they see the camera footage of how this happened."
    show sultan_talk_pose at right
    RAM "Well bro, if I were you id get your clothes replaced and get your weapons the mission starts tonight after all."
    "I think to myself if this is really the best course of action, should I really listen to the man who almost broke my projector and caused this whole debacle in the first place"
    "or should I go get my uniform so I am at least ready for the mission to begin or should I just try to fix this mess I am already and focus on fixing the projector."
    menu:
        "Get Army Uniform":
            jump getuniformwithoutsamuel
        "Go get screwdriver": # This was "Go fix projector"
            jump fixprojectoralone
label getuniformwithsamuel_alt:
    scene bg_military_entrance
    show ben_neutral at left
    show samuel_normal_pose at right
    BEN "Safety always comes first I think to myself as I turn around heading towards the supply depo."
    "I hear Samuel quickly follow behind me as he starts trying to make conversation."
    SAM "You know the two guys that run the stands where we are headed right? I spoke to them this morning they were kind of depressed."
    SAM "The sarg has been calling them heady and army, it seems it caught on with some of the recruits. I would try to keep it easy on them."
    "I mentally take a note of what  as we pass by a door that takes my attention it has a paper that has the text COMPUTER LAB drawn onto it."
    "The text is slopply written and in blank sharpie marker ink. The paper is ripped a part of it torn off and on the floor."
    "It also seems like someone or something dented the door. The door is dented enough to see a small crater where the impact was it was about as big as my head."
    "I see that Samuel is getting farther from me and I rush ahead to catch up to him, he seems to notice that I was looking at the door and asks"
    SAM "Do you want to check it out? I think we still have time."
    BEN "No, duty is more important. Maybe if we ever have down time after this we can go check it out together."
    SAM "Your loss."
    "and we both continue. There is a maintenance door that leads into a damp garage area."

    scene bg_elevator
    show ben_neutral at left
    show samuel_normal_pose at right

    "The room is pretty empty aside from two stands setup opposite to an elevator. The room is cold and dark only illuminated by the lights of the elevator and stands."
    "The two people stand there staring into nothingness the sound of a cheerful tune coming from the stand on the left."
    "The stand on the left labeled weapon stand has a bill board on it with the text “Todays menu” and a list of guns ranging from small pistols to large machine guns I can only dream of using."
    "The person manning the stand stands flamboyantly a unmoving smile, his eyes beat red in medieval knight armor, its shine contrasting the painted on pastel background behind him."
    "He seems to be breathing in and out waiting patiently for the next person to arrive at his stand. His most notable feature being his hands."
    "His hands seem to unusually contort at the wrists and his hands are stuck in twisted positions almost like his hands have no bones at all."
    "I feel a slight tap on my shoulder I choose to remain focused on what lay before me looking to the right there is at least some semblance of normalcy as I see a hooded man in all red robes."
    "The stand looks normal enough until I took a closer look first the red hood masking his face, there is something perduring out of his face. It is way too big to be a simple bump there has to be something more."
    "Second what’s behind him, its not a pastel wallpaper but products. He has many products behind him some seemingly unrelated to armor. There are some strange devices I am unable to recognize."
    "Questions pass through my mind like were did he get these from? why did he choose to display them so publicly?"
    "Finally that music, it is slow and methodical yet cheery. It is being played from a old stereo, the tone is almost hypnotic with how slow and droning the loop is."
    "I feel a tap on my shoulder and see Samuel he looks concerned"
    SAM "Are you alright? You have been staring into space for a few minuets , I can order the armor if your scared."
    BEN "No, I am fine. I was just a bit spaced out."
    SAM "You sure, maybe we should go back?"
    "I ignore his question and decide which stand I should approach."
    hide samuel_normal_pose
    show knight default at center
    KNIGHT "..."
    "As I approach the man he seems to grow. His shadow looming over me, he has turned into a giant. His armor shining in the low light of the room,"
    "his smile getting wider, a slight mumble coming from it. I was not sure how a face can even look like this he was no man he was a monster."
    "I feel another tap and finally give in looking behind me samuel put his hands on my shoulder almost as a comforting motion to tell me its going to be okay."
    show samuel_sholder_pose at right
    "I take a deep breath and begin the conversation"
    BEN "I am here to place an order in for a new uniform"
    "its face doesn’t move he stands there eyes unblinking almost like he is judging me, asking me “why did you come here”."
    "I almost take a step back but Samuel walks in front of me and loudly states"
    SAM "my friend is here to pick up a new gun!."
    "As I realized my mistake from earlier I notice Its eyeballs move quickly homing in on Samuel almost like they are locking on to a new target."
    "I prepare for impact before I see the monster come to life its bright smile turns into a frown, his eyes slowly start blinking and his hands,"
    "his broken hands move up to his face and pull something out. It is small by I see and hear it quite clearly, a pair of earphones the volume so loud I can make out it was playing some k-pop music."
    KNIGHT "What was that you said again."
    "The façade has vanished this was no monster, it was a man a broken tired man."
    "Samuel repeats his question and the man replies in a now defeated still raspy, monotone voice with"
    KNIGHT "I will put in a order for you it should be done before your mission starts."
    "He flips a small switch and a tube comes down from the ceiling."
    KNIGHT "So what kind of weapon do you want to use?"
    menu choice_of_weapons_alt: 
        "Pistol":
            $ player_weapon_choice = "Pistol"
            jump process_weapon_choice # This label was already used, ensure okay or make unique
        "Rifle":
            $ player_weapon_choice = "Rifle"
            jump process_weapon_choice
        "Shotgun":
            $ player_weapon_choice = "Shotgun"
            jump process_weapon_choice
        "Grenade Launcher (Dream Big)":
            $ player_weapon_choice = "Grenade Launcher"
            jump process_weapon_choice

label process_weapon_choice_alt: 
    KNIGHT "Good choice, I wouldn’t personally go for that one but oh well."
    "He places the paper back in the tube and flicks a switch. I watch as the paper quickly goes up into the unknown."
    KNIGHT "Anything else?"
    BEN "..."
    "he than grabs his headphones and puts them back in his ears."
    hide knight default
    hide samuel_sholder_pose
    show ben_neutral at left
    show samuel_normal_pose at right

    "Perhaps I was overthinking everything and this would go more smoothly than I have previously thought, as we walk over to the next stand I look over to Samuel and he gives me the thumbs up."
    "We than head over to the next stand [right stand]"
    show red_hood default at center
    RED_HOOD "..."
    "I take a deep breath as I approach the stand, the hooded man seems to notice me his head moves up and  in a low voice"
    RED_HOOD "Hello you two, you must be benjamin right? Today’s reading said you would come."
    BEN "Who told you I would come?"
    RED_HOOD "No matter, I have the order you were about to place ready."
    "He hands me a new uniform the right one."
    $ inventory.append("New Uniform")
    SAM "Alright, lets get you out of that uniform, lets head to the bathroom."
    BEN "I can’t accept this, what just happened is just too convenient. I have an urge a pulse even I need to figure out how this happened no matter the cost."
    BEN "hold up a second"
    "I put my hand up to Samuel as I face the man I say"
    BEN "How the hell did you know what I was going to order!"
    RED_HOOD "You best not seek knowledge that you are unprepared to learn about for the truth is far worse than what you should know."
    SAM "..."
    BEN "Cut the bullshit, who told you?"
    RED_HOOD "..."
    BEN "Tell me! Tell me now!"
    "and sighs he lifts his hood up a tiny amount revealing for only a second a single horn sticking out of his head before he puts the robe back down."
    RED_HOOD "Both of you mustn’t come back here for I have revealed some of my inner self."
    "we both walk backwards my uniform in hand until he are a safe enough distance from him."
    SAM "we will talk about this later."
    hide red_hood default
    hide samuel_normal_pose
    hide ben_neutral

    scene bg_main_desk_area # Placeholder for bathroom
    show ben_neutral at center # Changing
    "Me and Samuel head to the bathroom. I tell Samuel to wait outside as I enter the bathroom and begin to undress."
    "First my shirt comes off than my pants fall down, I grab the new uniform feeling how it was perfectly, I feel as the stiff fabric stretches with my skin as I pull my new pants up"
    "the pants almost being too big for me if it wasn’t for the belt holding them in place, I think about how dirty this uniform will get after the mission how this may be the only one time I see it clean and in prefect condition."
    "I feel the shirt slip on next as I slide it down my muscular body looking in the mirror I see myself and hype myself up for the mission to come."
    "I feel the polyester touch across my body as it rigidly comes into place. Next comes on the shoes they are heavy put reliable I than grab my helmet putting it on my head"
    "seeing the pointy metal come out of the top I think to myself it may be able to be used as a tool."
    "I than take one last look at myself in the mirror and leave the changing room."
    hide ben_neutral

    scene bg_elevator # Back to garage
    show drill_sarg_talk at center
    show samuel_normal_pose at right
    "As I leave I see the drill Sargent talking to Samuel outside he looks disappointed"
    DRI "So you were unable to fix this old thing? Well I hope you find a mechanic during the mission because we are getting ready to leave the base."
    DRI "Follow me outside you two maggots we are already late as is."
    "His frown worsens"
    "He looks to Samuel and chuckles"
    DRI "I know you two like chatting so I am separating you into different squads. This mission is important and I wouldn’t want you to screw this up. You will follow me do you understand"
    BEN "sir yes sir!"
    SAM "sir yes sir!"
    "and begin to follow him outside as the garage door opens up lighting up the room we see a line of soldiers waiting outside all rigid in form waiting for there orders."
    "We both head into our respective squads…"
    jump outsidewithuniform

label getscrewdriverwithsamuel_alt:
    scene bg_military_entrance
    show ben_neutral at left
    show samuel_redbook at right
    BEN "Contemplating my options I figure that I might as well start this pointless search for my screwdriver, I try to forget about the screwdriver."
    "I head to the right as me and Samuel walk to the right he begins to start some small talk"
    SAM "that book from earlier –"
    BEN "Yeah don’t worry about it, I won’t tell anyone you read picture books."
    SAM "Hey! Its not a picture book."
    "He moves the book back into both hands and begins reading"
    SAM "There exists two states in this world, the is and isn’t."
    BEN "I already told you, I won’t tell anyone you don’t need to make this worse than it already is"
    SAM "Once the lost artifacts are bought into one place…"
    "I move my hand and close the book myself as we walk and say"
    BEN "look man, I know that story is probably great and all but we have bigger problems we need to solve. Like getting that screwdriver!"
    SAM "This has to be connected to the mission, those scenes on the projector there similar to what is written in this book."
    "I dismiss his claim and we both continue onwards towards a giant window."

    scene bg_city_freedom
    "We both stop a bit and admire the outside, The window reveals open roads going into other buildings that look smaller from here than they actually are."
    "We can see trucks and military cars driving on the paved cement. We watch as two people in a jeep make hand motions talking to each other there car driving off into other facilities and the unknown."
    "We can see the calm sky seeing the morning sun come up over the horizon the clouds shapes are uniform."
    "We are at peace until the ground starts shaking, looking up the clouds disperse and open a fleet of osprey aircraft come whirling in and head towards the front of the building we are in."
    "We both can see and feel the aircraft fly above us disrupting the peace."
    "I hear someone stand, looking behind me I see the turban man from earlier getting up from his seat."
    hide ben_neutral
    hide samuel_redbook
    show sultan_talking_pose at center
    RAM "You never got my name did you?"
    "Looking at him with his lit cigar in his mouth  staring at me with tired eyes"
    RAM "You can call me the ram."
    "He takes another puff of his cigar."
    show ben_neutral at left
    show samuel_normal_pose at right
    "Me and Samuel stare at him for a few seconds processing that odd sounding name before he looks at my hands and looks back up at me and says"
    RAM "So you really are going to fix that projector bro?"
    "He gives me a side eye before sitting down again"
    RAM "I dealt with something similar on a previous mission."
    "Me and Samuel decide to sit down and listen to his story, he continues"
    RAM "I was in charge of protecting a audio device, it would play a simple lullaby it was meant to calm someone known as the giant . My squad was a team of four, but we lost one during the mission."
    RAM "The mission started off poorly. We were all ill equipped. Me and red hood were in charge of recon while the knight and private p were supposed to play that damn device."
    SAM "what happened to the other two people"
    RAM "That is their story to tell not mine."
    RAM "The damn thing ran out of battery” His face scrunches up and his anger builds “The main fucking device meant to save us ran on double a batteries"
    "he coughs cigar smoke coming out of his mouth he seems to be less tense than before as "
    RAM "This place is a joke. I wouldn’t trust that projector for a second."
    BEN "We were given orders to fix this projector and we will fulfill them"
    RAM "..."
    "I watch as the smoke cloud rises from his cigar it slowly rising up and disappearing into the air. He shakes his head"
    RAM "This is why I stayed in the military, to prevent people like you from dying"
    "he sighs looking defeated"
    RAM "This stress has been getting to me recently that this mission may be another failure, that we may not come back alive again."
    SAM "We won’t let that happen."
    RAM "I almost started a small fire in the storage room."
    "Me and samuel look at each other we both have been their earlier today and didn’t see him there he continues"
    RAM "I was smoking a cigar and I tossed it on the floor carelessly I was going to let it stay their but once I heard you two trying the combination to the storage room; I stomped it out and picked it back up quickly. Luckly, you got the code wrong at first."
    "I look at Samuel he is slightly embarrassed, ram notices this but does not say anything"
    RAM "I was able to sneak out of the room but I felt really guilty after about what I have done. I don’t know what would have happened if I let it go."
    RAM "I wasn’t in a good mental state earlier, after this smoke break I cooled off. Here hold out your hands"
    " as he swings his bag over and goes through it.” I hold out my hands as he asked and he pulls something out of has backpack and puts it in my hands he holds it tightly he whispers to me"
    RAM "Thanks for listening to me bro. This saved me once before maybe it can save you."
    "and he releases it from his hand and runs off."
    hide sultan_talking_pose

    "Looking down I see a screwdriver in my hand It seems to have an irregular shape it looked like it had two screwdriver heads bolted into it. They were both labeled with white text saying “single” and “double” on it."
    $ inventory.append("Special Screwdriver")
    "I look at samuel and he gives me the thumbs up and we both grin."
    SAM "Lets head back and fix that projector, we wouldn’t want to keep the sargent waiting would we?"
    "We both lined up with each other as we did many time before and I give him the signal to start counting he started counting down from three and than we sprinted back to the projector room."
    "He was in the lead till we reached the staircase, he almost feel and tripped over his own shoelace and I caught his hand and helped him back up saying"
    BEN "Be careful, if we go too fast we can get into trouble."
    "We both walk slowly down the stairs and start the race back up again after we leave the previous room as we reach the projector room we catch our breach I say in between my breaths"
    BEN "I think….I won."
    SAM "Not…a….chance..."
    hide ben_neutral
    hide samuel_normal_pose

    scene bootcampinsideprojectorroomstartm
    show ben_idle at left
    show samuel_normal_pose at right
    "We both agree that this was a tie and we head over to the projector after some time, I look at the projector as a whole seeing both films in there proper places"
    "I read the labels on the big tape reading the label it says AAXA SCP-A01 on the right gear and AAXA SCP-A02 on the left."
    BEN "I ask Samuel about these"
    SAM "I have no idea, maybe that is the manufacturing label or something?"
    "looking down I see the back of the projector there are four nuts. I look at the single screwdrivers in my hand and get to work."
    "I use the screwdriver head labeled single, the first screw comes out fine and than the second and the third until the back finally plops out onto the floor."
    "Looking inside the device I see many gears and knobs some of them labeled. Also a strange compartment requiring two screws to be removed."
    "These screws were attached to each other, I have never seen anything like this before, their oblique angels making it hard to find out what to do."
    "I ask samuel what this is he looks at it confused than asks me for my screwdriver, I hand it over it him and he picks it up."
    "He thinks for a bit than moves the screwdriver head into place so the one labeled “double” is in line with the one labeled “single” and presses it in."
    "As he presses it in there is a moment of silence before it properly clicks the satisfying sound of the click in my ears brightens my mood a bit as he begins to turn it."
    "Two of the screws pop out at once it seems like they were meant for this specific screwdriver."
    "I switch the screwdriver back to the single mode and I unscrew the last screw the final piece coming out revealing what looks to be a singular burnt out light bulb."
    "I begin to unscrew it but I feel a large shock as I pull my hand back I notice a small prick in my hand, I pull what looks like a small piece of red glass out"
    "it seems to be a glass shard as I start to bleed. I than watch as the lightbulb suddenly turns on as if it was not broken at all it shining a bright red color."
    "Me and Samuel look at each other as he is holding the unplugged power cord to the projector confused”."
    "The tapes start spinning and it makes a loud screeching sound enough for everyone in the base to hear."
    "Me and Samuel cover our ears, the sound still blasting through it. I watch as samuel quickly goes over and plugs the projector in and the sound stops."
    "A red light coming from the projector shows on the wall revealing text on a blue background it has a title that reads“ The unstable darkness” reading the text below"
    "“There exists many artifacts in this world lost to time. Some are secured and contained while others remain lost or stolen to time."
    "One of these affects the two states in this world, the is and isn’t. Combining both into one making fiction into reality, making the false into the true.”"
    "I look at the screen staring at it for a few seconds before I hear I click and a screech come from the projector as the projector light turns white and the slide changes to the next slide revealing what was in the slideshow from earlier today"
    "I pick up the screwdriver and pocked it while responding"
    BEN "Hey I was reading that!"
    "Samuel is about to respond when we hear footsteps behind us looking back we see the drill Sargent walk into the room smiling"
    hide ben_idle
    hide samuel_normal_pose
    show drill_sarg_very_happy at center
    DRI "Well you too really did an exceptional job."
    "He walks up to the projector and unplugs it picking it up as he does, "
    DRI "Your just in time too, we are loading up and preparing to start the mission, lets move out you two!."
    BEN "Sir yes sir!"
    SAM "Sir yes sir!"
    "I grunt as I feel a weight put onto my hand as he plops the projector into my now empty hands and we follow behind him"
    jump outsidewithoutuniform

label abandonsamuel_alt:
    scene bg_outside_projector_room
    show ben_neutral at center
    "I look to the left of the door seeing Samuel standing there reading a book, I pay less attention to him as I head towards the first place I think a screwdriver would be the storage room."
    scene bg_storage_room
    show ben_neutral at center
    "As I approach the storage room I notice a keypad next to the door I head towards the door and examine the keypad."
    "It has letters on it instead of numbers it seems I am spoused to enter a passphrase."
    "I quickly look to my left and look to my right and enter a random passphrase I thing in my head “Butts2012” after a few seconds of nothingness a buzz and a light red glow appear."
    "I stand there staring at the keypad watching the light fade back into place I laugh a bit to myself realizing that my journey ended as fast as it started."
    "I am startled as I hear someone walk up to me a soldier must have overheard me laughing."
    "Looking closer they seem familiar, I realize that they were in the meeting from before, it was the person sitting in the front seat."
    show sultan_talking_pose at right
    RAM "(if not met yet He reaches his hand out to me “want a cig bro?” I am caught off guard by this and instantly deny him)"
    RAM "So what are you laughing about bro?"
    "I watch as the smoke comes out of the lit cigar making little clouds go up into the sky and I respond with"
    BEN "I am [still] (if talked before) looking for a specialty screwdriver do you have any idea were one would be?"
    "He takes the cigar out of his mouth and walks up to the locked door, I watch him enter the passcode with ease almost like he has done this many times before"
    "I follow him inside the storage room and he walks of to a storage draw and slides it open revealing what must be a dozen screwdrivers."
    BEN "I thank him and head back to the projector room to grab the projector to fix, once I come back projector in hand I notice he is still standing in there"
    "using the closet as a place to hide his smoking habits from the public. I look at the projector as a whole seeing both films in there proper places I read the labels on the big tape reading the label"
    "it says AAXA SCP-A01 on the right gear and AAXA SCP-A02 on the left looking down I see the back of the projector there are four nuts."
    "I look at the screwdrivers laid out before me and get to work picking up the screwdriver that fits, the first screw comes out fine and than the second and the third"
    "until the back finally plops out onto the floor. Looking inside the device I see many gears and knobs some of them labeled. Also a strange compartment requiring two screws to be removed."
    "These screws were attached to each other, I have never seen anything like this before, their oblique angels making it hard to find out what screwdriver was needed."
    "After going through each screwdriver one by one I was unable to find out what was needed."
    "As I look at the gears trying to find out what was wrong I hear a flick almost like someone is tossing something and than a burst sound."
    "Looking behind me I see a bright light and than feel a intense heat, the cardboard boxes caught fire!"
    RAM "It wasn’t me bro, I don’t know how this could have happened."
    "He then begins to walk out of the room as the fire spreads not bothering to look back."
    hide sultan_talking_pose
    "The fire spreads from box to box as if it was a chorus singing a song, some big boxes some small boxes the room was quickly getting hotter the white smoke turned to black smoke and the fire soon engulfed the room."
    "I rush towards the projector and pick it up. I quickly run out of the room behind the man, I grab onto his shoulder before the adrenaline wears of and my hand slips"
    "I have to place the heavy projector back down. I kneel down and place it down, I am out of breath… I look up at him as he casually lights his next cigar."
    show sultan_talking_pose at right
    "The world spins around me as I hear beeping and screaming, the smoke creeping out of the storage cabinet into the main hall."
    "I hear a slight creak and feel as it starts raining. With the last bit of my energy I stand up in a turtle position and cover the projector with my body"
    "making sure it does not get soaked as I hear the chaos around me, I hear footsteps and screaming and feel the intense heat hit my back as the fire spread, I start to wince from the pain"
    "and decide it is best that I should just close my eyes and open them back up when this is all over, so I do I revert inwards thinking about my life decisions that bought me here."
    BEN "Maybe if I chose Samuel this wouldn’t have happened. Maybe I should have never joined the army. Maybe if I took action earlier she-."
    BEN "I stop myself no, it is my duty to complete this task, this mission. I chose to serve this country no one else did, no one else would. I take a deep breath and prepare to protect this projector with my life."
    "The few minutes felt like a blur to me, I feel as if my instincts have kicked in and I am unable to move, I feel my legs quiver and the water drip down my shirt."
    "I stayed in that position making sure the projector didn’t get wet like my life depended on it, until my legs finally gave in and I fell onto the floor avoiding the projector."
    "I lay there motionless for many more minuets as I catch my breath, I look up at the ceiling the sprinklers turning off and than looking straight ahead at the man that caused all of this."
    "As I regain my energy I sit back up and stand up I slap the cigar out of his hands, I step on it no I stomp on it as hard as I can putting out the bud until it is fully out."
    hide sultan_talking_pose
    "Looking around I notice a crowd of at least 5 people has gathered around us undoubtedly coming here due to the fire."
    "I ignore them though and return to the projector, it seems like the back piece of the projector was still in the room from when I took it off."
    "However aside from some burn marks on the front the projector seems fine, I look inside the room I was just in most of the floor is flooded, there are various tools and trinkets floating in the water and some ash"
    "the back plate of the projector is nowhere in site if I wanted to get it back on id have to search the room for it."
    "There are two people in fire retardant suits in the room assessing the damages they don’t look particularly happy about it and I am sure ill see them again once they see the camera footage of how this happened."
    show sultan_talk_pose at right
    RAM "Well bro, if I were you id get your clothes replaced and get your weapons the mission starts tonight after all."
    "I think to myself if this is really the best course of action, should I really listen to the man who almost broke my projector and caused this whole debacle in the first place"
    "or should I go get my uniform so I am at least ready for the mission to begin or should I just try to fix this mess I am already and focus on fixing the projector."
    menu:
        "Get Army Uniform":
            jump getuniformwithoutsamuel
        "Go fix projector": 
            jump fixprojectoralone_alt

label fixprojectoralone_alt:
    scene bg_storage_room 
    show ben_neutral at center # Soaked, possibly holding projector
    BEN "I decide to stick with my main mission."
    BEN "Even though my clothes are soaked I need to fix this projector."
    "I take a deep breath and start focusing. I start by doing a damage assessment on the projector."
    "The front lens seems to be damaged while the back piece is missing, most likely destroyed from the fire."
    "The internal parts seem damp, there is possible water damage done to this."
    "The normal screws I took out from earlier are also missing."
    "I need to go back into the storage room to search for the missing parts."
    "I mentally take note of all that is missing and prepare to return to the storage room."
    "I get up from my kneeling stature and I am met with a man in a firefighters uniform staring at me sternly."
    show q3_firefighter_stern at right # Assuming Q3 is firefighter character, need pose
    Q3 "So you’re the sergeants lap dog huh? I heard a lot about you."
    "I stare back at him thinking of what I should say next."
    Q3 "You caused a lot of trouble here you know that?" # Laughing, mocking
    BEN "What are you talking about?"
    Q3 "You were in that room when the fire started right? You could have stopped it but you chose to protect that thing."
    "He points to the projector."
    BEN "This is an important piece of military equipment, it is vital to the mission." # Annoyed
    Q3 "You crayon eaters are always too focused on your damn mission! People could have died in this fire, do you understand that?" # Annoyed
    "I simply stare back at him confused on what he is talking about he scoffs at me and mumbles something while walking off."
    hide q3_firefighter_stern

    "I decide to begin my assessment if it is safe enough to enter back into the room to try to recover the missing screws and backplate."
    "I walk past some people and look into the room. The room has another firefighter in it he looks tired he is holding a bucket."
    "There is some puddles and a lot of burn marks and sut on the floor it looks safe enough to enter."
    "I walk into the entrance of the room my already wet shoes making a squishing sound causing the firefighters to notice me."
    show q3_firefighter_tired at right # Tired firefighter pose
    Q3 "Listen I know you went through a lot this morning but you can’t walk around like that."
    Q3 "I am getting off shift soon so follow me."
    "He puts the bucket he is holding on the floor and walks out of the room guiding me to follow him."
    hide q3_firefighter_tired
    "I obliged picking up the projector and following him past the storage room door into what seems to be a maintenance hallway"
    "my shoes making the same squishing sound as we both walked in silence."
    "Going through a door I see many rectangular storage devices and a stairway to upstairs I see it is blocked by a green container."
    "The firefighter taps on one of the storage devices and it effortlessly opens revealing civilian clothing."
    show q3_firefighter_default at right # Default firefighter pose
    Q3 "Take them." # Implied from "tosses them... telling me to take them"
    "He takes off his firefighter shoes and tosses them to me."
    "I put down the projector and I take off my wet shoes and slip into his shoes, them feeling warm and used."
    "It felt kind of gross wearing someone else’s clothes but It did feel better than what I was wearing before."
    "As the man picks up the full rectangular storage container I tell him"
    BEN "thank you"
    Q3 "Try not to get these dirty too okay?"
    "as he walks upstairs with his civilian clothes."
    hide q3_firefighter_default

    "I pick up my projector and head back to the storage room."
    scene bg_storage_room # Back in the burnt storage room
    show ben_neutral at left
    "As I arrive I can see the crowd has thinned only a few people remain the smoking man he is standing in front of the burnt down room smoking a new cigar."
    show sultan_talking_pose at right # Assuming SUL is the smoking man
    "I walk past him and confront him yet again"
    BEN "Do you have any remorse?"
    "He takes out the cigar from his mouth and waits a bit before blowing another puff until he finally says"
    SUL "Yeah a bit, my mistake man.."
    "I walk past him and enter the room telling him that he has problems."
    hide sultan_talking_pose
    "As I enter the room I head to wear I originally had put the projector finding the spot were it was before strangely dry."
    "I look my around the room and find 3 of the 4 screws I unscrewed picking them up and putting them in my pocket."
    "I begin to pick up some of the burnt boxes the bottom of them spilling out there contents making the floor an even bigger mess."
    "Realizing that this was a mistake I put the burnt boxes back down and I picked up the mess they made."
    "I check near the trash can were the fire started and find a burnt out cigar soaked in water and something next to it."
    "I am confused why this screwdriver would be here though but I don’t question it."
    "After some more time and box moving I eventually find the back plate it took a lot of damage from the initial fire and it seems like it is unrecoverable."
    "I leave the backplate on the floor, I am careless as I put it down and I hear it fall and hit the floor."
    "I notice a hidden trap door on the floor where it fell, it seems the fire damage burnt off its hinge and opened up this trap door revealing a ladder going deeper into the facility."
    "I decide to investigate this trap door as it could have more clues. I leave the projector upstairs and begin my decent into the underground."

    scene black # Or a dark basement scene
    "As I travel down the ladder I notice how the light slowly dims until it is pitch black."
    "I think to myself as I descend down into the darkness that this was probably a bad idea."
    "And that I can climb back up before it gets too dark but my exploratory instincts kick in and I continue to descend."
    "I eventually reach the bottom of the ladder the room pitch black and I can only navigate the room by my other senses."
    "I begin to feel around the walls of this room and I start moving to the right of the ladder I hit another wall more concrete."
    "Moving to the right again I feel more concrete and glass I am careful around the glass as I feel around the section I feel is jagged and sharp almost like the glass is broken."
    "There is some sort of dry liquid on the glass it is rough and crumbly. If I had a light I would be able to tell what it is."
    "Moving more across the wall I reach the left side of the room feeling around there is a door on it is a stappled piece of paper."
    "I rip the paper off of the door and put it in my pocket I also feel something hit my foot, it hurts a bit from walking into it but I bend down and put it in my pocket."
    "I continue following the wall until I reach the ladder again. I decide it is time to climb back up."

    scene bg_storage_room # Back to storage room, light returns
    show ben_neutral at center
    "Climbing back up I reflect on what I just did thinking it was probably not the best idea to go into a pitch dark room without telling anyone."
    "But nevertheless the light gets brighter and brighter until I can see again. I examine what I put in my pocket first the tool."
    "The tool looks like a screwdriver. I pick up the screwdriver from my pocket and examine it closer."
    "Looking at it the screwdriver looks weird. It appears to be a duel headed screwdriver,"
    "this screwdriver having an irregular shape it looked like it had two screwdriver heads bolted into it. They were both labeled with white text saying “single” and “double” on it."
    "I decided to put it in my backpack perhaps this was the screwdriver I was looking for."
    $ inventory.append("Special Screwdriver") # Assuming this is the same screwdriver
    "I check the paper I take out the crumpled paper from my pocket and read it over I find it is a timetable log."
    "It seems like they were doing some experimentation in the laboratory and it seems the experiments were failures."
    "There were many things labeled from testing medical injections to testing new equipment I have never even heard of."
    "All of the equipment listed had a monkeys paw effect to it. One piece of equipment I noticed in particular looked like futuristic power suits"
    "that were able to withstand 2 metric tons of weight being pressed against it but when the user tried to take it off after sustaining damage there skin would peel off with the suit."
    "The more damage the more skin peels off. Another thing of note from the papers were that those three letters appeared again but there was different numbers after them SCP."
    "I think to myself there must be a connection somewhere to these three letters, perhaps it has something to do with these experiments."
    "I pocket the paper thinking that it may be important for later."
    "I decide to head back to the main room to try to repair the projector."
    hide ben_neutral

    scene bootcampinsideprojectorroomstartm # Or current projector room scene
    show ben_neutral at left # Ben brings projector
    "I pick up the projector and head into the projector room I see that the room is vacant aside from a person with a bag on there head sitting there."
    show bagman_default at right
    "He stares at me and than stares at the projector. The bagman walks up to me and says"
    BAG "I-I will help you… I don’t want another incident happening."
    "I lay the projector down and the bagman comes over to me I ask before we start"
    BEN "How can I trust you to not break this thing?"
    BAG "I-I was a lead researcher…" # Hesitates
    BEN "You were? What happened."
    BAG "Before my dismissal I –" # Stops himself
    BAG "Lets just fix this, here I will help you."
    "I look at the projector as a whole seeing both films in there proper places I read the labels on the big tape reading the label it says AAXA SCP-A01 on the right gear and AAXA SCP-A02 on the left."
    "I ask the bag headed man about these and he perks up responds with"
    BAG "They are those tapes object class and designation. AAXA means it is class c and A01 stands for the first month and day."
    BAG "You don’t have to worry about them just know the higher the class the more dangerous the object is."
    "His speech is noticeably less shuddery and more clear it seems he is very interested in this topic."
    "Looking down I see the back of the projector the plate is on the table were I placed it there are three nuts on the floor."
    "The bagman walks over to me and guides my hand to a component of the projector another panel that is screwed in I look at the single screwdrivers in my hand and get to work."
    "I use the screwdriver head labeled single, the first screw comes out fine and than the second and the third until the part finally plops out onto the floor."
    "He continues while he helps me work"
    BAG "Each department has their own official designation of these objects many of them produce anomalous properties."
    BAG "The foundation is trying to standardize these classifications but the dod likes there own way of doing things."
    "Looking inside the device I see many gears and knobs some of them labeled. Also a strange compartment requiring two screws to be removed."
    "These screws were attached to each other, I have never seen anything like this before, their oblique angels making it hard to find out what to do."
    "I ask bagman what this is he looks at it than asks me for my screwdriver, I hand it over it him and he picks it up."
    "He than moves the screwdriver head into place so the one labeled “double” is in line with the one labeled “single” and presses it in."
    "As he presses it he continues"
    BAG "These are only given scientists and important people, they are used to keep normal people from accessing this projector."
    BAG "I don’t even think the sarg knows these are required. They are designed specifically of this SCP."
    "before it properly clicks the satisfying sound of the click in my ears brightens my mood a bit as he begins to turn it."
    "Two of the screws pop out at once it seems like they were meant for this specific screwdriver. He switches the screwdriver back to the single mode"
    "and he begins to unscrew the last screw the final piece coming out revealing what looks to be a singular burnt out light bulb."
    BAG "This bulb is dangerous watch this"
    "he began to unscrew it but a shock sound is heard and he pulled his hand back I notice a small prick in his hand were he held it,"
    "he pulled out what looks like a small piece of red glass out of his hand he starts to bleed and puts his hand in his mouth."
    "I than watch as the lightbulb suddenly turns on as if it was not broken at all it shining a bright red color."
    "Me and bagman look at each other before he tells me to cover my ears. The tapes start spinning and it makes a loud screeching sound enough for everyone in the base to hear."
    "The sound still blasting through it. I watch as bagman says something and quickly goes over and plugs the projector in and the sound stops the screwdriver falling on the floor."
    "A red light coming from the projector shows on the wall revealing text on a blue background it has a title that reads “The unstable darkness” reading the text below"
    "“There exists many artifacts in this world lost to time. Some are secured and contained while others remain lost or stolen to time."
    "One of these affects the two states in this world, the is and isn’t. Combining both into one making fiction into reality, making the false into the true.”"
    "I look at the screen staring at it for a few seconds before I hear I click and a screech come from the projector as the projector light turns white and the slide changes to the next slide revealing what was in the slideshow from earlier today"
    "I pick up the screwdriver and pocked it while responding"
    BEN "Hey I was reading that!"
    "Bagman is about to respond when we hear footsteps behind us looking back we see the drill Sargent walk into the room smiling"
    hide ben_neutral
    hide bagman_default
    show drill_sarg_very_happy at center
    DRI "Well you two really did an exceptional job."
    "He walks up to the projector and unplugs it picking it up as he does, "
    DRI "Your just in time too, we are loading up and preparing to start the mission, lets move out you two!."
    BEN "Sir yes sir!"
    "while he returns to becoming a stuttering mess bagman’s face beat red." # This refers to Bagman
    "I grunt as I feel a weight put onto my hand as he plops the projector into my now empty hands he tells bagman to go on ahead that he wants to talk to me in private,"
    "bagman quickly runs out of the room and after a few seconds the sargent tells me"
    DRI "If I were you, I would stay away from him. He may be smart but he is dangerous he caused a lot of issues for my department in the past."
    "I think to myself what this could mean while following him out into the outside…"
    jump getuniformwithsamuel_alt # Adjusted to point to the renamed duplicate

label getuniformwithoutsamuel:
    scene bg_storage_room # Or appropriate scene after fire/decision
    show ben_neutral at center # Ben is likely soaked
    BEN "I need to get a new uniform and my weapon." # This was part of the thought process before menu
    "I pick up the soaked projector carefully trying not to cut myself on the broken part and glance overat the man who caused this (if he's still around)." # Sultan may or may not be present
    "My goal was not to fix this projector it was get a new uniform. I think back to passing by samuel if I could have gotten him to carry this projector for me."
    "I decide the best course of action is to ask the main desk."

    scene bg_main_desk_area
    show ben_neutral at center # Carrying projector
    "As I walk to the main desk I find two cardboard cutouts of people placed lazily manning the stand. Walking up to the desk I step in a puddle of water getting my already soaked shoes more wet,"
    "slightly annoyed I put the projector on the table with a plunk and static starts coming from the cutouts."
    BEN "Hello? Is anyone there."
    "More static plays from the cutouts, already annoyed I call out"
    BEN "HELLO!?"
    "and receive no response looking closer at the cutouts I realize there are wires attached to them leading into a backroom."
    "I decide to follow them I go around the desk and open the backroom door to find a empty lounge room."
    "The state of it is not the best there is a single couch a mini fridge and a old tv playing static. The walls were peeling off and there was a ton of empty soda cans on the floor."
    "Looking around the room further I notice the wire leads up to a single microphone laid out on the couch covered by books and empty plastic snack bags."
    "I pick up the microphone and speak into it hearing my voice from the other room I realize that this microphone is connected to a speak, it seems they set up this system so they can man the front desk while lounging around."
    "I look a book that I picked up it was labeled “One hundred and one ways to survive a class k scenario”."
    "I humored the book opening it up but was surprised to see a single page stappled into the book locking the other pages out."
    "The page looks like it was written by someone rather than typed out the plain list had detailed instructions on how to use a device called the music nox it described a device that would be able to calm any anomaly into submission."
    "In the book there was big red text written in marker seemingly after the fact saying “MAKE SURE TO BRING SPARE BATTERYS” with the bottom text crossed out."
    "This having no relevant information to the current mission I close the book and place it back where it was before back onto the pile."
    "I head back out of the room that bringing me no closer to getting my uniform I pick back up the projector it feeling more heavy than before,"
    "as I pick it up I think I hear a small clicking sound but upon putting it back down and examining it to see if it is broken it seems that it was just my imagination."
    "I decide to head to the right to the elevator, the elevator has only a single button and it glows a faint yellow hue."

    scene bg_elevator
    show ben_neutral at left # Carrying projector
    show ema default at right # Girl at elevator
    "As I arrive I notice a girl waiting at the elevator she looks skinny in figure and is wearing a standard female military uniform she had a pistol on at her side."
    "Her hair was long and dirty covering most of her face making her eyes hidden. As I wondered who exactally she was."
    "The elevator opens and she walks inside I quickly follow behind her almost missing the door closing."
    "The elevator is cramped and sweaty the old thing makes a screeching sound as it closed, the only light from the elevator being a single led bar in the ceiling,"
    "there were two buttons labeled with images, one of a up arrow and the other a down arrow. She pressed the up arrow already and with a small hitch the elevator starts moving up."
    "We stand there in silence for a few seconds before she breaks the silence her voice is smooth and melodic."
    EMA "You look like you were hit by truck"
    BEN "Yeah, I get that a lot."
    EMA "Your pretty funny you know that. Here you can take this."
    "She handed me a small candy. It was wrapped in red wrapping paper and it was circular shaped."
    $ inventory.append("Red Candy")
    "The elevator dinged open revealing a parking garage."
    hide ema default
    "The garage was mainly empty aside from two stands to the left there was someone dressed as a knight and to the right someone was dressed in a red hood."
    "Both of these people made me uneasy, as I go to examine them further I hear the same voice from before behind me"
    show ema default at right
    EMA "I wouldn’t worry too much about these two, they have been through a lot."
    "She walks towards the man in armor. I follow closely behind her, she talks to the man in armor."
    hide ema default
    show knight default at center
    "His armor shines in the light almost too bright its shine contrasting the painted on pastel background behind him."
    "He is active in conversation engaging with the girl from before he hands her a pack of cigars and pistol ammunition."
    "Refocusing back on him his most notable feature being his hands. His hands seem to unusually contort at the wrists and his hands are stuck in twisted positions"
    "almost like his hands have no bones at all. He uses one hand to push the other hand back into place and they snap together like lego pieces."
    "The girl takes the stuff on the table and he waves goodbye to her."
    BEN "I would like to order a weapon for today’s deployment"
    KNIGHT "What was that you said again."
    BEN "I repeat his question"
    KNIGHT "I will put in a order for you it should be done before your mission starts."
    "He flips a small switch and a tube comes down from the ceiling. He takes out a small paper and asks"
    KNIGHT "So what kind of weapon do you want to use?"
    menu choice_of_weapons_alone2: # Adjusted menu name for uniqueness
        "Pistol  ":
            $ player_weapon_choice = "Pistol"
            jump process_weapon_choice_alone2 # Jump to unique label
        "Rifle  ":
            $ player_weapon_choice = "Rifle"
            jump process_weapon_choice_alone2
        "Shotgun  ":
            $ player_weapon_choice = "Shotgun"
            jump process_weapon_choice_alone2

label process_weapon_choice_alone2: # Unique label
    KNIGHT "Good choice, I wouldn’t personally go for that one but oh well."
    "He places the paper back in the tube and flicks a switch. I watch as the paper quickly goes up into the unknown."
    KNIGHT "Anything else?"
    BEN "..."
    "he than grabs something from his pocked, he puts it in his ear upon further inspection I realize it is headphones. He seems to go back into his own world as his eyes glaze over and the music starts playing in his hear."
    hide knight default
    "I look to the right and see that the lady also has moved onto that stand, something seems wrong with the man at the stand."
    show red_hood default at center
    show ema default at left
    "He is in a red hood but there is something perduring out of his face. I begin to panic in thought a bit but I remember what the girl from earlier told me, she did not want me to think too much about it so I will take her advice."
    "I take a deep breath and I wait in line behind her."
    "I see the hooded man turn around revealing the back of his garments his hood hides his face from full view he grabs an object from a shelf in his stand and asks the girl"
    RED_HOOD "Would you like today’s fortune?"
    EMA "..."
    RED_HOOD "Todays fortune foretells some come complications, you best stay in that computer room of yours.."
    "She seemingly ignores him and walks off"
    hide ema default
    BEN "I would like to put in a order for a new uniform."
    RED_HOOD "I know, that lady already told me."
    BEN "How did she know!"
    RED_HOOD "That is not for me to say, maybe she just had a hunch"
    "he tells me as he walks into the back of his stand. I stand there alone in silence he eventually comes back with a folded up freshly ironed uniform."
    $ inventory.append("New Uniform")
    "He places the uniform ontop of the projector I am holding adding more weight to the already heavy load I am carrying."
    "I head with both the projector and uniform in hand to the bathroom."
    hide red_hood default
    hide ben_neutral

    scene bg_main_desk_area # Placeholder for bathroom
    show ben_neutral at center # Changing
    "I enter an empty stall and put the projector on the floor. The giant machine standing there First my shirt comes off than my pants fall down, I grab the new uniform feeling how it was perfectly"
    "the one from this morning falling on top of the projector. I feel as the stiff fabric stretches with my skin as I pull my new pants up the pants almost being too big for me if it wasn’t for the belt holding them in place."
    "I feel the shirt slip on next as I slide it down my muscular body looking in the mirror I see myself and the broken projector below. I reflect on my life choices as I stare at my reflection everything that lead me up to this moment."
    "I feel the polyester touch across my body as it rigidly comes into place. Next comes on the shoes they are heavy put reliable I than grab my helmet putting it on my head"
    "seeing the pointy metal come out of the top I think to myself it may be able to be used as a tool."
    "I than take one last look at myself in the mirror and leave the changing room."
    hide ben_neutral

    scene bg_elevator # Back to garage
    show ben_neutral at center # In new uniform, carrying projector
    "As I leave the bathroom I see the room still empty no one to by seen, I quickly pick up my old uniform and place it on top of the projector, I begin walking towards the staging area of the mission."
    "As I walk out of the room I see the man in the red hood call out to me in a still hushed voice although he was shouting."
    show red_hood default at right
    "I walk over to him and he offers to hold onto my previous uniform for me."
    "I think about this and figure It would be best to accept his offer he walks out from behind his stand and takes the folded garment himself without saying a word and walks into the backroom."
    hide red_hood default
    "I stand there for a few seconds before regaining my composure, I thank continue on by myself towards the exit door."
    "Upon arriving outside I see soldiers lined up and I see Samuel talking to the drill Sargent I walk up to him"
    jump outsidewithuniform

label outsidewithuniform:
    scene bg_landing_zone_generic
    show ben_neutral at left # In uniform
    show drill_sarg_talk at center
    show samuel_normal_pose at right
    DRI "Everyone is already gathered outside and people are gathering for a very important meeting you will follow me and points will be dedcuted since you are late."
    BEN "SIR YES SIR"
    SAM "SIR YES SIR"
    "and we follow him outside to the landing zone. There are 5 ospery ships outside and soldiers lined up in rows."
    "I quickly head towards my platoon and stand in position. As i stand at the landing zone as a osprey lands, I look to the left to see samuel smiling and starting at the ospery,"
    "looking right I see the sargent standing firm looking determined. The drill sargent speaks pointing to me"
    DRI "Dirtbag, you may have proven yourself in fixing that projector but this will be the real test."
    "The wind from the ospery causes me to put my hands up to cover my eyes from the sheer force of it."
    DRI "This mission may be the last one you go on."
    DRI "I will be staying here, it is your problem now"
    "walking off."
    hide drill_sarg_talk
    hide samuel_normal_pose
    "As he leaves I look back to the center the osprey a sargent walks downs the retractable stairs sizing up everyone."
    show lt_stern at center
    LT "We have a serious sitution on our hands."
    LT "The LZ will be hot by the time of arrival 30 mikes. Once you reach the landing zone you will secure it and evacuate any non combatince as you match your to point alpha."
    LT "Point alpha is a residential complex were your main target designated as the nest. Is there any questions?"
    LT "Good, *points to benjerman* make sure you bring that projector, it is essechial it gets dilvered to the nest"
    BEN "Yes sir!"
    "The drill sargent directs us all onto multiple opserys me and samuel are split up for the first time in awhile."
    "I almost start to worry about but than I calm I don't really care how he holds up on his own I sit down on my seat it feels nice and coushiny."
    hide ben_neutral
    hide lt_stern
    scene bg_osprey_interior_generic
    show ben_sitting at left
    "The first time I have sat down since the inital meeting. The lutenent jumps onto the ship i feel it shake a bit. I feel a tap on my sholder and look to my right."
    show bagman_default at center
    "I get startled as I see someone with a bag on there head sitting next to me."
    BAG "y-you forgot your weapon a-and your uniform"
    BEN "Huh?"
    "he turns around hiding his already hidden face with his hands."
    BAG "..."
    BEN "Why the hell are you wearing a bag of your head and not a helmet. Take that off,"
    "I reach for his bag and he slaps my hand saying"
    BAG "Don't touch that."
    "I figure it is best to not continue my advances to unmask him."
    LT "Is there a problem soldier."
    BEN "Yes sir! This projector is still broken sir!"
    LT "Well shit! You better hope their is a mechanic at the LZ."
    BEN "What if there isn’t?"
    LT "Well that is just too bad you will have to repair it yourself in a live fire zone, good luck maggot."
    "I feel heat in my lap looking down I see the projector is oddly warm. As I look down at the projector on my lap I notice a small part of it moving as the lutenent speaks up"
    LT "We have a very important mission on our hands, multiple undislosed beams of energy have began etruding from the earth. These beams seems to be eminating enrgy capable of blocking out radio and microwaves"
    LT "and have been classfied as a cognitohazard. You will be provided protective glasses and gear cabable of blocking out most of the harmful effects.”"
    "As he talks I put my hand trying to stop the small part from moving, I pull back instinctively as I feel a cut on my finger, it seems the part that was moving was sharp as he continues."
    LT "There are multiple power outages and unkowns when we arrive near the landing zone."
    "A loud screech is heard from the projector and a red light is projected out of it."
    "The lieutenant runs over to me grabbing the screeching projector.  something to me but the sound is way too loud for me to make out what he is saying."
    "He quickly brings the projector into the front of the osprey and the sound is muffled but still clear behind the door after a few minuets a loud spark is heard and the sound stops."
    "He walks back into the room side eyeing me and says"
    LT "Well it seems like you DID fix the projector. Maybe you are not as useless as you claim to be. Too bad the spark plug is burnt out."
    LT "The operation will be designated as operation flashpoint this operation will come in three phases our batalltion has been designated as delta 9 or DT9 for short."
    LT "We will be working in collaberation with another batalltion designated Nu-7. Doing a radiowave anylisis we were able to determine the central location of the main energy sources."
    BAG "W-what was that."
    "His voice is so low I almost did not notice him, nevertheless I answer with"
    BEN "I will tell you later"
    LT "Our main priortiy is to capture and secure the suspected perpetrator of this incident. Looking at your tactical map we will enter from the side windows on the second floor"
    LT "while team delta will enter through the side and main entrances. As you will be in two groups of three you will recommended to form a echelon right formation but if the situation calls for it you may break formation."
    LT "I and the other teams lutenent will stand gaurd outside while you breach and clear the rooms. It will be mandatory during this section to wear the protective gear provided to you, there is no telling what can await you inside that house."
    "I try to focus on something else to calm this madness I look to my side for my sidearm and realize, I never got any weapon."
    "I think about if I should tell this to the lutient but I already caused so much trouble for him already."
    "As I deliberate on if I should my thought is interrupted as "
    LT "Our targets details are classfied however it is imperative that we capture the target alive as he is the key to solving all of this. For any other unautherized personal a shoot on sight policy"
    LT "has been vetted and put in place by the ethics commite. Other organizations will be working closely with us on this mission so the policy is only autherized within 30ft of the targets location."
    LT "I can not stress the importance of capturing the target alive, Your secondary objectives are securing important personal and eliminating all unkown threats in the area."
    LT "The other phases of the plan will be relayed to you once the main objective is complete, do I have any questions?"
    "I look down on my empty lap and look back up, I see bagman give me a quick glance than look back up at the lieutenant."
    "He looks at me and chuckles "
    LT "You will get the projector and sidearm back don’t worry, I will add some straps to it so you can wear it on your back.."
    "The Osprey flies on..."
    return

label outsidewithoutuniform:
    scene bg_landing_zone_generic
    show ben_neutral at left
    show drill_sarg_talk at center
    DRI "Everyone is already gathered outside and people are gathering for a very important meeting you will follow me and points will be dedcuted since you are late."
    BEN "SIR YES SIR"
    "and we follow him outside to the landing zone. There are 5 ospery ships outside and soldiers lined up in rows."
    "I quickly head towards my platoon and stand in position. As i stand at the landing zone as a osprey lands, I look to the left to see samuel smiling and starting at the ospery,"
    "looking right I see the sargent standing firm looking determined. The drill sargent speaks pointing to me"
    DRI "Dirtbag, you may have proven yourself in fixing that projector but this will be the real test."
    "The wind from the ospery causes me to put my hands up to cover my eyes from the sheer force of it."
    DRI "This mission may be the last one you go on."
    DRI "I will be staying here, it is your problem now"
    "walking off."
    hide drill_sarg_talk
    "As he leaves I look back to the center the osprey a sargent walks downs the retractable stairs sizing up everyone."
    show lt_stern at center
    LT "We have a serious sitution on our hands."
    LT "The LZ will be hot by the time of arrival 30 mikes. Once you reach the landing zone you will secure it and evacuate any non combatince as you match your to point alpha."
    LT "Point alpha is a residential complex were your main target designated as the nest. Is there any questions?"
    LT "Good, *points to benjerman* make sure you bring that projector, it is essechial it gets dilvered to the nest"
    BEN "Yes sir!"
    "The drill sargent directs us all onto multiple opserys me and samuel are split up for the first time in awhile."
    "I almost start to worry about but than I calm I don't really care how he holds up on his own I sit down on my seat it feels nice and coushiny."
    hide ben_neutral
    hide lt_stern
    scene bg_osprey_interior_generic
    show ben_sitting at left
    "The first time I have sat down since the inital meeting. The lutenent jumps onto the ship i feel it shake a bit. I feel a tap on my sholder and look to my right."
    show bagman_default at center
    "I get startled as I see someone with a bag on there head sitting next to me."
    BAG "y-you forgot your weapon a-and your uniform"
    BEN "Huh?"
    "he turns around hiding his already hidden face with his hands."
    BEN "Why the hell are you wearing a bag of your head and not a helmet. Take that off,"
    "I reach for his bag and he slaps my hand saying"
    BAG "Don't touch that."
    "I figure it is best to not continue my advances to unmask him."
    LT "Is there a problem soldier."
    BEN "Yes sir! I do not have my weapon or my uniform."
    LT "We are behind schedule already so you will have to make due with what you have."
    BEN "But i have nothing!"
    LT "Well that is just too bad you will have to suck it up! I will read out your orders too."
    LT "Do you understand maggot!"
    "I feel someone put something on my lap lap looking down I see a pistol."
    $ inventory.append("Pistol")
    LT "I said DO YOU UNDERSTAND MAGGOT."
    BEN "SIR YES SIR."
    "As I look down at the gun on my lap the lutenent speaks up"
    LT "We have a very important mission on our hands, multiple undislosed beams of energy have began etruding from the earth. These beams seems to be eminating enrgy capable of blocking out radio and microwaves"
    LT "and have been classfied as a cognitohazard. You will be provided protective glasses and gear cabable of blocking out most of the harmful effects.”"
    "As he talks I hold the weapon in my lap feeling the tightness of the grip, feeling each bump and indent on the gun. I move my hand to the release as he continues."
    LT "There are multiple power outages and unkowns when we arrive near the landing zone. The operation will be designated as operation flashpoint this operation will come in three phases our batalltion has been designated as delta 9 or DT9 for short."
    LT "We will be working in collaberation with another batalltion designated Nu-7. Doing a radiowave anylisis we were able to determine the central location of the main energy sources."
    "The magazine falls out of the gun onto my lap I pick it up and look inside seeing all the bullets that will eventually be used in this gun. I slowly slot the magazine back into the gun."
    LT "Our main priortiy is to capture and secure the suspected perpetrator of this incident. Looking at your tactical map we will enter from the side windows on the second floor"
    LT "while team delta will enter through the side and main entrances. As you will be in two groups of three you will recommended to form a echelon right formation but if the situation calls for it you may break formation."
    LT "I and the other teams lutenent will stand gaurd outside while you breach and clear the rooms. It will be mandatory during this section to wear the protective gear provided to you, there is no telling what can await you inside that house."
    "I move my hand upwards slowly and rhythmically feeling the stock and eventually the whole cylinder of the gun, there are many guns like this here but this one is mine. I cock back the gun slowly. as "
    LT "Our targets details are classfied however it is imperative that we capture the target alive as he is the key to solving all of this. For any other unautherized personal a shoot on sight policy"
    LT "has been vetted and put in place by the ethics commite. Other organizations will be working closely with us on this mission so the policy is only autherized within 30ft of the targets location."
    LT "I can not stress the importance of capturing the target alive, Your secondary objectives are securing important personal and eliminating all unkown threats in the area."
    LT "The other phases of the plan will be relayed to you once the main objective is complete, do I have any questions?"
    "I leave my gun on my lap and look back up, I see bagman give me a quick glance than look back up at the lieutenant. Everyone looking at the lieutenant"
    "The journey continues..."
    return
label example_intelligence_check:
    $ base_chance = 30
    $ skill_level = stats["intelligence"]["level"]
    $ skill_name = "intelligence"
    $ total_bonuses = 5 # Example bonus

    "You attempt a difficult task requiring sharp wits."
    call screen roll_screen(base_chance, skill_level, skill_name, total_bonuses)

    $ roll_success = _return # The roll_screen will return True for success, False for failure
    if roll_success:
        "Your intelligence (and maybe that minigame!) helped you succeed!"
    else:
        "Despite your efforts, you couldn't quite figure it out."
    return