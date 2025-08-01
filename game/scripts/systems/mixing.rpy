# Combined File: Merged scripts for liquids combining, crafting, character status, and related functionalities.

# --- Default Variables ---
default holding_items = ["Glue", "Screwdriver", "Tape"]
default current_mode = "construction"
default selected_items = []
default stirring_progress = 0
default stirring_tool = None
default stirring_complete = False
default last_mouse_pos = (0, 0)
default stirring_direction = None
default stirring_count = 0
default is_mixing = False
default mixing_progress = 0
default current_mixing_step = 0
default mixing_attempts = 0
default input_amount = ""
default selected_container = None
default selected_liquids = []
default mixing_steps = ["top", "right", "bottom", "left"]

# --- Init Python Block (Merged and Resolved Duplicates) ---
init python:
    # From File 1 (non-overlapping or placeholders replaced by File 2 implementations)
    selected_liquids = []  # Already defaulted, but keeping for consistency
    selected_container = None  # Already defaulted

    def add_liquid(liquid_name, amount):
        for liquid in liquid_inventory:
            if liquid["name"] == liquid_name:
                liquid["amount"] += amount
                break

    def remove_liquid(liquid_name, amount):
        for liquid in liquid_inventory:
            if liquid["name"] == liquid_name:
                if liquid["amount"] >= amount: liquid["amount"] -= amount
                else: renpy.notify("Not enough liquid available.")
                break

    def has_stirring_tool(tool):
        return True  # Placeholder, assume always true for testing

    # From File 2 (implementations overriding placeholders from File 1)
    def remove_from_list(list_var, item):
        if item in list_var:
            list_var.remove(item)
            renpy.notify(f"Removed {item} from selection.")

    def select_item(item):
        if item not in selected_items and len(selected_items) < 2:
            selected_items.append(item)

    def combine_items(player_obj):  
        global selected_items
        if len(selected_items) != 2:
            renpy.notify("You need exactly two items to combine.")
            return

        item_tuple = tuple(sorted(selected_items))
        if item_tuple in crafting_recipes:
            recipe = crafting_recipes[item_tuple]
            holding_item = recipe["holding_item"]

            if holding_item == "Glue":
                glue_available = any(liquid["name"] == "Glue" and liquid["amount"] > 0 for liquid in player_obj.inventory.liquids)
                if not glue_available:
                    renpy.notify("You need Glue to hold the items together.")
                    return
            elif not any(i["name"] == holding_item for i in player_obj.inventory.items):
                renpy.notify(f"You need {holding_item} to hold the items together.")
                return

            new_item = recipe["result"]
            player_obj.inventory.add_item(new_item)
            for item in selected_items:
                player_obj.inventory.remove_item(item)

            if holding_item == "Glue":
                for liquid in player_obj.inventory.liquids:
                    if liquid["name"] == "Glue":
                        liquid["amount"] -= 10
                        if liquid["amount"] <= 0:
                            player_obj.inventory.liquids.remove(liquid)
                        break

            renpy.notify(f"You crafted: {new_item} using {holding_item}.")
            selected_items = []
        else:
            renpy.notify("These items cannot be combined.")

    def deconstruct_item(player_obj, item):  # Pass player_obj
        if item in deconstruction_recipes and any(i["name"] == item for i in player_obj.inventory.items):
            components = deconstruction_recipes[item]
            for component in components:
                player_obj.inventory.add_item(component)
            player_obj.inventory.remove_item(item)
            renpy.notify(f"You deconstructed {item} into: {', '.join(components)}.")
        else:
            renpy.notify(f"{item} cannot be deconstructed or is not in inventory.")

    def add_liquid_to_selected(liquid, amount):
        if not selected_container:
            return
        if selected_container["current_amount"] + amount > selected_container["capacity"]:
            renpy.notify("Not enough space in the container!")
            return
        if amount > liquid["amount"]:
            renpy.notify("Not enough liquid available!")
            return

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

    def mix_liquids(container, liquids):
        recipe_name = check_mix_recipe(container)
        if recipe_name:
            total_volume = sum(c["amount"] for c in container["contents"])
            container["contents"] = [{"name": recipe_name, "amount": total_volume}]
            container["current_amount"] = total_volume
            renpy.notify(f"Successfully created {recipe_name}!")
        else:
            renpy.notify("No valid recipe found. The mixture turned into sludge.")
            container["contents"] = [{"name": "Sludge", "amount": container["current_amount"]}]

    def check_mix_recipe(container):
        container_liquids = {c["name"]: c["amount"] for c in container["contents"]}
        for recipe_name, recipe_ingredients in liquid_mix_recipes.items():
            if all(ingredient in container_liquids and container_liquids[ingredient] >= amount for ingredient, amount in recipe_ingredients.items()):
                return recipe_name
        return None

    def drain_liquid(container):
        if container["contents"]:
            container["contents"].clear()
            container["current_amount"] = 0
            renpy.notify(f"Drained all liquid from the {container['name']}.")

    def pour_liquid(source_container, target_container):
        if source_container["contents"]:
            total_pour_amount = source_container["current_amount"]
            if target_container:
                if target_container["current_amount"] + total_pour_amount <= target_container["capacity"]:
                    target_container["contents"].extend(source_container["contents"])
                    target_container["current_amount"] += total_pour_amount
                    source_container["contents"].clear()
                    source_container["current_amount"] = 0
                    renpy.notify(f"Poured contents from {source_container['name']} to {target_container['name']}.")
                else:
                    renpy.notify("Not enough space in the target container!")
            else: # Pour to ground
                source_container["contents"].clear()
                source_container["current_amount"] = 0
                renpy.notify(f"Poured contents from {source_container['name']} to the ground.")

    def update_stirring_progress():
        global stirring_progress, last_mouse_pos, stirring_direction, stirring_count, stirring_complete
        current_mouse_pos = renpy.get_mouse_pos()
        if last_mouse_pos != (0, 0):
            dx = current_mouse_pos[0] - last_mouse_pos[0]; dy = current_mouse_pos[1] - last_mouse_pos[1]
            if abs(dx) > abs(dy): new_direction = "right" if dx > 0 else "left"
            else: new_direction = "down" if dy > 0 else "up"
            if stirring_direction and \
               ((stirring_direction, new_direction) in [("right", "down"), ("down", "left"), ("left", "up"), ("up", "right")]):
                stirring_count += 1
                if stirring_count >= 4:
                    stirring_progress += 10; stirring_count = 0
                    if stirring_progress >= 100:
                        stirring_progress = 100; stirring_complete = True; renpy.notify("Stirring complete!")
                        mix_liquids(selected_container, selected_liquids)
            stirring_direction = new_direction
        last_mouse_pos = current_mouse_pos

    def reset_stirring():
        global stirring_tool, stirring_progress, stirring_complete, last_mouse_pos, stirring_direction, stirring_count
        stirring_tool, stirring_progress, stirring_complete = None, 0, False
        last_mouse_pos, stirring_direction, stirring_count = (0, 0), None, 0

    def handle_mixing_click(direction):
        global current_mixing_step, mixing_attempts
        if direction == mixing_steps[current_mixing_step]:
            current_mixing_step += 1
            if current_mixing_step >= len(mixing_steps):
                current_mixing_step = 0; mixing_attempts += 1
                if mixing_attempts >= 2:
                    renpy.notify("Mixing complete!"); mix_liquids(selected_container, selected_liquids); reset_mixing()
                else:
                    renpy.notify(f"Step {mixing_attempts + 1}: Continue mixing!")
        else:
            renpy.notify("Wrong direction! Start over."); reset_mixing()

    def reset_mixing():
        global current_mixing_step, mixing_attempts
        current_mixing_step, mixing_attempts = 0, 0

    def handle_mixing_motion():
        global mixing_progress, is_mixing
        if is_mixing:
            mixing_progress += renpy.random.randint(1, 3)
            if mixing_progress >= 100:
                mixing_progress = 100; is_mixing = False; renpy.notify("Mixing complete!")
                mix_liquids(selected_container, selected_liquids)

