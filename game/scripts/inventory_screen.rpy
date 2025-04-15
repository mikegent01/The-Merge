# --- Styles (Keep these as they are) ---
style inventory_button:
    padding (10, 5)
    xalign 0.5

style slot_frame:
    background "#728477" # Example style
    padding (5, 5, 5, 5) # Corrected padding
    xysize (100, 100) # Smaller default size

style section_frame:
    background "#113111" # Example style
    padding (15, 15)

# Style for stat icons - NOTE: This style definition itself isn't used directly by 'add',
# but we use its properties (xysize) on the 'add' statement below.
style stat_icon:
    xysize (50, 50) # Adjust size as needed

# --- --- --- INVENTORY SYSTEM --- --- ---

# --- Main Inventory Screen ---
screen inventory():
    modal True
    tag inventory # Tag for easy showing/hiding

    frame:
        style "section_frame"
        xysize (1100, 750) # Adjusted size
        xalign 0.5
        yalign 0.5

        hbox: # Main layout: Inventory Grid | Details/Equipped
            spacing 20

            # --- Left Pane: Inventory Grid ---
            vbox:
                frame: # Frame around the grid section
                    style "section_frame"
                    ysize (710) # Reduced to fit new main frame height
                    xsize (500) # Give it a bit less width

                    vbox:
                        spacing 10
                        text "Inventory" size 30 xalign 0.5 color "#FFFFFF"
                        python:
                             _inv_weight = calculate_total_weight()
                             _remaining_slots = get_remaining_space()
                             _max_slots_display = max_space
                             _grid_cols = 4
                             _grid_rows = max_space // _grid_cols + (1 if max_space % _grid_cols else 0)
                        text f"Weight: {_inv_weight:.1f} kg" size 16 xalign 0.5 color "#CCCCCC"
                        text f"Slots: {len(inventory)} / {max_space}" size 16 xalign 0.5 color "#CCCCCC"

                        viewport:
                            draggable True
                            mousewheel True
                            scrollbars "vertical"
                            ysize 580

                            grid _grid_cols _grid_rows:
                                xfill True
                                spacing 10

                                for item_id in inventory:
                                    python:
                                        _details = items.get(item_id)
                                        _tooltip_text = "Unknown Item"
                                        if _details:
                                            _tooltip_text = _details.get("description", item_id)
                                        _img_path = "images/inventory/" + item_id.replace(" ", "_") + ".png"

                                    if _details:
                                        button:
                                            style "slot_frame"
                                            xysize (90, 90)
                                            action SetVariable("selected_item", item_id)
                                            tooltip _tooltip_text

                                            if renpy.loadable(_img_path):
                                                add _img_path xalign 0.5 yalign 0.5 zoom 0.6
                                            else:
                                                text item_id size 10 xalign 0.5 yalign 0.5

                                $ filled_slots = len(inventory)
                                for i in range(filled_slots, max_space):
                                    frame:
                                        style "slot_frame"
                                        xysize (90, 90)
                                        background "#556655"
                                        text "Empty" xalign 0.5 yalign 0.5 color "#AAAAAA" size 10


            # --- Right Pane: Details or Equipped View ---
            vbox:
                frame:
                    style "section_frame"
                    ysize (650)
                    xsize (540)

                    viewport:
                        scrollbars "vertical"
                        mousewheel True

                        if selected_item:
                            use item_details_panel(item_id=selected_item)
                        else:
                            use equipped_items_panel()

                null height 10
                hbox:
                    xalign 0.5
                    spacing 15
                    textbutton "Crafting" action [SetVariable("selected_items", []), Show("crafting_screen")] style "inventory_button"
                    textbutton "Liquids" action [SetVariable("selected_container", None), Show("combine_liquids_screen")] style "inventory_button"
                  #  textbutton "Status" action Show("character_status_screen") style "inventory_button"
                  #  textbutton "Journal" action Show("journal_screen") style "inventory_button"
                    textbutton "Close" action [SetVariable("selected_item", None), Hide("inventory")] style "inventory_button"


