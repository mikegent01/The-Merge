style transparent_button:
    background None  # No background
    hover_background None  # No background on hover
    padding (10, 5)  # Padding for better clickability
    xalign 0.5  # Center align
    color "#09ff80"  # White text color
    hover_color "#4CAF50"  # Green text color on hover
    outlines []  # Remove any text outlines

style inventory_button:
    background "#1E4A1E"  # Dark green background for buttons
    hover_background "#728477"  # Light green hover effect
    padding (10, 10)
    color "#FFFFFF"  # White text
    xalign 0.5 

screen slot_selection():
    modal True
    frame:
        xsize 400
        ysize 300
        xalign 0.5
        yalign 0.5
        background "#1E4A1E"
        padding (20, 20)

        vbox:
            spacing 10
            text "Select a Slot to Equip [selected_item]" size 25 xalign 0.5 color "#FFFFFF"

            # Only show slots that are valid for the selected item
            if items[selected_item]["type"] == "weapon":
                textbutton "Left Hand" action [Function(equip_item, selected_item, "left_hand"), Hide("slot_selection")] style "inventory_button"
                textbutton "Right Hand" action [Function(equip_item, selected_item, "right_hand"), Hide("slot_selection")] style "inventory_button"
            elif items[selected_item]["type"] == "tool":
                textbutton "Left Hand" action [Function(equip_item, selected_item, "left_hand"), Hide("slot_selection")] style "inventory_button"
                textbutton "Right Hand" action [Function(equip_item, selected_item, "right_hand"), Hide("slot_selection")] style "inventory_button"
            elif items[selected_item]["type"] == "consumable":
                textbutton "Body" action [Function(equip_item, selected_item, "body"), Hide("slot_selection")] style "inventory_button"

            textbutton "Cancel" action Hide("slot_selection") style "inventory_button"

