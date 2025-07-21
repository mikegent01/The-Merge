
screen status_screen(player_obj):
    modal True
    frame:
        xsize 800
        ysize 800
        xalign 0.5
        yalign 0.5
        background "#0A0A0A"
        style "rounded_frame"

        vbox:
            spacing 15

            fixed:
                xsize 800
                ysize 450
                add "images/stats_icons/full_body_diagram.png" xalign 0.5 yalign 0.5

                button:  # Left Leg (top left 593 407, bottom right 610 452)
                    xpos 340 ypos 370
                    xsize (630 - 593) ysize (452 - 407)
                    action Show("condition_details", player_obj=player_obj, part="left_leg")
                    tooltip "Click to view Left Leg details"
                button:  # Right Leg (top left 680 427, bottom right 702 451)
                    xpos 430 ypos 370
                    xsize (630 - 593) ysize (452 - 407)
                    action Show("condition_details", player_obj=player_obj, part="right_leg")
                    tooltip "Click to view Right Leg details"
                button:  # Body (top left 607 278, bottom right 699 365)
                    xpos 357 ypos 228
                    xsize (710 - 607) ysize (395 - 278)
                    action Show("condition_details", player_obj=player_obj, part="body")
                    tooltip "Click to view Body details"
                button:  # Right Arm (top right 601 300, bottom left 574 373 → bounding box adjusted)
                    xpos 330 ypos 255
                    xsize (601 - 574) ysize (383 - 300)
                    action Show("condition_details", player_obj=player_obj, part="left_arm")
                    tooltip "Click to view Right Arm details"
                button:  # Left Arm (top right 693 276, bottom left 723 365 → bounding box adjusted)
                    xpos 453 ypos 240
                    xsize (723 - 693) ysize (365 - 276)
                    action Show("condition_details", player_obj=player_obj, part="right_arm")
                    tooltip "Click to view Left Arm details"
                button:  # Head (bottom left 609 270, top right 706 182 → bounding box adjusted)
                    xpos 339 ypos 140
                    xsize (736 - 609) ysize (270 - 182)
                    action Show("condition_details", player_obj=player_obj, part="head")
                    tooltip "Click to view Head details"

            if player_obj.is_stat_higher("mental_resilience", 50):
                text "Sanity Level" size 30 xalign 0.5 color "#FFFFFF" bold True
                $ sanity = player_obj.stats.get("sanity", {}).get("current_sanity", 50)
                bar value sanity range 100 xmaximum 400 ymaximum 20 style "health_bar" xalign 0.5

            $ average_health, average_cleanliness, average_temperature = player_obj.calculate_averages()
            $ can_view_health = player_obj.is_stat_higher("medical", 100)
            $ can_view_health_small = player_obj.is_stat_higher("medical", 59)
            $ has_thermometer = player_obj.inventory.has_item("thermometer")

            frame:
                vbox:
                    spacing 10
                    text "Averages" size 30 xalign 0.5 color "#FFFFFF" bold True
                    if can_view_health_small:
                        text f"Est. Avg Health: {average_health}%" size 24 color "#FFFFFF"
                        bar value average_health range 100 xmaximum 400 ymaximum 20 style "health_bar" bar_invert (average_health < 50)
                    if can_view_health:
                        text f"Avg Cleanliness: {average_cleanliness}%" size 24 color "#FFFFFF"
                        bar value average_cleanliness range 100 xmaximum 400 ymaximum 20 style "clean_bar"
                    if has_thermometer or can_view_health:
                        text f"Avg Temperature: {average_temperature}°F" size 24 color "#FFFFFF"
                        bar value average_temperature range 100 xmaximum 400 ymaximum 20 style "temp_bar"

            hbox:
                xalign 0.5
                spacing 20
                textbutton "Write a report" action Show("medical_summary_sheet", player_obj=player_obj)
                textbutton "Quick Heal" action Show("heal_menu", player_obj=player_obj) style "inventory_button"
                textbutton "Close" action Hide("status_screen") style "close_button"

