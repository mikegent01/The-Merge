screen inventory:
    modal True
    frame:
        xsize 400
        ysize 600
        xalign 0.5
        yalign 0.5
        background "#276127"

        vbox:
            text "My Inventory" size 30 xalign 0.5

            # Show current weight and remaining space
            $ current_weight = calculate_total_weight()
            $ remaining_space = get_remaining_space()
            text "Weight Of Carried Items: " + str(current_weight) + " kg"
            text "Remaning Space In Your Bag: " + str(remaining_space) + " N"
            text "Max Weight You Can Hold: " + str(current_strength) + " kg"
            # Left Arm Slot
            hbox:
                vbox:
                    text "Left Hand" size 18
                    frame:
                        background "#728477"
                        xsize 100
                        ysize 100
                        if left_arm_item:   
                            if renpy.loadable("images/inventory/" + left_arm_item + ".png"):
                                add "images/inventory/" + left_arm_item + ".png" xalign 0.5 yalign 0.5
                            else:
                                text left_arm_item xalign 0.5 yalign 0.5
                        else:
                            text "Empty" xalign 0.5 yalign 0.5


                    if not left_arm_item:
                        textbutton "Equip" action Show("item_select", arm="left")
                    else:
                        textbutton "Unequip" action Function(unequip_item, "left")
                        textbutton "Discard" action Function(discard_item, "left")
                        textbutton "Use" action Function(use_item, left_arm_item)

                # Right Arm Slot
                vbox:
                    text "Right Hand" size 18
                    frame:
                        background "#728477"
                        xsize 100
                        ysize 100
                        if right_arm_item:   
                            if renpy.loadable("images/inventory/" + right_arm_item + ".png"):
                                add "images/inventory/" + right_arm_item + ".png" xalign 0.5 yalign 0.5
                            else:
                                text right_arm_item xalign 0.5 yalign 0.5
                        else:
                            text "Empty" xalign 0.5 yalign 0.5



                    if not right_arm_item:
                        textbutton "Equip" action Show("item_select", arm="right")
                    else:
                        textbutton "Unequip" action Function(unequip_item, "right")
                        textbutton "Discard" action Function(discard_item, "right")
                        textbutton "Use" action Function(use_item, right_arm_item)

            # Add a section for body armor
            text "Body Armor" size 20 xalign 0.5
            if body_armor_item:  # Assuming you have a variable for body armor
                text "Equipped: " + body_armor_item xalign 0.5  # Indicate equipped body armor
            else:
                text "Equipped: None" xalign 0.5

            # Button to show the equipable armor screen
            textbutton "Equip Armor" action Show("equip_armor")
            if inventory:
                textbutton "Create Items" action Show("crafting_screen")
            if is_container_empty():              
                textbutton "Create Liquids" action Show("combine_liquids_screen")
                textbutton "View Containers" action Show("liquid_management_screen")
            textbutton "Close" action Hide("inventory"):
                xalign 1.0
                yalign 1.0
screen equip_armor():
    modal True
    frame:
        xsize 400
        ysize 400
        xalign 0.5
        yalign 0.5
        background "#113111"

        vbox:
            text "Equip Armor" size 30 xalign 0.5

            # Display currently equipped armor
            text "Current Armor I have Equipped: " + (body_armor_item if body_armor_item else "None") xalign 0.5

            # Scrollable item list for armor
            text "Armor I can Equip" size 20 xalign 0.5
            
            viewport:
                mousewheel True
                vbox:
                    for armor_item in armor_inventory:  # Iterate over each item in armor_inventory
                        if isinstance(armor_item, dict):  # Check if armor_item is a dictionary
                            # Start a frame for each armor item for better separation
                            frame:
                                xalign 0.5
                                background "#113111"        
                                vbox:
                                    $ armor_name = armor_item['name']  # Get the armor name
                                    $ armor_description = armor_item['description']  # Get the armor description
                                    $ armor_weight = armor_item['weight']  # Get the armor weight
                                    $ armor_durability = armor_item['durability']  # Get the armor durability

                                    # Prepare the image path, replacing spaces with underscores
                                    $ image_path = "images/inventory/" + armor_name.replace(" ", "_") + ".png"

                                    # Display armor image if it exists
                                    if renpy.loadable(image_path):
                                        add image_path xalign 0.5 yalign 0.5  # Add the image for the armor item
                                    else:
                                        text armor_name xalign 0.5 yalign 0.5  # Fallback to text if image not found

                                    # Display armor name and details
                                    text "Name: " + armor_name xalign 0.5  # Display armor name
                                    text "Weight: " + str(armor_weight) + " kg" xalign 0.5  # Display weight
                                    text "Durability: " + str(armor_durability) xalign 0.5  # Display durability
                                    text armor_description xalign 0.5  # Display description

                                    # Check if the armor is the currently equipped one
                                    if armor_name == body_armor_item:
                                        text "Equipped" xalign 0.5  # Display 'Equipped' if the armor is already equipped
                                    else:
                                        # If armor is broken (durability <= 0), show "Remove" button
                                        if armor_durability <= 0:
                                            text f"{armor_name} is damaged and cannot be equipped" xalign 0.5
                                        else:
                                            # Show the Equip button only if durability > 0
                                            textbutton "Equip" action Function(equip_item, "body", armor_name) xalign 0.5

                                    text ""  
                                    frame:  
                                        xsize 380  
                                        ysize 2  
                                        background "#174517"        

        # Close button in bottom-right corner
        textbutton "Close" action Hide("equip_armor"):
            xalign 1.0
            yalign 1.0