screen inventory():
    modal True    

    frame:
        xsize 1200
        ysize 5000
        background "#1E4A1E"  # Dark green background for the entire screen
        padding (20, 20)

        viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"  # Enable vertical scrollbars

            hbox:
                spacing 20

                # Left Side: Inventory Slots
                frame:
                    background "#113111"  # Darker green background for the inventory section
                    xsize 600
                    ysize 760
                    padding (10, 10)

                    vbox:
                        spacing 10
                        text "Inventory Slots" size 30 xalign 0.5 color "#FFFFFF"
                        text "Remaining Slots: [get_remaining_space()]" size 20 xalign 0.5 color "#FFFFFF"
                        
                        viewport:  # Add a viewport for the inventory slots
                            draggable True
                            mousewheel True
                            scrollbars "vertical"  # Enable vertical scrollbars
                            xsize 580  # Adjust width to fit within the frame
                            ysize 600  # Adjust height to limit the scrollable area

                            grid 4 get_remaining_space():  
                                spacing 10
                                for i in range(get_remaining_space()): 
                                    frame:
                                        background "#728477"  # Light green background for each slot
                                        xsize 120
                                        ysize 120
                                        padding (10, 10)

                                        if i < len(inventory):
                                            $ item = inventory[i]
                                            if renpy.loadable("images/inventory/" + item + ".png"):
                                                add "images/inventory/" + item + ".png" xalign 0.5 yalign 0.5 xsize 100 ysize 100
                                            else:
                                                text item xalign 0.5 yalign 0.5 color "#FFFFFF"

                                            # Click to select the item
                                            textbutton "" action SetVariable("selected_item", item) style "transparent_button":
                                                xfill True
                                                yfill True
                                        else:
                                            text "Empty" xalign 0.5 yalign 0.5 color "#FFFFFF"

                # Right Side: Selected Item Info and Equipped Slots
                frame:
                    background "#113111"  # Darker green background for the right section
                    xsize 560
                    ysize 760
                    padding (10, 10)

                    vbox:
                        spacing 10

                        # Selected Item Info
                        if selected_item:
                            text "Selected Item" size 30 xalign 0.5 color "#FFFFFF"
                            frame:
                                background "#728477"  # Light green background for the selected item info
                                padding (10, 10)
                                vbox:
                                    spacing 10
                                    if renpy.loadable("images/inventory/" + selected_item + ".png"):
                                        add "images/inventory/" + selected_item + ".png" xalign 0.5 yalign 0.5 xsize 200 ysize 200
                                    else:
                                        text "No image available" xalign 0.5 yalign 0.5 color "#FFFFFF"

                                    text "Name: [selected_item]" size 18 color "#FFFFFF"
                                    text "Weight: [get_item_weight(selected_item)] kg" size 18 color "#FFFFFF"
                                    text "Description: [get_item_description(selected_item)]" size 18 color "#FFFFFF"

                                    # Equip and Discard buttons for the selected item
                                    textbutton "Equip" action Show("slot_selection") style "inventory_button"
                                    textbutton "Discard" action Function(remove_item, selected_item) style "inventory_button"
                                    textbutton "Close" action SetVariable("selected_item", None) style "inventory_button"
                        # Equipped Slots (Formatted like a body)
                        if not selected_item:  # Only show equipped items if no item is selected
                            viewport:  # Add a viewport for the equipped items section
                                draggable True
                                mousewheel True
                                scrollbars "vertical"  # Enable vertical scrollbars
                                xsize 740  # Adjust width to fit within the frame
                                ysize 500  # Adjust height to limit the scrollable area

                                vbox:
                                    spacing 10
                                    text "Equipped Items" size 30 xalign 0.5 color "#FFFFFF"

                                    # Head Slot
                                    frame:
                                        background "#728477"  # Light green background for the slot
                                        xsize 150
                                        ysize 150
                                        xalign 0.5

                                        if head_item:
                                            if renpy.loadable("images/inventory/" + head_item + ".png"):
                                                add "images/inventory/" + head_item + ".png" xalign 0.5 yalign 0.5 xsize 100 ysize 100
                                            else:
                                                text head_item xalign 0.5 yalign 0.5 color "#FFFFFF"
                                        else:
                                            text "Empty" xalign 0.5 yalign 0.5 color "#FFFFFF"

                                        if head_item:
                                            hbox:
                                                textbutton "Use" action Function(use_item, head_item) style "inventory_button"
                                                textbutton "Unequip" action Function(unequip_item, "head") style "inventory_button" 

                                    # Left Hand, Body, and Right Hand Slots
                                    hbox:
                                        xalign 0.5

                                        # Left Hand Slot
                                        frame:
                                            background "#728477"  # Light green background for the slot
                                            xsize 150
                                            ysize 150

                                            if left_hand_item:
                                                if renpy.loadable("images/inventory/" + left_hand_item + ".png"):
                                                    add "images/inventory/" + left_hand_item + ".png" xalign 0.5 yalign 0.5 xsize 100 ysize 100
                                                else:
                                                    text left_hand_item xalign 0.5 yalign 0.5 color "#FFFFFF"
                                            else:
                                                text "Empty" xalign 0.5 yalign 0.5 color "#FFFFFF"

                                            if left_hand_item:
                                                hbox:
                                                    textbutton "Use" action Function(use_item, left_hand_item) style "inventory_button"
                                                    textbutton "Unequip" action Function(unequip_item, "left_hand") style "inventory_button"

                                        # Body Slot
                                        frame:
                                            background "#728477"  # Light green background for the slot
                                            xsize 150
                                            ysize 150

                                            if body_item:
                                                if renpy.loadable("images/inventory/" + body_item + ".png"):
                                                    add "images/inventory/" + body_item + ".png" xalign 0.5 yalign 0.5 xsize 100 ysize 100
                                                else:
                                                    text body_item xalign 0.5 yalign 0.5 color "#FFFFFF"
                                            else:
                                                text "Empty" xalign 0.5 yalign 0.5 color "#FFFFFF"

                                            if body_item:
                                                hbox:
                                                    textbutton "Use" action Function(use_item, body_item) style "inventory_button"
                                                    textbutton "Unequip" action Function(unequip_item, "body") style "inventory_button"

                                        # Right Hand Slot
                                        frame:
                                            background "#728477"  # Light green background for the slot
                                            xsize 150
                                            ysize 150

                                            if right_hand_item:
                                                if renpy.loadable("images/inventory/" + right_hand_item + ".png"):
                                                    add "images/inventory/" + right_hand_item + ".png" xalign 0.5 yalign 0.5 xsize 100 ysize 100
                                                else:
                                                    text right_hand_item xalign 0.5 yalign 0.5 color "#FFFFFF"
                                            else:
                                                text "Empty" xalign 0.5 yalign 0.5 color "#FFFFFF"

                                            if right_hand_item:
                                                hbox:
                                                    textbutton "Use" action Function(use_item, right_hand_item) style "inventory_button"
                                                    textbutton "Unequip" action Function(unequip_item, "right_hand") style "inventory_button"

                                    # Left and Right Leg Slots
                                    hbox:
                                        xalign 0.5

                                        # Left Leg Slot
                                        frame:
                                            background "#728477"  # Light green background for the slot
                                            xsize 150
                                            ysize 150

                                            if left_leg_item:
                                                if renpy.loadable("images/inventory/" + left_leg_item + ".png"):
                                                    add "images/inventory/" + left_leg_item + ".png" xalign 0.5 yalign 0.5 xsize 100 ysize 100
                                                else:
                                                    text left_leg_item xalign 0.5 yalign 0.5 color "#FFFFFF"
                                            else:
                                                text "Empty" xalign 0.5 yalign 0.5 color "#FFFFFF"

                                            if left_leg_item:
                                                hbox:
                                                    textbutton "Use" action Function(use_item, left_leg_item) style "inventory_button"
                                                    textbutton "Unequip" action Function(unequip_item, "left_leg") style "inventory_button"

                                        # Right Leg Slot
                                        frame:
                                            background "#728477"  # Light green background for the slot
                                            xsize 150
                                            ysize 150
                                            padding (10, 10)

                                            if right_leg_item:
                                                if renpy.loadable("images/inventory/" + right_leg_item + ".png"):
                                                    add "images/inventory/" + right_leg_item + ".png" xalign 0.5 yalign 0.5 xsize 100 ysize 100
                                                else:
                                                    text right_leg_item xalign 0.5 yalign 0.5 color "#FFFFFF"
                                            else:
                                                text "Empty" xalign 0.5 yalign 0.5 color "#FFFFFF"

                                            if right_leg_item:
                                                hbox:
                                                    spacing 10
                                                    textbutton "Equip" action Show("slot_selection") style "inventory_button"
                                                    textbutton "Unequip" action Function(unequip_item, "right_leg") style "inventory_button"

                        # Additional Actions
                        hbox:
                            spacing 20
                            if inventory:
                                textbutton "Create Items" action Show("crafting_screen") style "inventory_button"
                            textbutton "Create Liquids" action Show("combine_liquids_screen") style "inventory_button"
                            textbutton "View Containers" action Show("liquid_management_screen") style "inventory_button"
                        textbutton "Close" action Hide("inventory") style "inventory_button"