# --- Screens (Merged from Both Files) ---

# From File 1: combine_liquids_screen
screen combine_liquids_screen(player_obj):
    modal True
    tag liquids

    frame:
        style "section_frame"
        xysize (1000, 700)
        xalign 0.5 yalign 0.5

        vbox:
            spacing 15
            text "Liquid Station" size 30 xalign 0.5 color "#FFFFFF"

            hbox:
                spacing 20

                vbox:
                    spacing 10
                    text "Available Pure Liquids" size 20 color "#FFFFFF"
                    frame:
                         style "section_frame"
                         background "#2E4F2E"
                         padding (10, 10, 10, 10)
                         xsize 250 ysize 550
                         viewport:
                             scrollbars "vertical" mousewheel True
                             vbox:
                                 spacing 8
                                 if not player_obj.inventory.liquids:  # Use obj.inventory.liquids
                                     text "- None -" size 14 color "#AAAAAA"
                                 for liquid in player_obj.inventory.liquids:  # Use obj.inventory.liquids
                                      if liquid.get("amount", 0) > 0:
                                          text f"{liquid['name']}: {liquid['amount']} ml" size 16 color "#DDDDDD"
                                          if selected_container:
                                               textbutton "Add to Bottle" action Show("input_amount_screen", liquid=liquid) style "inventory_button" text_size 12 padding (5,2) sensitive (selected_container["current_amount"] < selected_container["capacity"])

                vbox:
                    spacing 10
                    text "Containers" size 20 color "#FFFFFF"
                    frame:
                         style "section_frame"
                         background "#2E4F2E"
                         padding (10, 10, 10, 10)
                         xsize 300 ysize 550
                         viewport:
                             scrollbars "vertical" mousewheel True
                             vbox:
                                 spacing 8
                                 if not player_obj.inventory.containers:  # Use obj.inventory.containers
                                      text "- None -" size 14 color "#AAAAAA"
                                 for container in player_obj.inventory.containers:  # Use obj.inventory.containers
                                      button:
                                          action SetVariable("selected_container", container)
                                          hbox:
                                              spacing 10
                                              $ img_path = "images/inventory/" + container['name'].replace(" ", "_") + ".png"
                                              if renpy.loadable(img_path):
                                                  add img_path zoom 0.3
                                              else:
                                                  frame:
                                                      xysize(30,30)
                                                      background "#AAAAAA"

                                              vbox:
                                                  text container["name"] size 16 color ("#FFFF88" if selected_container == container else "#FFFFFF")
                                                  text f"{container['current_amount']} / {container['capacity']} ml" size 14 color "#CCCCCC"
                                                  bar value container["current_amount"] range container["capacity"] xsize 100

                vbox:
                    spacing 10
                    text "Selected Container" size 20 color "#FFFFFF"
                    frame:
                         style "section_frame"
                         background "#2E4F2E"
                         padding (10, 10, 10, 10)
                         xsize 350 ysize 550
                         if selected_container:
                             vbox:
                                 spacing 8
                                 text selected_container["name"] size 18 color "#FFFF88" xalign 0.5
                                 $ img_path = "images/inventory/" + selected_container['name'].replace(" ", "_") + ".png"
                                 if renpy.loadable(img_path):
                                     add img_path zoom 0.5 xalign 0.5
                                 else:
                                     frame:
                                         xysize(60,60)
                                         background "#AAAAAA"
                                         xalign 0.5

                                 bar value selected_container["current_amount"] range selected_container["capacity"] xsize 250 xalign 0.5
                                 text f"{selected_container['current_amount']} / {selected_container['capacity']} ml" size 16 color "#CCCCCC" xalign 0.5

                                 text "Contents:" size 16 color "#FFFFFF"
                                 if not selected_container["contents"]:
                                     text "- Empty -" color "#AAAAAA"
                                 else:
                                     for content in selected_container["contents"]:
                                         text f"- {content.get('name', 'Unknown')}: {content.get('amount', 0)} ml" size 14 color "#DDDDDD"

                                 null height 15
                                 text "Actions:" size 16 color "#FFFFFF"
                                 textbutton "Pour Into..." action Show("liquid_pour_target_screen", source_container=selected_container, player_obj=player_obj) style "inventory_button" sensitive (selected_container["current_amount"] > 0)
                                 if len(selected_container["contents"]) >= 2:
                                     textbutton "Mix Contents" action [Function(reset_stirring), Show("stirring_minigame")] style "inventory_button"

                         else:
                             text "Select a container from the list." xalign 0.5 yalign 0.5 color "#AAAAAA"

            null height 10
            textbutton "Close Liquids" action [SetVariable("selected_container", None), Hide("liquids")] style "inventory_button" xalign 0.5

