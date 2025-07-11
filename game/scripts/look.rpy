screen dynamic_text_screen():
    modal True # Prevents interaction with underlying screens, good for this mode
    #intreactivesection01
    if last_label == "intreactivesection01" or test_room == 0:
        $ projectorx = 650
        $ seatx = 190
        if abs(benx - 80) <= projectorx or abs(benx + 80) <= projectorx:
            imagebutton:
                idle "images/inventory/inventory_hud/magna.png"
                hover "images/inventory/inventory_hud/magna_hover.png"
                focus_mask True
                xpos 650 ypos 300 
                action [Hide("dynamic_text_screen"), Show("projector_look_s1")]
                tooltip "Look at the people"
        if abs(benx - 80) <= seatx or abs(benx + 80) <= seatx and not has_item("tissue"):
            imagebutton:
                idle "images/inventory/inventory_hud/magna.png"
                hover "images/inventory/inventory_hud/magna_hover.png"
                focus_mask True
                xpos 264 ypos 563 
                action [Hide("dynamic_text_screen"), Show("seat_look_s1")]
                tooltip "Look at the people"
                
        textbutton "Cancel Look Mode" action Hide("dynamic_text_screen") xalign 0.5 yalign 0.95

    else:
        frame:
            xalign 0.5 yalign 0.5 padding (20, 20)
            vbox:
                text "You look around."
                textbutton "Close" action Hide("dynamic_text_screen")

screen projector_look_s1():
    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)
        
        vbox:
            spacing 10
            text "I look at the projector screen thinking about the presentation that just played, it is hard to belive that a portal can destroy a whole town like that..."
            textbutton "Return" action [Hide("projector_look_s1"), Show("dynamic_text_screen")]
screen seat_look_s1():
    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)
        
        vbox:
            spacing 10
            text "There is a tissue on my seat, it must have fell out of my pocket. I pick up the tissue"
            textbutton "Return" action [Hide("projector_look_s1"), Show("dynamic_text_screen")]