screen item_select(arm):
    modal True
    frame:
        xsize 600
        ysize 500
        xalign 0.5
        yalign 0.5
        background "#07391a"
        padding (20, 20)

        vbox:
            spacing 10
            text "Select an Item" size 25 xalign 0.5 color "#FFFFFF"

            viewport:
                mousewheel True
                scrollbars "vertical"
                vbox:
                    spacing 10
                    for item in inventory:
                        frame:
                            background "#1E4A1E"
                            padding (10, 10)
                            hbox:
                                if renpy.loadable("images/inventory/" + item + ".png"):
                                    add "images/inventory/" + item + ".png" size (50, 50)
                                else:
                                    text item size 18 color "#FFFFFF"

                                textbutton "Equip" action Function(equip_item, arm, item) style "inventory_button"
                                textbutton "Use" action Function(use_item, item) style "inventory_button"
                                textbutton "Info" action Show("item_info", item=item) style "inventory_button"

            textbutton "Cancel" action Hide("item_select") style "inventory_button" xalign 0.5

screen crafting_screen():
    modal True
    frame:
        xsize 800
        ysize 600
        xalign 0.5
        yalign 0.5
        background "#113111"
        padding (20, 20)

        vbox:
            spacing 10
            label "Item Inspection" text_size 30 text_color "#FFFFFF"

            hbox:
                spacing 20
                textbutton "Construction" action SetVariable("current_mode", "construction") style "inventory_button"
                textbutton "Destruction" action SetVariable("current_mode", "destruction") style "inventory_button"

            viewport:
                draggable True
                mousewheel True
                scrollbars "vertical"
                xsize 760
                ysize 400

                vbox:
                    spacing 10
                    if current_mode == "construction":
                        label "Available Items" text_size 24 text_color "#FFFFFF"
                        for item in inventory:
                            if item not in selected_items:
                                frame:
                                    background "#1E4A1E"
                                    padding (10, 10)
                                    hbox:
                                        if renpy.loadable("images/inventory/" + item + ".png"):
                                            add "images/inventory/" + item + ".png" size (50, 50)
                                        else:
                                            text item size 18 color "#FFFFFF"

                                        textbutton "Select" action [SetVariable("selected_item", item), Function(select_item, item)] style "inventory_button"

                        label "Selected Items" text_size 24 text_color "#FFFFFF"
                        for selected_item in selected_items:
                            frame:
                                background "#1E4A1E"
                                padding (10, 10)
                                hbox:
                                    if renpy.loadable("images/inventory/" + selected_item + ".png"):
                                        add "images/inventory/" + selected_item + ".png" size (50, 50)
                                    else:
                                        text selected_item size 18 color "#FFFFFF"

                                    textbutton "Remove" action [SetVariable("selected_item", selected_item), Function(remove_item, selected_item)] style "inventory_button"

                        if len(selected_items) == 2:
                            textbutton "Combine" action [Function(combine_items), Show("crafting_screen")] style "inventory_button"
                        else:
                            text "Select 2 items to combine." size 18 color "#FFFFFF"

                    elif current_mode == "destruction":
                        label "Available Items" text_size 24 text_color "#FFFFFF"
                        for item in inventory:
                            frame:
                                background "#1E4A1E"
                                padding (10, 10)
                                hbox:
                                    if renpy.loadable("images/inventory/" + item + ".png"):
                                        add "images/inventory/" + item + ".png" size (50, 50)
                                    else:
                                        text item size 18 color "#FFFFFF"

                                    textbutton "Deconstruct" action [SetVariable("selected_item", item), Function(deconstruct_item, item)] style "inventory_button"

            textbutton "Cancel" action Hide("crafting_screen") style "inventory_button" xalign 0.5