# --- Item Details Panel (Used by inventory_display) ---
screen item_details_panel(item_id):
    $ details = items.get(item_id)
    $ item_weight = get_item_weight(item_id)
    $ item_desc = get_item_description(item_id)

    if details:
        vbox:
            spacing 15
            # FIX: Removed invalid padding from vbox
            # padding (10, 10)
            text "Selected Item" size 25 xalign 0.5 color "#FFFFFF"

            frame:
                style "slot_frame"
                xysize (180, 180)
                xalign 0.5
                $ img_path = "images/inventory/" + item_id.replace(" ", "_") + ".png"
                if renpy.loadable(img_path):
                     add img_path xalign 0.5 yalign 0.5
                else:
                     text item_id size 14 xalign 0.5 yalign 0.5

            text f"Name: {item_id}" size 18 color "#FFFFFF" xalign 0.5
            text f"Weight: {item_weight} kg" size 16 color "#CCCCCC" xalign 0.5
            text f"Type: {details.get('type', 'N/A')}" size 16 color "#CCCCCC" xalign 0.5
            text f"Desc: {item_desc}" size 16 color "#DDDDDD" xalign 0.5

            null height 10

            hbox:
                xalign 0.5
                spacing 10
                textbutton "Equip" action Show("slot_selection_screen", item_id=item_id) style "inventory_button"
                textbutton "Use" action [Function(use_item, item_id), SetVariable("selected_item", None), Hide("inventory")] style "inventory_button"
                textbutton "Discard" action [Function(remove_item, item_id)] style "inventory_button"

            textbutton "Deselect" action SetVariable("selected_item", None) style "inventory_button"

    else:
        text "Error: Item details not found." xalign 0.5 color "#FF8888"


# --- Equipped Items Panel (Used by inventory_display) ---
screen equipped_items_panel():
    vbox:
        spacing 15
        # FIX: Removed invalid padding from vbox
        # padding (10, 10)
        text "Equipped Items" size 25 xalign 0.5 color "#FFFFFF"

        # Head
        hbox:
            xalign 0.5
            use equipment_slot_display(slot_name="head", current_item_id=head_item)

        # Hands and Body Row
        hbox:
            xalign 0.5
            spacing 5
            use equipment_slot_display(slot_name="left_hand", current_item_id=left_hand_item)
            use equipment_slot_display(slot_name="body", current_item_id=body_item)
            use equipment_slot_display(slot_name="right_hand", current_item_id=right_hand_item)

        # Legs Row
        hbox:
            xalign 0.5
            spacing 5
            use equipment_slot_display(slot_name="left_leg", current_item_id=left_leg_item)
            use equipment_slot_display(slot_name="right_leg", current_item_id=right_leg_item)

# --- Reusable Equipment Slot Display ---
screen equipment_slot_display(slot_name, current_item_id):
    $ details = items.get(current_item_id) if current_item_id else None

    frame:
        style "slot_frame"
        xysize (90, 90)
        tooltip slot_name.replace("_", " ").title()

        vbox:
            if details:
                $ img_path = "images/inventory/" + current_item_id.replace(" ", "_") + ".png"
                if renpy.loadable(img_path):
                     add img_path xalign 0.5 yalign 0.5 zoom 0.6
                else:
                     text current_item_id size 10 xalign 0.5 yalign 0.5

                hbox:
                    xalign 0.5
                    spacing 5
                    textbutton "U" action [Function(use_item, current_item_id), Hide("inventory")] style "inventory_button" text_size 10 padding (2,2) tooltip "Use"
                    textbutton "X" action Function(unequip_item, slot_name) style "inventory_button" text_size 10 padding (2,2) tooltip "Unequip"
            else:
                text "Empty" xalign 0.5 yalign 0.5 color "#AAAAAA" size 10