# From File 1: liquid_pour_target_screen
screen liquid_pour_target_screen(source_container, player_obj):
     modal True

     frame:
         style "section_frame"
         padding (20, 20, 20, 20)
         xalign 0.5 yalign 0.5

         vbox:
             spacing 10
             text f"Pour from {source_container['name']} into:" size 20 color "#FFFFFF"

             viewport:
                 ysize 300
                 scrollbars "vertical" mousewheel True
                 vbox:
                     spacing 8
                     textbutton "Ground" action [Function(pour_liquid, source_container, None), Hide("liquid_pour_target_screen")] style "inventory_button"
                     if not player_obj.inventory.containers:
                         text "- No other containers -" size 14 color "#AAAAAA"
                     for target_container in player_obj.inventory.containers:
                         if target_container != source_container:
                             $ available_space = target_container["capacity"] - target_container["current_amount"]
                             textbutton f"{target_container['name']} ({available_space} ml space)" action [Function(pour_liquid, source_container, target_container), Hide("liquid_pour_target_screen")] style "inventory_button" sensitive (available_space > 0)

             null height 10
             textbutton "Cancel" action Hide("liquid_pour_target_screen") style "inventory_button"

# From File 1: stirring_minigame (with File 2's implementation in mind)
screen stirring_minigame():
    modal True

    frame:
        style "section_frame"
        xysize (500, 500)
        xalign 0.5 yalign 0.5

        vbox:
            spacing 15
            text "Mix Liquids" size 25 color "#FFFFFF" xalign 0.5

            text "Select Stirring Tool:" size 18 color "#DDDDDD" xalign 0.5
            hbox:
                xalign 0.5 spacing 10
                $ possible_tools = ["Stick", "Spoon", "Hand"]
                for tool in possible_tools:
                    if has_stirring_tool(tool):
                        textbutton tool action SetVariable("stirring_tool", tool) style "inventory_button"
                    else:
                        textbutton tool action None style "inventory_button" sensitive False

            if stirring_tool:
                text f"Using: {stirring_tool}" size 16 color "#FFFF88" xalign 0.5
                null height 20

                frame:
                    background "#0A200A"
                    xysize (300, 200) xalign 0.5
                    text "Stir Here (Mouse Movement)" xalign 0.5 yalign 0.5 color "#AAAAAA"
                    timer 0.1 repeat True action Function(update_stirring_progress)

                null height 10
                bar value stirring_progress range 100 xsize 300 xalign 0.5 left_bar "#4CAF50" right_bar "#2A4A2A"
                text f"Progress: {stirring_progress}%" size 16 color "#FFFFFF" xalign 0.5

                if stirring_complete:
                    text "Mixing Complete!" size 18 color "#4CAF50" xalign 0.5
                    textbutton "Finalize Mix" action [Function(mix_liquids, selected_container, selected_liquids), Hide("stirring_minigame")] style "inventory_button"

            else:
                 text "Select a tool to begin stirring." size 16 color "#AAAAAA" xalign 0.5

            null height 20
            textbutton "Cancel Mixing" action [Function(reset_stirring), Hide("stirring_minigame")] style "inventory_button" xalign 0.5

