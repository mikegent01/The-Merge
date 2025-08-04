screen dynamic_text_screen():
    if last_label == "intreactivesection01" or test_room == 0:
        $ projectorx = 650
        $ seatx = 274
        $ podiumx = 1005
        $ rajmanx = 441
        if abs(benx - 80) <= projectorx :
            imagebutton:
                idle "images/inventory/inventory_hud/magna.png"
                hover "images/inventory/inventory_hud/magna_hover.png"
                focus_mask True
                xpos projectorx ypos 300 
                action [Hide("dynamic_text_screen"), Show("projector_look_s2")]      
        if abs(benx - 80) <= 78 :
            imagebutton:
                idle "images/inventory/inventory_hud/magna.png"
                hover "images/inventory/inventory_hud/magna_hover.png"
                focus_mask True
                xpos 78 ypos 516
                action [Hide("dynamic_text_screen"), Show("bagman_look_s1")]                
        if abs(benx - 80) <= 1132 :
            imagebutton:
                idle "images/inventory/inventory_hud/magna.png"
                hover "images/inventory/inventory_hud/magna_hover.png"
                focus_mask True
                xpos 1132 ypos 429
                action [Hide("dynamic_text_screen"), Show("projector_look_s1")]                  
        if abs(benx - 80) <= podiumx :
            imagebutton:
                idle "images/inventory/inventory_hud/magna.png"
                hover "images/inventory/inventory_hud/magna_hover.png"
                focus_mask True
                xpos podiumx ypos 505 
                action [Hide("dynamic_text_screen"), Show("podium_look_s1")]
        if abs(benx - 80) <= seatx :
            imagebutton:
                idle "images/inventory/inventory_hud/magna.png"
                hover "images/inventory/inventory_hud/magna_hover.png"
                focus_mask True
                xpos seatx ypos 526 
                action [Hide("dynamic_text_screen"), Show("seat_look_s1")]

        if abs(benx - 80) <= 932:
            imagebutton:
                idle "images/inventory/inventory_hud/magna.png"
                hover "images/inventory/inventory_hud/magna_hover.png"
                focus_mask True
                xpos 932 ypos 487
                action [Hide("dynamic_text_screen"), Show("wire_look_s1")]                
        if abs(benx - 80) <= rajmanx :
            imagebutton:
                idle "images/inventory/inventory_hud/magna.png"
                hover "images/inventory/inventory_hud/magna_hover.png"
                focus_mask True
                xpos rajmanx ypos 508
                action [Hide("dynamic_text_screen"), Show("rajman_look_intreactivesection01")]                

    else:
        frame:
            xalign 0.5 yalign 0.5 padding (20, 20)
            vbox:
                text "I look around."
                textbutton "Close" action Hide("checkKey")

screen projector_look_s2():
    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)
        
        vbox:
            spacing 10
            text "I look at the projector screen thinking about the presentation that just played, it is hard to belive that a portal can destroy a whole town..."
            textbutton "Return" action [Hide("projector_look_s2"), Show("checkKey")]

screen seat_look_s1():
    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)
        
        vbox:
            spacing 10
            if not game_state["chapter_1"]["projector_room"]["picked_tissue_up"]:
                text "There is a tissue on my seat, it must have fell out of my pocket. I pick up the tissue"
                textbutton "Pick Up" action [Function(player.inventory.add_item, "Tissue"), SetDict(game_state["chapter_1"]["projector_room"], "picked_tissue_up", True), Hide("seat_look_s1"), Jump("intreactivesection01")]
            else:
                text "There is nothing here..."
                textbutton "Return" action [Hide("seat_look_s1"), Show("checkKey")]

screen podium_look_s1():
    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)
        
        vbox:
            spacing 10
            text "Looking at the podium, I think of something in that position."
            textbutton "Return" action [Hide("podium_look_s1"), Show("checkKey")]

screen rajman_look_intreactivesection01():
    python:
        if 'rajman_intel_success' not in game_state["rolls"]["roll_results"]:
            roll_result = player.perform_roll(skill_name='perception', base_chance=40)
            game_state["rolls"]["roll_results"]['rajman_intel_success'] = roll_result

    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)

        vbox:
            spacing 10
            text "I look at the man the things I notice most about him his is turban, he is wearing an ottoman style turban possibly for religious reasons but i am not sure."
            $ rajman_roll = game_state["rolls"]["roll_results"].get('rajman_intel_success', {})
            if rajman_roll.get('success', False):
                text "I however do notice that he is hiding something, he is looking at his pocket at something smoking"
                text f"Intelligence Roll Passed: {rajman_roll.get('roll', 0)} >= {rajman_roll.get('threshold', 0)}" size 18 color "#00FF00"
            else:
                text f"Intelligence Roll Failed: {rajman_roll.get('roll', 0)} < {rajman_roll.get('threshold', 0)}" size 18 color "#FF0000"
            textbutton "Return" action [Hide("rajman_look_intreactivesection01"), Show("checkKey")]

