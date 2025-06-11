screen speak_to_people():
    modal True # Prevents interaction with underlying screens

    if last_label == "start":
        # --- Clickable icons for "talk" actions ---
        # Note: Adjust xpos, ypos, and icon paths as needed.

        # Talk to the person in the front seat
        imagebutton:
            idle "images/inventory/inventory_hud/speechbubble.png"
            hover "images/inventory/inventory_hud/speechbubble_hover.png"
            focus_mask True
            xpos 850 ypos 250 # Placeholder: Adjust to front seat person's position
            action [Hide("speak_to_people"), Jump("FrontSeat")]
            tooltip "Talk to person in front"

        # Talk to the person in the back seat
        imagebutton:
            idle "images/inventory/inventory_hud/speechbubble.png"
            hover "images/inventory/inventory_hud/speechbubble_hover.png"
            focus_mask True
            xpos 850 ypos 350 # Placeholder: Adjust to back seat person's position
            action [Hide("speak_to_people"), Jump("BackSeat")]
            tooltip "Talk to person in back"

        textbutton "Cancel Talk Mode" action Hide("speak_to_people") xalign 0.5 yalign 0.95

    else:
        # Fallback for other labels or if no specific UI is defined for "talk"
        frame:
            xalign 0.5 yalign 0.5 padding (20, 20)
            vbox:
                spacing 10
                text "Who do you want to talk to?"
                # Add generic talk options or just a close button if not applicable
                textbutton "Close" action Hide("speak_to_people")