# From File 1: input_amount_screen
screen input_amount_screen(liquid):
    default amount_to_add = ""

    modal True
    frame:
        xsize 400
        ysize 200
        xalign 0.5
        yalign 0.5
        background "#1B3D1B"
        padding (20, 20)

        vbox:
            spacing 10
            text "Enter Amount to Add (ml):" size 20 color "#FFFFFF"

            # Input field for the amount
            input value ScreenVariableInputValue("amount_to_add") length 5 allow "0123456789" color "#FFFFFF" size 20

            hbox:
                spacing 20
                textbutton "Add":
                    action [
                        Function(add_liquid_to_selected, liquid, int(amount_to_add) if amount_to_add.isdigit() else 0),
                        Hide("input_amount_screen")
                    ]
                textbutton "Cancel":
                    action Hide("input_amount_screen")

# From File 1: use_liquid_screen
screen use_liquid_screen():
    modal True
    frame:
        xsize 400
        ysize 400
        xalign 0.5
        yalign 0.5
        background "#113111"
        padding (20, 20)

        vbox:
            spacing 10
            label "Use Liquid" text_size 30 text_color "#FFFFFF"
            text "Select a liquid to use:" size 18 color "#FFFFFF"

            for liquid in inventory:
                if liquid["type"] == "liquid":
                    frame:
                        background "#1E4A1E"
                        padding (10, 10)
                        hbox:
                            text f"{liquid['name']} - {liquid['amount']}ml available" size 18 color "#FFFFFF"
                            textbutton "Use" action [Function(use_liquid, liquid), Hide("use_liquid_screen")] style "inventory_button"

            textbutton "Cancel" action Hide("use_liquid_screen") style "inventory_button" xalign 0.5

