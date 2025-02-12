
screen status_screen():
    modal True
    frame:
        xsize 800
        ysize 600
        xalign 0.5
        yalign 0.5
        background "#111111"

        vbox:
            spacing 20
            text "My Health Overview" size 40 xalign 0.5 color "#FFFFFF" bold True

            # Calculate averages
            $ average_health, average_cleanliness, average_temperature = calculate_averages()

            $ medical_level = stats["medical"]["level"]
            $ can_view_health = is_stat_higher("medical", 100, stats)
            $ can_view_health_small = is_stat_higher("medical", 59, stats)
            $ can_view_hygiene = is_stat_higher("intelligence", 50, stats)

            # Body Parts Status
            for part in ["head", "body", "left_arm", "right_arm", "left_leg", "right_leg"]:
                frame:
                    background "#222222"
                    padding (10, 10)
                    hbox:
                        spacing 20
                        text part.replace("_", " ").capitalize() + ":" size 24 color "#FFFFFF"
                        if not can_view_health:
                            textbutton "View Status" action Show("condition_details", part=part) style "inventory_button"
                        if can_view_health:
                            bar value default_status[part]["health"] range 100 xmaximum 400 ymaximum 25
                            textbutton "View Status" action Show("condition_details", part=part) style "inventory_button"
            textbutton "Cancel" action Hide("status_screen") style "inventory_button" xalign 0.5
            frame:
                background "#222222"
                padding (10, 10)
                vbox:
                    spacing 10
                    text "Averages" size 30 xalign 0.5 color "#FFFFFF" bold True

                    if can_view_health_small:
                        text "Estimated Average Health: [average_health]%" size 24 color "#FFFFFF"
                        bar value average_health range 100 xmaximum 400 ymaximum 25

                        text "Average Cleanliness: [average_cleanliness]%" size 24 color "#FFFFFF"
                        bar value average_cleanliness range 100 xmaximum 400 ymaximum 25

                    if has_item("thermometer"):
                        text "Average Temperature: [average_temperature]°F" size 24 color "#FFFFFF"
                        bar value average_temperature range 100 xmaximum 400 ymaximum 25

            # Close Button
            textbutton "Close" action Hide("status_screen") style "inventory_button" xalign 0.5
