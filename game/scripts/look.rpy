screen dynamic_text_screen():
    modal True # Prevents interaction with underlying screens, good for this mode

    if last_label == "start" or test_room == 0:
        if abs(benx - 80) <= 600:
            imagebutton:
                idle "images/inventory/inventory_hud/magna.png"
                hover "images/inventory/inventory_hud/magna_hover.png"
                focus_mask True
                xpos 650 ypos 300 
                action [Hide("dynamic_text_screen"), Show("projector_look_s1")]
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
            text "I look at the projector screen thinking about the presentation that just played, it is hard to belive that a portal can destroy a whole town like that."
            textbutton "Return" action [Hide("projector_look_s1"), Show("dynamic_text_screen")]