screen liquid_management_screen():
    modal True
    frame:
        xsize 800
        ysize 600
        xalign 0.5
        yalign 0.5
        background "#113111"
        padding (20, 20)

        vbox:
            spacing 10
            label "Liquid Management" text_size 30 text_color "#FFFFFF"

            for liquid in liquid_inventory:
                if liquid["amount"] > 0:
                    frame:
                        background "#1E4A1E"
                        padding (10, 10)
                        hbox:
                            text f"{liquid['name']}: {liquid['amount']} ml" size 18 color "#FFFFFF"
                            bar value liquid['amount'] range 118 xsize 400

            textbutton "Close" action Hide("liquid_management_screen") style "inventory_button" xalign 0.5

screen combine_liquids_screen():
    modal True
    frame:
        xsize 1000
        ysize 600
        xalign 0.5
        yalign 0.5
        background "#1B3D1B"
        padding (20, 20)

        hbox:
            spacing 20

            # Left Side: Bottles List
            vbox:
                spacing 10
                text "Bottles" size 24 color "#FFFFFF"
                for container in container_inventory:
                    frame:
                        background "#2A4A2A"
                        padding (10, 10)
                        vbox:
                            text f"{container['name']}" size 18 color "#FFFFFF"
                            text f"{container['current_amount']}/{container['capacity']} ml" size 16 color "#FFFFFF"
                            if selected_container != container:
                                textbutton "Select" action SetVariable("selected_container", container) style "inventory_button"
                            else:
                                text "✔ Selected" size 18 color "#4CAF50"

            # Middle: Selected Bottle Details
            if selected_container:
                vbox:
                    spacing 10
                    text "Selected Bottle" size 24 color "#FFFFFF"
                    text f"{selected_container['name']}" size 18 color "#FFFFFF"
                    text f"Capacity: {selected_container['capacity']} ml" size 16 color "#FFFFFF"
                    bar:
                        value selected_container["current_amount"]
                        range selected_container["capacity"]
                        xsize 400
                        left_bar "#4CAF50"
                        right_bar "#2A4A2A"

                    # Contents of the Selected Bottle
                    text "Contents:" size 18 color "#FFFFFF"
                    for content in selected_container["contents"]:
                        text f"{content['name']}: {content['amount']} ml" size 16 color "#FFFFFF"

                    # Drain Button
                    textbutton "Drain 10 ml" action Function(drain_liquid, selected_container) style "inventory_button"

            # Right Side: Liquids and Pour Options (Scrollable)
            if selected_container:
                viewport:
                    mousewheel True
                    scrollbars "vertical"
                    xsize 300
                    ysize 500
                    vbox:
                        spacing 10
                        text "Liquids" size 24 color "#FFFFFF"
                        for liquid in liquid_inventory:
                            if liquid["amount"] > 0:
                                frame:
                                    background "#2F523F"
                                    padding (10, 10)
                                    vbox:
                                        text f"{liquid['name']} - {liquid['amount']} ml available" size 18 color "#FFFFFF"
                                        textbutton "Add to Bottle" action Function(add_liquid_to_selected, liquid) style "inventory_button"

                        # Pour Options
                        text "Pour Into:" size 24 color "#FFFFFF"
                        for container in container_inventory:
                            if container != selected_container:
                                frame:
                                    background "#2A4A2A"
                                    padding (10, 10)
                                    vbox:
                                        text f"{container['name']}" size 18 color "#FFFFFF"
                                        textbutton "Pour Here" action Function(pour_liquid, selected_container, container) style "inventory_button"

                        # Pour to Ground Option
                        frame:
                            background "#2A4A2A"
                            padding (10, 10)
                            vbox:
                                text "Ground" size 18 color "#FFFFFF"
                                textbutton "Pour Here" action Function(pour_liquid, selected_container, None) style "inventory_button"

        # Mix Button
        if selected_container and len(selected_container["contents"]) >= 2:
            textbutton "Mix" action Show("stirring_minigame") style "inventory_button" xalign 0.5

        # Cancel Button
        textbutton "Cancel" action Hide("combine_liquids_screen") style "inventory_button" xalign 0.9
