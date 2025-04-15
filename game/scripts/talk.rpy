

screen projector_room_people():
    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)
        
        vbox:
            spacing 10
            text "There are three people in the projector room. I have talked to the drill sargent. Who else should i talk to?"
            
            textbutton "Talk to the person in the front seat" action [Hide("projector_room_people"), Jump("FrontSeat")]
            textbutton "Talk to the person in the back seat" action [Hide("projector_room_people"), Jump("BackSeat")]
            textbutton "Return" action Hide("projector_room_people")
