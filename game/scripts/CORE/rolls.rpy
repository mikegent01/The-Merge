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
            
            textbutton "Close" action Hide("roll_history_screen") xalign 0.5 text_color "#FFFFFF" text_hover_color "#FFFF00"  
