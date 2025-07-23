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


init python:
    def remove_from_list(list_var, item):
        if item in list_var:
            list_var.remove(item)
            renpy.notify(f"Removed {item} from selection.")

    def select_item(item):
        if item not in selected_items and len(selected_items) < 2:
            selected_items.append(item)

    def combine_items(player_obj):  # Pass player_obj
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

# --- Crafting Screen (Updated with remove_from_list) ---
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