screen projector_look_s1():
    python:
        if 'projector_success' not in game_state["rolls"]["roll_results"]:
            roll_result = player.perform_roll(skill_name='perception', base_chance=20)
            game_state["rolls"]["roll_results"]['projector_success'] = roll_result

    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)

        vbox:
            spacing 10
            text "The Drill Sargent is standing there he is wearing a standard issue uniform and a blue hat with the words MP on it. There appears to be dust on his hat. I don't feel like talking to him as it seems like a bad idea."
            $ projector_roll = game_state["rolls"]["roll_results"].get('projector_success', {})
            if projector_roll.get('success', False):
                text "I also notice the drill Sargent has a scar on his left arm, he seems to be covering it up with his uniform deliberately"
                text f"Intelligence Roll Passed: {projector_roll.get('roll', 0)} >= {projector_roll.get('threshold', 0)}" size 18 color "#00FF00"
            else:
                text f"Intelligence Roll Failed: {projector_roll.get('roll', 0)} < {projector_roll.get('threshold', 0)}" size 18 color "#FF0000"
            textbutton "Return" action [Hide("projector_look_s1"), Show("checkKey")]

screen bagman_look_s1():
    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)

        vbox:
            spacing 10
            text "There is a man with a bag on his head.... I will call him bagman from now on"
            textbutton "Return" action [Hide("bagman_look_s1"), Show("checkKey")]

screen wire_look_s1():
    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)

        vbox:
            spacing 10
            text "The wire is unplugged, it connects the projector screen to the wall"
            textbutton "Return" action [Hide("wire_look_s1"), Show("checkKey")]
screen roll_history_screen():
    frame:
        xalign 0.5 yalign 0.3  # Moved up to avoid bottom HUD overlap
        xsize 800 ysize 500  # Reduced height slightly to minimize overlap
        padding (20, 20)
        background "#333333cc"  # Semi-transparent dark background for better visibility and color
        
        vbox:
            spacing 10
            
            text "Roll History" size 24 xalign 0.5 color "#FFFFFF"  # White title for contrast
            
            viewport id "roll_viewport":
                ysize 350  # Fixed height for scrollable area (scroll with mousewheel or drag)
                mousewheel True
                draggable True
                
                vbox:
                    spacing 5
                    if len(roll_queue) == 0:
                        text "No rolls yet." color "#888888"
                    else:
                        for idx, roll_data in enumerate(roll_queue):
                            frame:
                                background "#222222"  # Dark gray background for each roll entry
                                padding (10, 10)
                                xfill True
                                
                                vbox:
                                    text f"Roll #{idx + 1}: {roll_data['skill'].capitalize()}" bold True color "#FFFF00"  # Yellow for roll title
                                    if roll_data['proficiency']:
                                        text f"Proficiency: {roll_data['proficiency'].capitalize()}" color "#CCCCCC"  # Light gray
                                    text f"Roll: {roll_data['roll']} (Threshold: {roll_data['threshold']}, Chance: {roll_data['total_chance']}%)" color "#FFFFFF"  # White for details
                                    if roll_data['success']:
                                        text "Success!" color "#00FF00" bold True  # Green for success, bold
                                    else:
                                        text "Failure." color "#FF0000" bold True  # Red for failure, bold
                                    if roll_data['emotion_bonuses']:
                                        text "Emotion Bonuses:" color "#00FFFF"  # Cyan header
                                        for emo, bonus in roll_data['emotion_bonuses']:
                                            text f"- {emo.capitalize()}: +{bonus}" color "#FFFFFF"  # White for bonuses
            
            textbutton "Close" action Hide("roll_history_screen") xalign 0.5 text_color "#FFFFFF" text_hover_color "#FFFF00"  # Colored button at bottom
screen roll_history_screen():
    frame:
        xalign 0.5 yalign 0.3  # Moved up to avoid bottom HUD overlap
        xsize 800 ysize 500  # Reduced height slightly to minimize overlap
        padding (20, 20)
        background "#333333cc"  # Semi-transparent dark background for better visibility and color
        
        vbox:
            spacing 10
            
            text "Roll History" size 24 xalign 0.5 color "#FFFFFF"  # White title for contrast
            
            viewport id "roll_viewport":
                ysize 350  # Fixed height for scrollable area (scroll with mousewheel or drag)
                mousewheel True
                draggable True
                
                vbox:
                    spacing 5
                    if len(roll_queue) == 0:
                        text "No rolls yet." color "#888888"
                    else:
                        for idx, roll_data in enumerate(roll_queue):
                            frame:
                                background "#222222"  # Dark gray background for each roll entry
                                padding (10, 10)
                                xfill True
                                
                                vbox:
                                    text f"Roll #{idx + 1}: {roll_data['skill'].capitalize()}" bold True color "#FFFF00"  # Yellow for roll title
                                    if roll_data['proficiency']:
                                        text f"Proficiency: {roll_data['proficiency'].capitalize()}" color "#CCCCCC"  # Light gray
                                    text f"Roll: {roll_data['roll']} (Threshold: {roll_data['threshold']}, Chance: {roll_data['total_chance']}%)" color "#FFFFFF"  # White for details
                                    if roll_data['success']:
                                        text "Success!" color "#00FF00" bold True  # Green for success, bold
                                    else:
                                        text "Failure." color "#FF0000" bold True  # Red for failure, bold
                                    if roll_data['emotion_bonuses']:
                                        text "Emotion Bonuses:" color "#00FFFF"  # Cyan header
                                        for emo, bonus in roll_data['emotion_bonuses']:
                                            text f"- {emo.capitalize()}: +{bonus}" color "#FFFFFF"  # White for bonuses
            
            textbutton "Close" action Hide("roll_history_screen") xalign 0.5 text_color "#FFFFFF" text_hover_color "#FFFF00"  # Colored button at bottom