screen player_stats_screen():
    modal True
    frame:
        xsize 1000
        ysize 800
        xalign 0.5
        background "#111111"

        vbox:
            spacing 20
            text "Player Stats" size 40 xalign 0.5 color "#FFFFFF" bold True

            # Toggle Buttons for Categories
            hbox:
                spacing 20
                xalign 0.5
                textbutton "Mental" action [SetVariable("selected_category", "soft")] style "category_button"
                textbutton "Physical" action [SetVariable("selected_category", "hard")] style "category_button"
                textbutton "Emotions" action [SetVariable("selected_category", "emotions")] style "category_button"
                textbutton "Relationships" action [SetVariable("selected_category", "relationships")] style "category_button"
                textbutton "Close" action Hide("player_stats_screen") style "inventory_button"

            # Stats Section
            viewport:
                draggable True
                mousewheel True
                xsize 950
                ysize 600

                vbox:
                    spacing 20
                    if selected_category == "soft" or selected_category == "hard":
                        for stat in stats:
                            if (selected_category == "soft" and stat in soft_skills) or (selected_category == "hard" and stat in hard_skills):
                                frame:
                                    background "#222222"
                                    padding (15, 10)
                                    hbox:
                                        spacing 20
                                        vbox:
                                            spacing 10
                                            text stat.replace("_", " ").capitalize() size 30 color "#00CCFF" bold True
                                            text "Level: [stats[stat]['level']]" size 20 color "#CCCCCC"
                                            bar value stats[stat]["level"] range stats[stat]['max_xp'] xmaximum 600 ymaximum 25
                                            text "Skill: [stats[stat]['current_value']]" size 20 color "#CCCCCC"
                                            bar value stats[stat]["current_value"] range stats[stat]["max_xp"] xmaximum 600 ymaximum 25
                                            text "XP: [stats[stat]['current_xp']] / [stats[stat]['max_xp']]" size 20 color "#CCCCCC"
                                            bar value stats[stat]["current_xp"] range stats[stat]["max_xp"] xmaximum 600 ymaximum 25

                                            if stats[stat]["current_xp"] >= stats[stat]["max_xp"]:
                                                textbutton "Level Up!" action Function(level_up, stat) style "level_up_button"

                                        # Icon Section
                                        frame:
                                            background None
                                            xsize 210
                                            ysize 607
                                            vbox:
                                                xalign 0.5
                                                yalign 0.5
                                                $ icon_path = "images/stats_icons/{}.png".format(stat)
                                                if renpy.exists(icon_path):
                                                    add icon_path xsize 210 ysize 607
                                                else:
                                                    text "[stat.capitalize()] Icon" size 15 color "#CCCCCC"

                    elif selected_category == "emotions":
                        # Get the top 3 emotions and the rest
                        $ top_emotions, other_emotions = get_top_emotions(emotions)

                        # Get the top emotion and its bonuses
                        $ top_emotion, top_bonuses = get_top_emotion_bonuses(emotions)

                        # Display the top emotion and its bonuses
                        text "Main Emotion" size 30 xalign 0.5 color "#FFFFFF" bold True
                        if top_emotion:
                            frame:
                                background "#2f612f"
                                padding (15, 10)
                                vbox:
                                    spacing 10
                                    text top_emotion.capitalize() size 24 color "#ffeb34" bold True
                                    bar value emotions[top_emotion]["value"] range 100 xmaximum 600 ymaximum 25

                                    # Display bonuses
                                    text "Bonuses:" size 20 color "#FFFFFF" bold True
                                    for stat, bonus in top_bonuses.items():
                                        hbox:
                                            spacing 10
                                            text stat.replace("_", " ").capitalize() size 18 color "#CCCCCC"
                                            if bonus > 0:
                                                text f"+{bonus}" size 18 color "#00FF00" 
                                            else:
                                                text f"{bonus}" size 18 color "#FF0000"
                        # Display the remaining top emotions
                        text "Minor Emotions" size 30 xalign 0.5 color "#FFFFFF" bold True
                        for emotion, data in top_emotions[1:]:
                            frame:
                                background "#132a16"
                                padding (15, 10)
                                vbox:
                                    
                                    spacing 10
                                    text emotion.capitalize() size 24  bold True 
                                    bar value data["value"] range 100 xmaximum 600 ymaximum 25

                                    # Get reduced bonuses for the emotion
                                    $ reduced_bonuses = get_reduced_bonuses(data["bonus"])
                        
                                    # Display reduced bonuses
                                    text "Bonuses:" size 20 color "#FFFFFF" bold True
                                    for stat, bonus in reduced_bonuses.items():
                                        hbox:
                                            spacing 10
                                            text stat.replace("_", " ").capitalize() size 18 color "#CCCCCC"
                                            if bonus > 0:
                                                text f"+{bonus}" size 18 color "#2aba2a"
                                            else:
                                                text f"{bonus}" size 18 color "#FF0000"
                        
                        # Display the remaining emotions
                        text "Other Emotions" size 30 xalign 0.5 color "#FFFFFF" bold True
                        for emotion, data in other_emotions:
                            frame:
                                background "#222222"
                                padding (15, 10)
                                hbox:
                                    spacing 20
                                    text emotion.capitalize() size 24 color "#FF66CC" bold True
                                    bar value data["value"] range 100 xmaximum 600 ymaximum 25

                    elif selected_category == "relationships":
                        for person in relationships:
                            if relationships[person]["met"]:
                                frame:
                                    background "#222222"
                                    padding (15, 10)
                                    vbox:
                                        spacing 10
                                        text person.capitalize() size 30 color "#66FF66" bold True

                                        # Get relationship description
                                        $ trust = relationships[person]["trust"]
                                        $ friendship = relationships[person]["friendship"]
                                        $ hostility = relationships[person]["hostility"]
                                        $ relationship_description = get_relationship_description(trust, friendship, hostility)
                                        text relationship_description size 24 color "#CCCCCC"

                                        # Relationship bars
                                        hbox:
                                            text "Trust:" size 20 color "#CCCCCC"
                                            bar value trust range 100 xmaximum 600 ymaximum 25
                                        hbox:
                                            text "Friendship:" size 20 color "#CCCCCC"
                                            bar value friendship range 100 xmaximum 600 ymaximum 25
                                        hbox:
                                            text "Hostility:" size 20 color "#CCCCCC"
                                            bar value hostility range 100 xmaximum 600 ymaximum 25

            # Close Button
            textbutton "Close":
                action Hide("player_stats_screen")
                xalign 0.5
                yalign 1.0
                style "inventory_button"
screen heal_menu():
    modal True
    frame:
        xsize 500
        ysize 400
        xalign 0.5
        yalign 0.5
        background "#111111"

        vbox:
            spacing 20
            text "Select a Body Part to Heal" size 30 xalign 0.5 color "#FFFFFF" bold True

            for part in ["head", "body", "left_arm", "right_arm", "left_leg", "right_leg"]:
                textbutton part.replace("_", " ").capitalize() action [Show("medkit_item_menu", part=part)] style "inventory_button"

            textbutton "Cancel" action Hide("heal_menu") style "inventory_button" xalign 0.5