screen player_stats_screen(player_obj):
    modal True
    frame:
        xsize 1000
        ysize 800
        xalign 0.5
        background "#111111"

        at transform:
            alpha 0.0
            linear 0.5 alpha 1.0

        vbox:
            spacing 20
            text "Player Stats" size 40 xalign 0.5 color "#FFFFFF" bold True

            hbox:
                spacing 20
                xalign 0.5
                textbutton "Mental" action SetVariable("selected_category", "soft") style "category_button"
                textbutton "Physical" action SetVariable("selected_category", "hard") style "category_button"
                textbutton "Emotions" action SetVariable("selected_category", "emotions") style "category_button"
                textbutton "Relationships" action SetVariable("selected_category", "relationships") style "category_button"

            text "Filter:" size 20 color "#FFFFFF"
            input value VariableInputValue("stat_filter") allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ " xmaximum 300

            viewport:
                draggable True
                mousewheel True
                xsize 950
                ysize 600
                vbox:
                    spacing 20
                    if selected_category in ["soft", "hard"]:
                        for stat_name, stat_data in player_obj.stats.items():
                            if stat_filter.lower() in stat_name.lower() and ((selected_category == "soft" and stat_name in soft_skills) or (selected_category == "hard" and stat_name in hard_skills)):
                                frame:
                                    background "#222222"
                                    padding (15, 10)
                                    hbox:
                                        vbox:
                                            spacing 10
                                            text stat_name.replace("_", " ").capitalize() size 30 color "#00CCFF" bold True
                                            text f"Level: {stat_data['level']}" size 20 color "#CCCCCC" tooltip "Higher level unlocks better abilities."
                                            bar value stat_data["level"] range stat_data['max_xp'] xmaximum 600 ymaximum 25 bar_invert (stat_data["level"] < 5)
                                            text f"Skill: {stat_data['current_value']}" size 20 color "#CCCCCC"
                                            bar value stat_data["current_value"] range stat_data["max_xp"] xmaximum 600 ymaximum 25
                                            text f"XP: {stat_data['current_xp']} / {stat_data['max_xp']}" size 20 color "#CCCCCC"
                                            bar value stat_data["current_xp"] range stat_data["max_xp"] xmaximum 600 ymaximum 25
                                            if stat_data["current_xp"] >= stat_data["max_xp"]:
                                                textbutton "Level Up!" action Function(player_obj.level_up, stat_name) style "level_up_button"
                                        add f"images/stats_icons/{stat_name}.png" size (50, 50)

                    elif selected_category == "emotions":
                        $ top_emotions = player_obj.get_top_emotions()
                        $ other_emotions = [(name, val) for name, val in player_obj.emotions.items() if (name, val) not in top_emotions and stat_filter.lower() in name.lower()]
                        text "Top Emotions:" size 30 color "#FFFFFF"
                        for emo, val in top_emotions:
                            text f"{emo.capitalize()}: {val}" size 24 color "#CCCCCC"
                        text "Other Emotions:" size 30 color "#FFFFFF"
                        for emo, val in other_emotions:
                            text f"{emo.capitalize()}: {val}" size 24 color "#CCCCCC"

                    elif selected_category == "relationships":
                        for person, rel_data in player_obj.relationships.items():
                            if rel_data.get("met") and stat_filter.lower() in person.lower():
                                $ relationship_description = player_obj.get_relationship_description(person)
                                frame:
                                    background "#222222"
                                    padding (15, 10)
                                    vbox:
                                        text person.capitalize() size 30 color "#00CCFF" bold True
                                        text relationship_description size 20 color "#CCCCCC"
                                        $ bond_strength = (rel_data.get("trust", 0) + rel_data.get("friendship", 0)) / 2
                                        text "Bond Strength:" size 20 color "#FFFFFF"
                                        bar value bond_strength range 100 xmaximum 400 ymaximum 20

            textbutton "Close" action Hide("player_stats_screen") style "inventory_button" xalign 0.5

