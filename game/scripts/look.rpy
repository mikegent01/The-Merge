screen dynamic_text_screen():
    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)
       
        vbox:
            spacing 10
           
            if last_label == "bootcampinsideprojectorroomstart":
                text "I am inside of a projector room."
                
                # Adding direction buttons for the projector room
                hbox:
                    spacing 15
                    textbutton "Look at the projector." action [Hide("dynamic_text_screen"), Show("north_search_dialogue")]
                    textbutton "Look at the exit door." action [Hide("dynamic_text_screen"), Show("south_search_dialogue")]
                    textbutton "Look at the people sitting down." action [Hide("dynamic_text_screen"), Show("east_search_dialogue")]
                    textbutton "Look at the wall" action [Hide("dynamic_text_screen"), Show("west_search_dialogue")]
                    textbutton "Look at the projector" action [Hide("dynamic_text_screen"), Show("center_search_dialogue")]
                
            elif last_label == "home_scene":
                text "You're back at home. It's quiet and peaceful."
                # Add home-specific options here
                hbox:
                    spacing 15
                    textbutton "Kitchen" action [Hide("dynamic_text_screen"), Show("kitchen_dialogue")]
                    textbutton "Bedroom" action [Hide("dynamic_text_screen"), Show("bedroom_dialogue")]
                    textbutton "Living Room" action [Hide("dynamic_text_screen"), Show("living_room_dialogue")]
                
            elif last_label == "park_scene":
                text "You're at the park. Birds are chirping in the distance."
                # Add park-specific options here
                hbox:
                    spacing 15
                    textbutton "Pond" action [Hide("dynamic_text_screen"), Show("pond_dialogue")]
                    textbutton "Playground" action [Hide("dynamic_text_screen"), Show("playground_dialogue")]
                    textbutton "Path" action [Hide("dynamic_text_screen"), Show("path_dialogue")]
                
            else:
                text "You're on your journey. Where to next?"
               
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