# --- Slot Selection Screen ---
screen slot_selection_screen(item_id):
    modal True
    $ details = items.get(item_id)
    $ item_type = details.get("type") if details else None

    frame:
        style "section_frame"
        xysize (400, 350)
        xalign 0.5 yalign 0.5

        vbox:
            spacing 15
            text f"Equip {item_id} To:" size 20 xalign 0.5 color "#FFFFFF"

            if item_type == "head":
                textbutton "Head" action [Function(equip_item, item_id, "head"), Hide("slot_selection_screen")] style "inventory_button"
            elif item_type == "body":
                textbutton "Body" action [Function(equip_item, item_id, "body"), Hide("slot_selection_screen")] style "inventory_button"
            elif item_type == "weapon" or item_type == "tool":
                textbutton "Left Hand" action [Function(equip_item, item_id, "left_hand"), Hide("slot_selection_screen")] style "inventory_button"
                textbutton "Right Hand" action [Function(equip_item, item_id, "right_hand"), Hide("slot_selection_screen")] style "inventory_button"
            elif item_type == "legs":
                 textbutton "Left Leg" action [Function(equip_item, item_id, "left_leg"), Hide("slot_selection_screen")] style "inventory_button"
                 textbutton "Right Leg" action [Function(equip_item, item_id, "right_leg"), Hide("slot_selection_screen")] style "inventory_button"
            elif item_type == "consumable":
                 textbutton "Body (Consume)" action [Function(equip_item, item_id, "body"), Hide("slot_selection_screen")] style "inventory_button"
            else:
                text "This item type cannot be equipped directly." color "#FFAAAA" xalign 0.5

            textbutton "Cancel" action Hide("slot_selection_screen") style "inventory_button"


# --- --- --- CRAFTING SYSTEM --- --- ---
screen crafting_screen():
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
                                for item_id in inventory:
                                    if item_id not in selected_items:
                                        $ details = items.get(item_id)
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
                                         $ sel_details = items.get(sel_id)
                                         if sel_details:
                                             vbox:
                                                 $ img_path = "images/inventory/" + sel_id.replace(" ", "_") + ".png"
                                                 if renpy.loadable(img_path):
                                                     add img_path zoom 0.4 xalign 0.5
                                                 else:
                                                     text sel_id size 12 xalign 0.5

                                                 text sel_id size 12 color "#DDDDDD" xalign 0.5
                                                 textbutton "Remove" action RemoveFromList(selected_items, sel_id) style "inventory_button" text_size 12 padding (5,2)

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
                        textbutton "Combine" action Function(combine_items) style "inventory_button" sensitive (len(selected_items) == 2)

            elif current_mode == "destruction":
                 vbox:
                     text "Select Item to Deconstruct" size 20 color "#FFFFFF"
                     viewport:
                         ysize 400 xsize 700
                         scrollbars "vertical" mousewheel True
                         grid 5 5:
                             spacing 10
                             for item_id in inventory:
                                 python:
                                     _details = items.get(item_id)
                                     _tooltip_text = "Unknown Item"
                                     _can_deconstruct = item_id in deconstruction_recipes
                                     if _details:
                                         _tooltip_text = _details.get("description", item_id)
                                         if not _can_deconstruct:
                                             _tooltip_text = "Cannot deconstruct"
                                     _img_path = "images/inventory/" + item_id.replace(" ", "_") + ".png"

                                 if _can_deconstruct:
                                     if _details:
                                         button:
                                              style "slot_frame"
                                              action [Function(deconstruct_item, item_id), Hide("crafting")]
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


