screen dynamic_text_screen():
    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)
       
        vbox:
            spacing 10
           
            if last_label == "bootcampinsideprojectorroomstart":
                text "I am inside of a projector room. I can perform a search on the area to the north, south, east, west, and center. Which area should I search?"
                
                # Adding direction buttons for the projector room
                hbox:
                    spacing 15
                    textbutton "North" action [Hide("dynamic_text_screen"), Show("north_search_dialogue")]
                    textbutton "South" action [Hide("dynamic_text_screen"), Show("south_search_dialogue")]
                    textbutton "East" action [Hide("dynamic_text_screen"), Show("east_search_dialogue")]
                    textbutton "West" action [Hide("dynamic_text_screen"), Show("west_search_dialogue")]
                    textbutton "Center" action [Hide("dynamic_text_screen"), Show("center_search_dialogue")]
                
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
                text "There is a desk with the projector on it... There is also a speakng podium with a lamp and microphone..."
                text "Talking into the microphone would be a bad idea...."
            #    textbutton "Take Lens" action [Hide("north_search_dialogue"), SetVariable("has_lens", True), Show("dynamic_text_screen")]
                textbutton "Return" action [Hide("north_search_dialogue"), Show("dynamic_text_screen")]

# South search dialogue
screen south_search_dialogue():
    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)
        
        vbox:
            spacing 10
            text "There is the exit door...outside the door is a wall....."
            text "It smells pretty bad....."
         #   textbutton "Flip Switch" action [Hide("south_search_dialogue"), SetVariable("lights_on", True), Show("dynamic_text_screen")]
            textbutton "Return" action [Hide("south_search_dialogue"), Show("dynamic_text_screen")]

# East search dialogue
screen east_search_dialogue():
    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)
        
        vbox:
            spacing 10
            text "There are two people sitting down...talking to them might be a good idea"
            text "The one in the front is wearing a orange t-shirt and has a ottoman turban on his head."
            text "The one in the back has a paper mache in the shape of a moon on his head and is wearing a bag"
            text "Expect clowns when you come to a circus "
         #   textbutton "Examine Reels" action [Hide("east_search_dialogue"), Show("reels_dialogue")]
            textbutton "Return" action [Hide("east_search_dialogue"), Show("dynamic_text_screen")]

# West search dialogue
screen west_search_dialogue():
    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)
        
        vbox:
            spacing 10
            text "I found nothing just an empty wall..."
            text "It smells rather bad maybe I should clean it."
            if has_item("tissue"):
                textbutton "Clean Window" action [Hide("west_search_dialogue"), SetVariable("window_clean", True), Show("clean_window_dialogue")]
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
            text "There is a more modern projector on the ceiling... Why are we not using that projector?"
            text "....!"
            if not has_item("tissue"):
                text "There is a wet tissue someone used to blow there nose during the meeting...I pick it up"
                $ inventory.append("tissue")    
            textbutton "Return" action [Hide("center_search_dialogue"), Show("dynamic_text_screen")]


# Additional dialogue for clean window
screen clean_window_dialogue():
    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)
        
        vbox:
            spacing 10
            text "I wipe away years of dust and grime from the wall..."
            text "It helps calm my nerves."
            textbutton "Return" action [Hide("clean_window_dialogue"), Show("dynamic_text_screen")]