# Item info screen
screen item_info(item):
    modal True
    frame:
        xsize 400
        ysize 400
        xalign 0.5
        yalign 0.5
        background "#000000"
        
        vbox:
            text "Item Information" size 25 xalign 0.5
            
            if renpy.loadable("images/inventory/" + item + ".png"):
                # Display the item image centered
                add "images/inventory/" + item + ".png":
                    xalign 0.5
                    yalign 0.5
                    xsize 200
                    ysize 200
            else:
                text "No image available" xalign 0.5 yalign 0.5

            # Display item weight and description
            text "Weight: " + str(get_item_weight(item)) + " kg" xalign 0.5  # Assumes get_item_weight is defined
            text "Description: " + get_item_description(item) xalign 0.5  # Assumes get_item_description is defined
            
            # Add the buttons in a horizontal box (hbox)
            hbox:
                spacing 20  # Adjust the space between buttons
                
                # "Use" button
                textbutton "Use" action Function(use_item, item)

                # "Close" button
                textbutton "Close" action Hide("item_info")

# Item selection screen
screen item_select(arm):
    modal True
    frame:
        xsize 400
        ysize 400
        xalign 0.5
        yalign 0.5
        background "#07391a"
        
        vbox:
            text "Select an Item" size 25 xalign 0.5
            
            viewport:
                mousewheel True
                vbox:
                    for item in inventory:  # Assuming inventory is a list of items
                        hbox:
                            # Display item image if it exists
                            if renpy.loadable("images/inventory/" + item + ".png"):
                                add "images/inventory/" + item + ".png" size (50, 50)
                            else:
                                text item
                            
                            # Equip button
                            textbutton "Equip":
                                action Function(equip_item, arm, item)
                            
                            # Use button
                            textbutton "Use":
                                action Function(use_item, item)

                            # Info button to show item info
                            textbutton "Info":
                                action Show("item_info", item=item)
                            
            # Cancel button
            textbutton "Cancel" action Hide("item_select")

screen crafting_screen():
    frame:
        xalign 0.5
        yalign 0.5
        background "#113111"
        has vbox:
            label "Item Inspection" 

            # Mode Selection
            hbox:
                textbutton "Construction" action SetVariable("current_mode", "construction")
                textbutton "Destruction" action SetVariable("current_mode", "destruction")

            # Scrollable area for items
            viewport:
                draggable True
                mousewheel True
                # Set a size for the viewport to allow scrolling
                xsize 600
                ysize 400

                # Vertical box that contains the items
                vbox:
                    if current_mode == "construction":
                        # Available Items
                        label "Available Items"
                        for item in inventory:
                            if item not in selected_items:
                                if renpy.loadable("images/inventory/" + item + ".png"):
                                    add "images/inventory/" + item + ".png" size (50, 50)
                                    textbutton "Select" action [SetVariable("selected_item", item), Function(select_item, item)]
                                else:
                                    text item

                        # Divider
                        text " "

                        # Selected Items
                        label "Selected Items"
                        for selected_item in selected_items:
                            if renpy.loadable("images/inventory/" + selected_item + ".png"):
                                add "images/inventory/" + selected_item + ".png" size (50, 50)
                                textbutton "Remove" action [SetVariable("selected_item", selected_item), Function(remove_item, selected_item)]
                            else:
                                text selected_item

                        # Divider
                        text " "

                        # Holding Items
                        label "Cohesive Items"
                        if holding_items:
                            for holding_item in holding_items:
                                if holding_item in inventory:
                                    if renpy.loadable("images/inventory/" + holding_item + ".png"):
                                        add "images/inventory/" + holding_item + ".png" size (50, 50)
                                        # Show "Selected" if the holding item is already selected
                                        if holding_item == selected_holding_item:
                                            textbutton "Selected" action None  # No action when selected
                                        else:
                                            textbutton "Select " + holding_item action [SetVariable("selected_holding_item", holding_item)]

                                        # Only show "Remove" if the holding item is selected
                                        if holding_item == selected_holding_item:
                                            textbutton "Remove" action [Function(remove_holding_item, holding_item)]

                                    else:
                                        text holding_item 

                        # Combine Button
                        if len(selected_items) == 2:  # Require 2 items and a holding item
                            textbutton "Combine" action [Function(combine_items), Show("crafting_screen")]
                        else:
                            text ""
                            text "Select items to combine."

                    elif current_mode == "destruction":
                        label "Available Items"
                        for item in inventory:
                            if renpy.loadable("images/inventory/" + item + ".png"):
                                add "images/inventory/" + item + ".png" size (50, 50)
                                textbutton "Deconstruct " + item action [SetVariable("selected_item", item), Function(deconstruct_item, item)]
                            else:
                                text item

                        # Divider
                        text " "
                        text "Select an item to deconstruct."

            # Cancel Button
            textbutton "Cancel" action Hide("crafting_screen")

