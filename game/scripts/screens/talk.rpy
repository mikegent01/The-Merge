screen speakpeople():

    if last_label == "intreactivesection01" or test_room == 0:
        imagebutton:
            idle "images/inventory/inventory_hud/speechbubble.png"
            hover "images/inventory/inventory_hud/speechbubble_hover.png"
            focus_mask True
            xpos 350 ypos 350 # Placeholder: Adjust to front seat person's position
            action [Hide("speak_to_people"), Jump("FrontSeat")]
            tooltip "Talk to person in front"

        # Talk to the person in the back seat
        imagebutton:
            idle "images/inventory/inventory_hud/speechbubble.png"
            hover "images/inventory/inventory_hud/speechbubble_hover.png"
            focus_mask True
            xpos 10 ypos 350 # Placeholder: Adjust to back seat person's position
            action [Hide("speak_to_people"), Jump("BackSeat")]
            tooltip "Talk to person in back"
 

    else:
        # Fallback for other labels or if no specific UI is defined for "talk"
        frame:
            xalign 0.5 yalign 0.5 padding (20, 20)
            vbox:
                spacing 10
                text "Who do you want to talk to?"
                # Add generic talk options or just a close button if not appli ble
                textbutton "Close" action Hide("speak_to_people")