screen heal_menu(player_obj):
    modal True
    frame:
        xsize 500
        ysize 400
        xalign 0.5
        yalign 0.5
        background "#111111"
        at transform:
            alpha 0.0
            linear 0.5 alpha 1.0

        vbox:
            spacing 20
            text "Select a Body Part to Heal" size 30 xalign 0.5 color "#FFFFFF" bold True
            for part in ["head", "body", "left_arm", "right_arm", "left_leg", "right_leg"]:
                textbutton part.replace("_", " ").capitalize() action Show("medkit_item_menu", player_obj=player_obj, part=part) style "inventory_button" tooltip f"Heal {part} (Medical skill affects effectiveness)"
            textbutton "Cancel" action Hide("heal_menu") style "inventory_button" xalign 0.5

screen condition_details(player_obj, part):
    modal True
    frame:
        xsize 800
        ysize 600
        xalign 0.5
        yalign 0.5
        background "#111111"
        at transform:
            alpha 0.0
            linear 0.5 alpha 1.0

        vbox:
            spacing 20
            text f"{part.replace('_', ' ').title()} Status" size 40 xalign 0.5 color "#FFFFFF" bold True

            $ part_health = player_obj.health[part]['health']
            $ part_conditions = player_obj.health[part]['conditions']
            $ part_cleanliness = player_obj.health[part]['cleanliness']
            $ part_temp = player_obj.health[part]['temperature']
            $ can_view_health = player_obj.is_stat_higher("medical", 100)
            $ can_view_health_small = player_obj.is_stat_higher("medical", 59)
            $ has_thermometer = player_obj.inventory.has_item("thermometer")
            $ has_medkit = player_obj.inventory.has_item('medkit')
            $ medical_level = player_obj.stats.get("medical", {}).get("level", 0)
            $ pain_tolerance_bonus = player_obj.stats.get("pain_tolerance", {}).get("current_value", 0) / 10
            $ composure_bonus = player_obj.emotions.get("Composure", {}).get("value", 0) / 20
            $ adjusted_health_view = part_health + pain_tolerance_bonus + composure_bonus

            if can_view_health:
                text f"Health: {part_health}%" size 24 xalign 0.5 color "#FFFFFF"
                bar value part_health range 100 xmaximum 600 ymaximum 25 xalign 0.5 bar_invert (part_health < 50)
            elif can_view_health_small:
                text f"Estimated Health: {adjusted_health_view:.0f}%" size 24 xalign 0.5 color "#FFFFFF"
                if adjusted_health_view > 90:
                    text f"My {part} Feels Great!" size 24 xalign 0.5 color "#00FF00"
                elif adjusted_health_view > 50:
                    text f"My {part} Feels Fine." size 24 xalign 0.5 color "#FFD700"
                else:
                    text "It Hurts!" size 24 xalign 0.5 color "#FF0000"
            else:
                if part_health < (50 - pain_tolerance_bonus):
                    text "It Hurts!" size 24 xalign 0.5 color "#FF0000"
                else:
                    text "It feels alright." size 24 xalign 0.5 color "#AAAAAA"

            if can_view_health_small or (player_obj.emotions.get("Composure", {}).get("value", 0) > 50):
                text "Conditions:" size 30 xalign 0.5 color "#FFFFFF" bold True
                if part_conditions:
                    for condition in part_conditions:
                        text condition.capitalize() size 24 xalign 0.5 color "#CCCCCC"
                else:
                    text "No Current Conditions." size 24 xalign 0.5 color "#CCCCCC"
                text f"Hygiene: {part_cleanliness}%" size 24 xalign 0.5 color "#FFFFFF"
                bar value part_cleanliness range 100 xmaximum 600 ymaximum 25 xalign 0.5

            if has_thermometer or can_view_health or (player_obj.emotions.get("Authenticity", {}).get("value", 0) > 60):
                text f"Temperature: {part_temp}°F" size 24 xalign 0.5 color "#FFFFFF"
                bar value part_temp range 100 xmaximum 600 ymaximum 25 xalign 0.5

            if has_medkit:
                $ pride_bonus = player_obj.emotions.get("Pride", {}).get("value", 0) / 10
                $ heal_time = max(1, 10 - medical_level - pride_bonus)
                text f"Estimated Heal Time: {heal_time:.1f} minutes" size 20 xalign 0.5 color "#AAAAAA" italic True
                textbutton "Use Medkit" action Show("medkit_item_menu", player_obj=player_obj, part=part) style "inventory_button" xalign 0.5

            textbutton "Close" action Hide("condition_details") style "inventory_button" xalign 0.5