screen condition_details(part):
    modal True
    frame:
        xsize 800
        ysize 600
        xalign 0.5
        yalign 0.5
        background "#111111"

        vbox:
            spacing 20
            text part.replace("_", " ").capitalize() + " Status" size 40 xalign 0.5 color "#FFFFFF" bold True
            $ medical_level = stats["medical"]["level"]
            $ can_view_health = is_stat_higher("medical", 100, stats)
            $ can_view_health_small = is_stat_higher("medical", 59, stats)
            $ can_view_hygiene = is_stat_higher("intelligence", 50, stats)


            # Health Status
            $ health = default_status[part]['health']
            if health > 90:
                text "My "  + part.replace("_", " ") +  " Feels Great!" size 24 xalign 0.5 color "#00FF00"
            elif health > 75:
                text "My " + part.replace("_", " ") + " Feels Good!" size 24 xalign 0.5 color "#32CD32"
            elif health > 50:
                text "My "  + part.replace("_", " ") + " Feels Fine." size 24 xalign 0.5 color "#FFD700"
            elif health > 25:
                text "It Hurts!" size 24 xalign 0.5 color "#FFA500"
            elif health > 10:
                text "It Fucking Hurts!" size 24 xalign 0.5 color "#FF0000"
            else:
                text "At Death's Door..." size 24 xalign 0.5 color "#FF0000"

            # Health Bar
            if can_view_health:
                bar value default_status[part]["health"] range 100 xmaximum 600 ymaximum 25 xalign 0.5

            # Conditions
            if can_view_health_small:
                text "Conditions:" size 30 xalign 0.5 color "#FFFFFF" bold True
                if default_status[part]["conditions"]:
                    for condition in default_status[part]["conditions"]:
                        text condition.capitalize() size 24 xalign 0.5 color "#CCCCCC"
                else:
                    text "No Current Conditions." size 24 xalign 0.5 color "#CCCCCC"
            $ cleanliness = default_status[part]['cleanliness']

            $ temp = default_status[part]['temperature']
            if can_view_health_small:
                text "Hygiene: [default_status[part]['cleanliness']]%" size 24 xalign 0.5 color "#FFFFFF"
                bar value default_status[part]["cleanliness"] range 100 xmaximum 600 ymaximum 25 xalign 0.5
            if not can_view_health_small:
                if cleanliness > 90:
                    text "My " + part.replace("_", " ") + " is very clean" size 18 xalign 0.5 color "#00ff008e"
                elif cleanliness > 75:
                    text "My " + part.replace("_", " ") + " is clean" size 18 xalign 0.5 color "#32CD32"
                elif cleanliness > 50:
                    text "My " + part.replace("_", " ") + " is somewhat clean." size 18 xalign 0.5 color "#FFD700"
                elif cleanliness > 25:
                    text "My " + part.replace("_", " ") + " is kind of dirty" size 18 xalign 0.5 color "#FFA500"
                elif cleanliness > 10:
                    text "My " + part.replace("_", " ") + " is filthy" size 18 xalign 0.5 color "#ff0000"
                else:
                    text "My " + part.replace("_", " ") + " is fucking disgusting" size 18 xalign 0.5 color "#FF0000"


            if has_item("thermometer"):
                text "Temperature: [default_status[part]['temperature']]°F" size 24 xalign 0.5 color "#FFFFFF"
                bar value default_status[part]["temperature"] range 100 xmaximum 600 ymaximum 25 xalign 0.5
            else:
                if temp < 30:
                    text "My " + part.replace("_", " ") + " is Freezing Cold!" size 18 xalign 0.5 color "#00FFFF"
                elif temp < 45:
                    text "My " + part.replace("_", " ") + " is Very Cold!" size 18 xalign 0.5 color "#00BFFF"
                elif temp < 65:
                    text "My " + part.replace("_", " ") + " is Cold!" size 18 xalign 0.5 color "#1E90FF"
                elif temp < 75:
                    text "My " + part.replace("_", " ") + "'s temperature is fine." size 18 xalign 0.5 color "#32CD32"
                elif temp < 80:
                    text "My " + part.replace("_", " ") + " feels Warm." size 18 xalign 0.5 color "#FFD700"
                elif temp < 90:
                    text "My " + part.replace("_", " ") + " is too fucking hot!" size 18 xalign 0.5 color "#ff0000"
                else:
                    text "IT IS TOO FUCKING HOT!" size 18 xalign 0.5 color "#FF0000"

            # Medkit Button
            if has_item('medkit'):
                textbutton "Use Medkit" action [Show("medkit_item_menu", part=part)] style "inventory_button" xalign 0.5

            # Close Button
            textbutton "Close" action Hide("condition_details") style "inventory_button" xalign 0.5
screen medkit_item_menu(part):
    modal True
    frame:
        xsize 600
        ysize 500
        xalign 0.5
        yalign 0.5
        background "#111111"

        vbox:
            spacing 20
            text "Select an Item to Use" size 30 xalign 0.5 color "#FFFFFF" bold True

            # Scrollable Container
            viewport:
                draggable True
                mousewheel True
                ysize 350

                vbox:
                    spacing 10
                    for item, info in medkit_contents.items():
                        if is_stat_higher("medical", 40, stats):
                            textbutton f"{item.capitalize()} (Heals: {', '.join(info['conditions'])}, Health: +{info['healing']})" action [Function(use_medkit_item, part, item), Hide("medkit_item_menu")] style "inventory_button"
                        else:
                            textbutton f"{item.capitalize()}" action [Function(use_medkit_item, part, item), Hide("medkit_item_menu")] style "inventory_button"

            # Close Button
            textbutton "Cancel" action Hide("medkit_item_menu") style "inventory_button" xalign 0.5