# From File 1: character_status_screen
screen character_status_screen(player_obj):
    modal True
    tag status

    frame:
        style "section_frame"
        xysize (900, 700)
        xalign 0.5 yalign 0.5

        vbox:
            spacing 10
            text "Character Status" size 30 xalign 0.5 color "#FFFFFF"

            hbox:
                xalign 0.5 spacing 15
                textbutton "Body" action SetVariable("selected_tab", "Body") style "inventory_button" sensitive (selected_tab != "Body")
                textbutton "Stats" action SetVariable("selected_tab", "Stats") style "inventory_button" sensitive (selected_tab != "Stats")

            null height 15

            if selected_tab == "Body":
                python:
                    avg_health, avg_clean, avg_temp = player_obj.calculate_averages()
                text f"Overall: Health {avg_health}% | Cleanliness {avg_clean}% | Temp {avg_temp}°" size 18 xalign 0.5 color "#CCCCCC"

                viewport:
                    ysize 500
                    scrollbars "vertical" mousewheel True
                    grid 2 3:
                        spacing 15

                        for part, status_dict in player_obj.health.items():
                            frame:
                                style "section_frame"
                                background "#2E4F2E"
                                padding (10, 10, 10, 10)
                                vbox:
                                    spacing 5
                                    text part.replace("_", " ").title() size 18 color "#FFFF88"
                                    text f"Status: {status_dict.get('status', 'N/A')}" size 14
                                    text "Health:" size 14
                                    bar value status_dict.get('health', 0) range 100 xsize 150 left_bar "red" right_bar "#550000"
                                    text "Temp:" size 14
                                    bar value status_dict.get('temperature', 0) range 120 xsize 150 left_bar "orange" right_bar "#663300"
                                    text "Cleanliness:" size 14
                                    bar value status_dict.get('cleanliness', 0) range 100 xsize 150 left_bar "lightblue" right_bar "#003366"

                                    text "Conditions:" size 14
                                    if not status_dict.get('conditions'):
                                        text "- None -" size 12 color "#AAAAAA"
                                    else:
                                        for condition in status_dict.get('conditions'):
                                            text f"- {condition}" size 12 color "#FFAAAA"

                                    textbutton "Treat" action Show("medkit_screen", player_obj=player_obj, target_part=part) style "inventory_button" text_size 12 padding(5,2)

            elif selected_tab == "Stats":
                viewport:
                    ysize 500
                    scrollbars "vertical" mousewheel True
                    vbox:
                        spacing 15
                        for stat_name, data in player_obj.stats.items():
                            if stat_name == "sanity":
                                continue
                            frame:
                                style "section_frame"
                                background "#2E4F2E"
                                padding (10, 10, 10, 10)
                                hbox:
                                    spacing 10
                                    python:
                                        stat_img_path = "images/stats_icons/" + stat_name + ".png"
                                    if renpy.loadable(stat_img_path):
                                        add stat_img_path xysize (50, 50)
                                    else:
                                        frame style "stat_icon" background "#444444":
                                            xysize(50, 50)
                                            text stat_name[0].upper() size 30 xalign 0.5 yalign 0.5

                                    vbox:
                                        spacing 2
                                        text stat_name.title() size 18 color "#FFFF88"
                                        text f"Level: {data.get('level', 0)}" size 14
                                        text f"Value: {data.get('current_value', 0)}" size 14
                                        text "XP:" size 14
                                        bar value data.get('current_xp', 0) range data.get('max_xp', 100) xsize 200

                if "sanity" in player_obj.stats:
                    frame:
                        style "section_frame"
                        background "#2E4F2E"
                        padding (10, 10, 10, 10)
                        hbox:
                            spacing 10
                            python:
                                sanity_img_path = "images/stats_icons/sanity.png"
                            if renpy.loadable(sanity_img_path):
                                add sanity_img_path xysize (50, 50)
                            else:
                                frame style "stat_icon" background "#444444":
                                    xysize (50, 50)
                                    text "S" size 30 xalign 0.5 yalign 0.5

                            vbox:
                                text f"Sanity: {player_obj.stats['sanity'].get('current_sanity', 100)}%" size 18 color "#CCCCCC"
                                bar value player_obj.stats['sanity'].get('current_sanity', 100) range 100 xsize 250 left_bar "#AA00FF" right_bar "#330055"

            null height 15
            textbutton "Close Status" action Hide("status") style "inventory_button" xalign 0.5