screen medkit_item_menu(player_obj, part):
    modal True
    frame:
        xsize 600
        ysize 500
        xalign 0.5
        yalign 0.5
        background "#111111"
        at transform:
            alpha 0.0
            linear 0.5 alpha 1.0

        vbox:
            spacing 20
            text "Select an Item to Use" size 30 xalign 0.5 color "#FFFFFF" bold True
            viewport:
                draggable True
                mousewheel True
                ysize 350
                vbox:
                    spacing 10
                    for item, info in medkit_contents.items():
                        python:
                            button_text = f"{item.capitalize()}"
                            if player_obj.is_stat_higher("medical", 40) or (player_obj.emotions.get("Intelligence", {}).get("value", 0) > 70):
                                button_text += f" (Heals: {', '.join(info['conditions'])}, Health: +{info['healing']})"
                        textbutton button_text action [Hide("medkit_item_menu"), Function(start_healing_timer, player_obj, part, item)] style "inventory_button" tooltip "Apply to treat conditions (will take time)"
            textbutton "Cancel" action Hide("medkit_item_menu") style "inventory_button" xalign 0.5

screen healing_timer(heal_duration, player_obj, part, item):
    modal True
    zorder 200
    frame:
        xalign 0.5 yalign 0.5
        xsize 400 ysize 200
        background "#000000AA"
        vbox:
            spacing 10
            text "Healing in Progress..." size 30 xalign 0.5 color "#FFFFFF"
            text "Please wait while the treatment takes effect." size 20 xalign 0.5 color "#CCCCCC"
            bar value AnimatedValue(0, heal_duration, heal_duration) range heal_duration xmaximum 300 ymaximum 20 xalign 0.5

    timer heal_duration action [Function(player_obj.use_medkit_item, part, item), Hide("healing_timer"), Notify("Healing complete!")]