screen liquid_management_screen():
    frame:
        xalign 0.5  # Center the frame horizontally
        yalign 1.0  # Align the frame to the bottom of the screen
        background "#113111"
        has vbox:
            label "Liquid Management"

            # Loop through each liquid in the liquid_inventory
            for liquid in liquid_inventory:
                if liquid["amount"] > 0:  # Only show liquids that are available
                    hbox:
                        label f"{liquid['name']}:"  # Display the name of the liquid
                        text f"{liquid['amount']} ml"  # Display current amount
                        bar value liquid['amount'] range 118  # Horizontal bar representation

            textbutton "Close" action Hide("liquid_management_screen")  # Button to close the screen

screen combine_liquids_screen():
    frame:
        # Main container for the entire screen
        background "#113111"

        vbox:
            # Subheading for the screen
            text "Select a container and liquids to combine." style "subheading_text" align (0.5, 0.5)

            # ------------------- Containers Section -------------------
            label "Containers" style "category_title" align (0.5, 0.5)
            hbox:
                for container in container_inventory:
                    vbox:
                        text f"{container['name']} - {container['current_amount']}/{container['capacity']} ml  " style "container_text" 
                        # Conditional buttons for selecting containers
                        if selected_container != container:
                            textbutton "Select" action SetVariable("selected_container", container) style "container_button"
                        else:
                            text " ✔ Selected" style "selected_text"  # Indicate selection
                    # Add space between containers

            # ------------------- Available Liquids Section -------------------
            label "Available Liquids" style "subheading_text" align (0.5, 0.5)
            hbox:
                for liquid in liquid_inventory:
                    if liquid["amount"] > 0:
                        vbox:
                            text f"{liquid['name']} - {liquid['amount']} ml available  " style "liquid_text"
                            if liquid in selected_liquids:
                                text " ✔ Selected to be added to container" style "added_text"  # Indicate already added
                            else:
                                textbutton "Add to container" action [Function(add_liquid_to_selected, liquid)] style "add_button"
                        # Add space between liquids
                    #    spacing 10

            # ------------------- Selected Container and Liquids Section -------------------
            if selected_container:
                label "Selected Container" style "subheading_text" align (0.5, 0.5)
                hbox:
                    text f"{selected_container['name']} - {selected_container['current_amount']}/{selected_container['capacity']} ml  " style "selected_container_text" align (0.5, 0.5)

                label "Contents Inside Container:" style "subheading_text" align (0.5, 0.5)
                hbox:
                    for content in selected_container["contents"]:
                        vbox:
                            text f"{content['name']} - {content['amount']} ml  " style "content_text"
                            textbutton "Drain 10 ml" action [Function(drain_liquid, selected_container, content["name"])] style "drain_button"
                        # Add space between contents


                # ------------------- Selected Liquids to Add Section -------------------
                label "Selected Liquids to Add:" style "subheading_text" align (0.5, 0.5)
                hbox:
                    for liquid in selected_liquids:
                        text f"{liquid['name']} - {liquid['amount']} ml " style "selected_liquid_text"
                        # Add space between selected liquids

            # ------------------- Combine and Mix Buttons -------------------
            if selected_container:
                hbox:
                    if selected_liquids:
                        textbutton "Add to container." action [Function(combine_liquids, selected_container, selected_liquids)] style "combine_button"
                    else:
                        text "\n"
                        if check_mix_recipe(selected_container):
                            textbutton "Mix" action [Function(combine_liquids, selected_container, selected_liquids)] style "combine_button"
                        else:
                            text "This mixture would not make anything of note..." style "error_text" align (0.5, 0.5)
                        
            else:
                text "\n"
                text "Please select a container and some liquids." style "error_text" align (0.5, 0.5)

            # ------------------- Cancel Button -------------------
            textbutton "Cancel" action Hide("combine_liquids_screen") style "cancel_button"


screen use_liquid_screen():
    frame:
        vbox:
            label "Use Liquid"
            text "Select a liquid to use:"
            
            # Iterate through the inventory to display only liquids
            for liquid in inventory:
                if liquid["type"] == "liquid":  # Ensure we are only displaying liquids
                    text f"{liquid['name']} - {liquid['amount']}ml available"
                    textbutton "Use" action [Function(use_liquid, liquid), Hide("use_liquid_screen")]

            # Cancel button
        #    textbutton "Cancel" action Hide("use_liquid_screen")