# From File 2: crafting_screen
screen crafting_screen(player_obj):
    modal True
    tag crafting

    frame:
        style "section_frame"
        xysize (800, 600)
        xalign 0.5 yalign 0.5

        vbox:
            spacing 10
            text "Workshop" size 30 xalign 0.5 color "#FFFFFF"

            hbox:
                xalign 0.5
                spacing 20
                textbutton "Construction" action SetVariable("current_mode", "construction") style "inventory_button" sensitive (current_mode != "construction")
                textbutton "Destruction" action SetVariable("current_mode", "destruction") style "inventory_button" sensitive (current_mode != "destruction")

            if current_mode == "construction":
                hbox:
                    spacing 15
                    vbox:
                        text "Available Items" size 20 color "#FFFFFF"
                        viewport:
                            ysize 400 xsize 300
                            scrollbars "vertical" mousewheel True
                            vbox:
                                spacing 5
                                for item in player_obj.inventory.items:
                                    $ item_id = item["name"]
                                    if item_id not in selected_items:
                                        $ details = items_database.get(item_id)
                                        if details:
                                            hbox:
                                                spacing 10
                                                $ img_path = "images/inventory/" + item_id.replace(" ", "_") + ".png"
                                                if renpy.loadable(img_path):
                                                    add img_path zoom 0.3
                                                else:
                                                    frame:
                                                        xysize(20,20)

                                                text item_id size 14 color "#DDDDDD"
                                                textbutton "Select" action Function(select_item, item_id) style "inventory_button" text_size 14 padding (5,2) sensitive (len(selected_items) < 2)

                    vbox:
                        spacing 10
                        text "Selected for Combining" size 20 color "#FFFFFF"
                        frame:
                            style "slot_frame"
                            background "#2E4F2E"
                            xsize 400 ysize 150
                            padding (10, 10, 10, 10)
                            if not selected_items:
                                text "Select 2 items" xalign 0.5 yalign 0.5 color "#AAAAAA"
                            else:
                                grid 2 1:
                                     for sel_id in selected_items:
                                         $ sel_details = items_database.get(sel_id)
                                         if sel_details:
                                             vbox:
                                                 $ img_path = "images/inventory/" + sel_id.replace(" ", "_") + ".png"
                                                 if renpy.loadable(img_path):
                                                     add img_path zoom 0.4 xalign 0.5
                                                 else:
                                                     text sel_id size 12 xalign 0.5

                                                 text sel_id size 12 color "#DDDDDD" xalign 0.5
                                                 textbutton "Remove" action Function(remove_from_list, selected_items, sel_id) style "inventory_button" text_size 12 padding (5,2)

                        text "Select Holding Item (Required for some recipes):" size 16 color "#FFFFFF"
                        viewport:
                             ysize 100 xsize 400
                             scrollbars "horizontal"
                             mousewheel True
                             hbox:
                                 spacing 8
                                 textbutton "None" action SetVariable("selected_holding_item", None) style "inventory_button" text_size 12 padding (5,2) sensitive (selected_holding_item is not None)

                                 for hold_item in holding_items:
                                     textbutton hold_item action SetVariable("selected_holding_item", hold_item) style "inventory_button" text_size 12 padding (5,2) sensitive (selected_holding_item != hold_item)

                        null height 10
                        textbutton "Combine" action Function(combine_items, player_obj) style "inventory_button" sensitive (len(selected_items) == 2)  # Pass player_obj

            elif current_mode == "destruction":
                 vbox:
                     text "Select Item to Deconstruct" size 20 color "#FFFFFF"
                     viewport:
                         ysize 400 xsize 700
                         scrollbars "vertical" mousewheel True
                         grid 5 5:
                             spacing 10
                             for item in player_obj.inventory.items:
                                 python:
                                     item_id = item["name"]
                                     _details = items_database.get(item_id)
                                     _tooltip_text = "Unknown Item"
                                     _can_deconstruct = item_id in deconstruction_recipes
                                     if _details:
                                         _tooltip_text = _details.get("description", item_id)
                                         if not _can_deconstruct:
                                             _tooltip_text = "Cannot deconstruct"
                                     _img_path = "images/inventory/" + item_id.replace(" ", "_") + ".png"

                                 if _can_deconstruct:
                                     button:
                                         style "slot_frame"
                                         action [Function(deconstruct_item, player_obj, item_id), Hide("crafting")]  # Pass player_obj
                                         tooltip _tooltip_text
                                         if renpy.loadable(_img_path):
                                             add _img_path xalign 0.5 yalign 0.5 zoom 0.7
                                         else:
                                             text item_id size 12 xalign 0.5 yalign 0.5

                                 else:
                                     frame:
                                         style "slot_frame"
                                         background "#444444"
                                         tooltip _tooltip_text
                                         if _details:
                                             if renpy.loadable(_img_path):
                                                 add _img_path xalign 0.5 yalign 0.5 zoom 0.7 alpha 0.5
                                             else:
                                                 text item_id size 12 xalign 0.5 yalign 0.5 color "#888888"


            null height 20
            textbutton "Close Workshop" action [SetVariable("selected_items", []), SetVariable("selected_holding_item", None), Hide("crafting")] style "inventory_button"