screen medical_summary_sheet(player_obj):
    modal True
    frame:
        xsize 600
        ysize 700
        xalign 0.5
        yalign 0.5
        background Solid("#F5F5DC")  # Beige paper-like color placeholder; replace with "images/paper_background.png" when available

        vbox:
            spacing 10
            xalign 0.5
            yalign 0.5


            # Commented out for testing: Require pencil and paper
            if not (player_obj.inventory.has_item("pencil") and player_obj.inventory.has_item("paper")):
                text "I need a pencil and paper to write anything down!" size 24 color "#FF0000" xalign 0.5
                textbutton "Close" action Hide("medical_summary_sheet") xalign 0.5
            else:
                text "Medical Summary Sheet" size 30 color "#000000" bold True xalign 0.5  # Title like handwritten

                # Get key variables
                $ medical_level = player_obj.stats.get("medical", {}).get("level", 0)
                $ composure = player_obj.emotions.get("Composure", {}).get("value", 0)
                $ confidence = player_obj.emotions.get("Confidence", {}).get("value", 0)
                $ pride = player_obj.emotions.get("Pride", {}).get("value", 0)

                # Perform or retrieve roll for this last_label
                python:
                    if last_label not in summary_rolls:
                        summary_rolls[last_label] = player_obj.perform_roll("medical", base_chance=30 + medical_level * 5)
                    summary_quality = summary_rolls[last_label]

                # Emotion-based writing style modifiers
                python:
                    style_prefix = ""
                    if composure > 70:
                        style_prefix = "Health Report:"  # Precise and calm
                    elif composure < 30:
                        style_prefix = "Hmm I think.?"  # Scattered
                    if confidence < 30:
                        style_prefix += "I'm not sure, but... "
                    if pride > 70:
                        style_prefix += "As expected from someone like me, "

                # Averages (narrative phrasing)
                $ average_health, average_cleanliness, average_temperature = player_obj.calculate_averages()
                $ is_italics = composure < 50
                text "Overall Assessment:" size 26 color "#000000" bold True xalign 0.5
                if medical_level >= 1 or summary_quality:
                    text f"{style_prefix}My body feels about {average_health}% healthy overall. {'Pretty good!' if average_health > 70 else 'Could be better...' if average_health > 40 else 'It really hurts.'}" size 20 color "#000000" 
                if medical_level >= 2 or summary_quality:
                    text f"{style_prefix}Cleanliness is around {average_cleanliness}%. {'Spotless!' if average_cleanliness > 80 else 'A bit dirty.'}" size 20 color "#000000" 
                if medical_level >= 3 or summary_quality:
                    text f"{style_prefix}Average temperature feels like {average_temperature}°F. {'Normal.' if 90 > average_temperature > 60 else 'Too hot!' if average_temperature > 90 else 'Chilly.'}" size 20 color "#000000" 

                null height 20

                # Body Parts Summary (narrative, like personal notes)
                text "Body Parts Notes:" size 26 color "#000000" bold True xalign 0.5
                for part in ["head", "body", "left_arm", "right_arm", "left_leg", "right_leg"]:
                    python:
                        part_health = player_obj.health[part]['health']
                        part_conditions = player_obj.health[part]['conditions']
                        part_note = f"My {part.replace('_', ' ')}: "
                        if medical_level >= 5 or summary_quality:
                            part_note += f"Health at {part_health}%. "
                            if part_conditions:
                                part_note += f"Issues: {', '.join([c.capitalize() for c in part_conditions])}. "
                            else:
                                part_note += "No issues. "
                            part_note += "Feels " + ("amazing!" if part_health > 90 else "solid." if part_health > 60 else "painful.")
                        elif medical_level >= 3:
                            part_note += f"Roughly {part_health // 20 * 20}% healthy. "
                            part_note += f"{'Some conditions noted.' if part_conditions else 'Seems clear.'} "
                            part_note += "It's " + ("fine" if part_health > 60 else "hurting")
                        elif medical_level >= 1:
                            part_note += "Feels " + ("great" if part_health > 80 else "okay" if part_health > 50 else "bad")
                            if part_conditions:
                                part_note += ", something's off."
                        else:
                            part_note += "Hard to tell..."

                        # Emotion tweaks to note
                        if pride > 70 and part_health > 70:
                            part_note += " (As if i could get hurt by this!)"
                        elif confidence < 30:
                            part_note += "...I think?"

                    text part_note size 18 color "#000000"   # Italics if low composure (shaky writing)

                null height 20
                textbutton "Close" action Hide("medical_summary_sheet") xalign 0.5 style "inventory_button"
default summary_rolls = {}
init python:
    def start_healing_timer(player_obj, part, item):
        base_time = 60
        composure_bonus = player_obj.emotions.get("Composure", {}).get("value", 0) / 5
        confidence_penalty = max(0, 50 - player_obj.emotions.get("Confidence", {}).get("value", 0)) / 10
        heal_duration = base_time * (1 - composure_bonus / 100) + (confidence_penalty * 30)
        renpy.show_screen("healing_timer", heal_duration=heal_duration, player_obj=player_obj, part=part, item=item)
        