# --- --- --- LIQUID SYSTEM --- --- ---
screen combine_liquids_screen():
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
                                 if not liquid_inventory:
                                     text "- None -" size 14 color "#AAAAAA"
                                 for liquid in liquid_inventory:
                                      if liquid.get("amount", 0) > 0:
                                          text f"{liquid['name']}: {liquid['amount']} ml" size 16 color "#DDDDDD"
                                          if selected_container:
                                               textbutton "Add to Bottle" action Function(add_liquid_to_selected, liquid) style "inventory_button" text_size 12 padding (5,2) sensitive (selected_container["current_amount"] < selected_container["capacity"])

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
                                 if not container_inventory:
                                      text "- None -" size 14 color "#AAAAAA"
                                 for container in container_inventory:
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
                                 textbutton "Drain 10ml" action Function(drain_liquid, selected_container) style "inventory_button" sensitive (selected_container["current_amount"] > 0)
                                 textbutton "Pour Into..." action Show("liquid_pour_target_screen", source_container=selected_container) style "inventory_button" sensitive (selected_container["current_amount"] > 0)
                                 if len(selected_container["contents"]) >= 2:
                                     textbutton "Mix Contents" action [Function(reset_stirring), Show("stirring_minigame")] style "inventory_button"

                         else:
                             text "Select a container from the list." xalign 0.5 yalign 0.5 color "#AAAAAA"

            null height 10
            textbutton "Close Liquids" action [SetVariable("selected_container", None), Hide("liquids")] style "inventory_button" xalign 0.5

# --- Liquid Pour Target Screen ---
screen liquid_pour_target_screen(source_container):
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
                     if not container_inventory:
                         text "- No other containers -" size 14 color "#AAAAAA"
                     for target_container in container_inventory:
                         if target_container != source_container:
                             $ available_space = target_container["capacity"] - target_container["current_amount"]
                             textbutton f"{target_container['name']} ({available_space} ml space)" action [Function(pour_liquid, source_container, target_container), Hide("liquid_pour_target_screen")] style "inventory_button" sensitive (available_space > 0)

             null height 10
             textbutton "Cancel" action Hide("liquid_pour_target_screen") style "inventory_button"


# --- Stirring Minigame Screen ---
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
                    textbutton tool action SetVariable("stirring_tool", tool) style "inventory_button" sensitive (has_stirring_tool(tool))

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


# --- --- --- CHARACTER STATUS --- --- ---

