screen dynamic_text_screen():
    modal True # Prevents interaction with underlying screens, good for this mode

    if last_label == "start":
        # --- Clickable icons for "look" actions ---
        # Note: Adjust xpos, ypos, and icon paths as needed.

        # Look at the projector (on table)
        imagebutton:
            idle "images/inventory/inventory_hud/magna.png"
            hover "images/inventory/inventory_hud/magna_hover.png"
            focus_mask True
            xpos 300 ypos 200 # Placeholder: Adjust to projector's position
            action [Hide("dynamic_text_screen"), Show("north_search_dialogue")]
            tooltip "Look at the projector"

        # Look at the exit door
        imagebutton:
            idle "images/inventory/inventory_hud/magna.png"
            hover "images/inventory/inventory_hud/magna_hover.png"
            focus_mask True
            xpos 700 ypos 500 # Placeholder: Adjust to door's position
            action [Hide("dynamic_text_screen"), Show("south_search_dialogue")]
            tooltip "Look at the exit door"

        # Look at the people sitting down
        imagebutton:
            idle "images/inventory/inventory_hud/magna.png"
            hover "images/inventory/inventory_hud/magna_hover.png"
            focus_mask True
            xpos 900 ypos 300 # Placeholder: Adjust to people's position
            action [Hide("dynamic_text_screen"), Show("east_search_dialogue")]
            tooltip "Look at the people"

        # Look at the wall
        imagebutton:
            idle "images/inventory/inventory_hud/magna.png"
            hover "images/inventory/inventory_hud/magna_hover.png"
            focus_mask True
            xpos 100 ypos 300 # Placeholder: Adjust to wall's position
            action [Hide("dynamic_text_screen"), Show("west_search_dialogue")]
            tooltip "Look at the wall"

        # Look at the ceiling projector
        imagebutton:
            idle "images/inventory/inventory_hud/magna.png"
            hover "images/inventory/inventory_hud/magna_hover.png"
            focus_mask True
            xpos 500 ypos 50 # Placeholder: Adjust to ceiling projector's position
            action [Hide("dynamic_text_screen"), Show("center_search_dialogue")]
            tooltip "Look at the ceiling projector"

        textbutton "Cancel Look Mode" action Hide("dynamic_text_screen") xalign 0.5 yalign 0.95

    elif last_label == "home_scene": # Example of how other labels would work (original structure)
        frame:
            xalign 0.5 yalign 0.5 padding (20, 20)
            vbox:
                spacing 10
                text "You're back at home. It's quiet and peaceful."
                hbox:
                    spacing 15
                    textbutton "Kitchen" action [Hide("dynamic_text_screen"), Show("kitchen_dialogue")]
                    textbutton "Bedroom" action [Hide("dynamic_text_screen"), Show("bedroom_dialogue")]
                    textbutton "Living Room" action [Hide("dynamic_text_screen"), Show("living_room_dialogue")]
                textbutton "Close" action Hide("dynamic_text_screen")

    elif last_label == "park_scene": # Example
        frame:
            xalign 0.5 yalign 0.5 padding (20, 20)
            vbox:
                spacing 10
                text "You're at the park. Birds are chirping in the distance."
                hbox:
                    spacing 15
                    textbutton "Pond" action [Hide("dynamic_text_screen"), Show("pond_dialogue")]
                    textbutton "Playground" action [Hide("dynamic_text_screen"), Show("playground_dialogue")]
                    textbutton "Path" action [Hide("dynamic_text_screen"), Show("path_dialogue")]
                textbutton "Close" action Hide("dynamic_text_screen")
    else:
        # Fallback for other labels or if no specific UI is defined for "look"
        frame:
            xalign 0.5 yalign 0.5 padding (20, 20)
            vbox:
                text "You look around."
                textbutton "Close" action Hide("dynamic_text_screen")

# North search dialogue
screen north_search_dialogue():
    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)
        
        vbox:
            spacing 10
            if last_label == "bootcampinsideprojectorroomstart":
                text "There is a desk with the projector on it.There is also a speakng podium with a lamp and microphone.Talking into the microphone would be a bad idea."
                textbutton "Return" action [Hide("north_search_dialogue"), Show("dynamic_text_screen")]

# South search dialogue
screen south_search_dialogue():
    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)
        
        vbox:
            spacing 10
            text "There is the exit door.outside the door is a wall.It smells pretty bad"
            textbutton "Return" action [Hide("south_search_dialogue"), Show("dynamic_text_screen")]

# East search dialogue
screen east_search_dialogue():
    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)
        
        vbox:
            spacing 10
            text "There are two people sitting down.talking to them might be a good idea. The one in the front is wearing an orange t-shirt and has a ottoman turban on his head.The one in the back has a paper mache in the shape of a moon on his head and is wearing a bag"
            textbutton "Return" action [Hide("east_search_dialogue"), Show("dynamic_text_screen")]

# West search dialogue
screen west_search_dialogue():
    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)
        
        vbox:
            spacing 10
            text "I found nothing just an empty wall.It smells rather bad maybe I should clean it."
            if has_item("Tissue") and not "clean_window" == True:
                textbutton "Clean Window" action [Hide("west_search_dialogue"), Show("clean_window_dialogue")]
            else:
                text "Maybe i can find something in this room.."
            textbutton "Return" action [Hide("west_search_dialogue"), Show("dynamic_text_screen")]

# Center search dialogue
screen center_search_dialogue():
    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)
        
        vbox:
            spacing 10
            text "There is a more modern projector on the ceiling. Why are we not using that projector?"
            if not has_item("Tissue"):
                text "There is a wet Tissue hanging down from the projector. It looks like someone used this paper to blow their nose during the meeting.I pick it up"
                $ inventory.append("Tissue")    
            textbutton "Return" action [Hide("center_search_dialogue"), Show("dynamic_text_screen")]


# Additional dialogue for clean window
screen clean_window_dialogue():
    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)
        
        vbox:
            spacing 10
            text "I wipe away years of dust and grime from the wall.It helps calm my nerves"
            textbutton "Return" action [Hide("clean_window_dialogue"), Show("dynamic_text_screen"),SetVariable("clean_window", True)]