screen stirring_minigame():
    modal True
    frame:
        xsize 600
        ysize 600
        xalign 0.5
        yalign 0.5
        background "#1B3D1B"
        padding (20, 20)

        vbox:
            spacing 10
            text "Stir the Liquids" size 24 color "#FFFFFF" xalign 0.5

            # Stirring Tool Selection
            text "Select a Stirring Tool:" size 18 color "#FFFFFF" xalign 0.5
            hbox:
                spacing 20
                xalign 0.5
                for tool in ["Spoon", "Stick", "Whisk"]:
                    if has_stirring_tool(tool):
                        textbutton tool:
                            action SetVariable("stirring_tool", tool)
                            style "inventory_button"
                    else:
                        textbutton tool:
                            action None
                            style "inventory_button"
                            sensitive False  # Disable if the tool is not in inventory

            # Stirring Area
            if stirring_tool:
                text f"Using: {stirring_tool}" size 18 color "#FFFFFF" xalign 0.5
                text "Stir in a circular motion with your mouse." size 16 color "#FFFFFF" xalign 0.5

                # Stirring Progress Bar
                bar:
                    value stirring_progress
                    range 100
                    xsize 400
                    left_bar "#4CAF50"
                    right_bar "#2A4A2A"
                    xalign 0.5

                # Stirring Interaction
                if not stirring_complete:
                    timer 0.1 repeat True action Function(update_stirring_progress)
                    text "Stirring Progress: [stirring_progress]%" size 18 color "#FFFFFF" xalign 0.5
                else:
                    text "Stirring Complete!" size 18 color "#4CAF50" xalign 0.5

            # Cancel Button
            textbutton "Cancel" action [Hide("stirring_minigame"), Function(reset_stirring)] style "inventory_button" xalign 0.5
screen input_amount_screen(liquid):
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
            input:
                id "amount_input"
                default ""
                length 5
                allow "0123456789"
                color "#FFFFFF"
                size 20

            hbox:
                spacing 20
                textbutton "Add":
                    action [
                        Function(add_liquid_to_selected, liquid, int(amount_input.value or 0)),
                        Hide("input_amount_screen")
                    ]
                textbutton "Cancel":
                    action Hide("input_amount_screen")
screen input_amount_screen(liquid):
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
            input:
                id "amount_input"
                default ""
                length 5
                allow "0123456789"
                color "#FFFFFF"
                size 20

            hbox:
                spacing 20
                textbutton "Add":
                    action [
                        Function(add_liquid_to_selected, liquid, int(amount_input.value or 0)),
                        Hide("input_amount_screen")
                    ]
                textbutton "Cancel":
                    action Hide("input_amount_screen")
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