screen character_status_screen():
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
                textbutton "Emotions" action SetVariable("selected_tab", "Emotions") style "inventory_button" sensitive (selected_tab != "Emotions")

            null height 15

            # --- Body Status Tab ---
            if selected_tab == "Body":
                python:
                    avg_health, avg_clean, avg_temp = calculate_averages()
                text f"Overall: Health {avg_health}% | Cleanliness {avg_clean}% | Temp {avg_temp}°" size 18 xalign 0.5 color "#CCCCCC"

                viewport:
                    ysize 500
                    scrollbars "vertical" mousewheel True
                    grid 2 3:
                        spacing 15

                        for part, status_dict in default_status.items():
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

                                    textbutton "Treat" action Show("medkit_screen", target_part=part) style "inventory_button" text_size 12 padding(5,2)

            # --- Stats Tab ---
            elif selected_tab == "Stats":
                 viewport:
                     ysize 500
                     scrollbars "vertical" mousewheel True
                     vbox:
                         spacing 15
                         for stat_name, data in stats.items():
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
                                         # FIX: Apply size directly to add
                                         add stat_img_path xysize (50, 50)
                                     else:
                                         frame style "stat_icon" background "#444444":
                                             xysize(50, 50) # Apply size to frame
                                             text stat_name[0].upper() size 30 xalign 0.5 yalign 0.5

                                     vbox:
                                         spacing 2
                                         text stat_name.title() size 18 color "#FFFF88"
                                         text f"Level: {data.get('level', 0)}" size 14
                                         text f"Value: {data.get('current_value', 0)}" size 14
                                         text "XP:" size 14
                                         bar value data.get('current_xp', 0) range data.get('max_xp', 100) xsize 200

                 if "sanity" in stats:
                      frame:
                          style "section_frame"
                          background "#2E4F2E"
                          padding (10, 10, 10, 10)
                          hbox:
                                spacing 10
                                python:
                                    sanity_img_path = "images/stats_icons/sanity.png"
                                if renpy.loadable(sanity_img_path):
                                     # FIX: Apply size directly to add
                                    add sanity_img_path xysize (50, 50)
                                else:
                                    frame style "stat_icon" background "#444444":
                                        xysize (50, 50) # Apply size to frame
                                        text "S" size 30 xalign 0.5 yalign 0.5

                                vbox:
                                    text f"Sanity: {stats['sanity'].get('current_sanity', 100)}%" size 18 color "#CCCCCC"
                                    bar value stats['sanity'].get('current_sanity', 100) range 100 xsize 250 left_bar "#AA00FF" right_bar "#330055"


            # --- Emotions Tab ---
            elif selected_tab == "Emotions":
                 python:
                      top_emotions, other_emotions = get_top_emotions(emotions)
                 hbox:
                     spacing 20
                     vbox:
                          text "Dominant Emotions" size 20 color "#FFFFFF"
                          if not top_emotions:
                              text "- None -" size 14 color "#AAAAAA"
                          for name, data in top_emotions:
                              frame:
                                   style "section_frame"
                                   background "#3E5F3E" padding (8, 8, 8, 8)
                                   vbox:
                                       text f"{name}: {data['value']}" size 16 color "#FFFF88"
                                       text "Bonuses:" size 12
                                       if not data['bonus']:
                                           text "- None -" size 10 color "#AAAAAA"
                                       for bonus_stat, bonus_val in data['bonus'].items():
                                            text f"- {bonus_stat.title()}: {bonus_val:+} " size 10 color "#CCFFCC"

                     vbox:
                          text "Other Emotions" size 18 color "#CCCCCC"
                          viewport:
                              ysize 400
                              scrollbars "vertical"
                              mousewheel True
                          vbox:
                              spacing 5
                              if not other_emotions:
                                   text "- None -" size 14 color "#AAAAAA"
                              for name, data in other_emotions:
                                  frame:
                                      style "section_frame"
                                      background "#2E4F2E" padding (5, 5, 5, 5)
                                      vbox:
                                          text f"{name}: {data['value']}" size 14 color "#DDDDDD"
                                          python:
                                              reduced = get_reduced_bonuses(data['bonus'])
                                          if reduced:
                                              text "Effects (Reduced):" size 9 color "#AAAAAA"
                                              for bonus_stat, bonus_val in reduced.items():
                                                  text f"- {bonus_stat.title()}: {bonus_val:+}" size 9 color "#AAAAAA"


            null height 15
            textbutton "Close Status" action Hide("status") style "inventory_button" xalign 0.5


# --- Medkit Screen ---
screen medkit_screen(target_part=None):
    modal True
    tag medkit

    frame:
        style "section_frame"
        xysize (600, 500)
        xalign 0.5 yalign 0.5

        vbox:
            spacing 10
            text "Medkit" size 25 color "#FFFFFF" xalign 0.5
            if target_part:
                 text f"(Treating: {target_part.replace('_',' ').title()})" size 16 color "#CCCCCC" xalign 0.5

            viewport:
                ysize 350
                scrollbars "vertical" mousewheel True
                vbox:
                     spacing 8
                     if not medkit_contents:
                          text "Medkit is empty." color "#AAAAAA" xalign 0.5
                     else:
                          for item_name, info in medkit_contents.items():
                              frame:
                                   style "section_frame"
                                   background "#2E4F2E" padding (8, 8, 8, 8)
                                   hbox:
                                       spacing 15
                                       vbox:
                                           text item_name.title() size 16 color "#DDDDDD"
                                           text f"Heals: {', '.join(info.get('conditions', ['Health']))}" size 12 color "#AAAAFF"
                                           text f"Potency: {info.get('healing', 0)}" size 12 color "#AAAAFF"

                                       if target_part:
                                            textbutton f"Use on {target_part.replace('_',' ').title()}" action [Function(use_medkit_item, target_part, item_name), Hide("medkit")] style "inventory_button"
                                       else:
                                            text "Select part from Status screen" size 12 color "#AAAAAA"


            null height 15
            textbutton "Close Medkit" action Hide("medkit") style "inventory_button" xalign 0.5
