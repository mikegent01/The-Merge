screen status_screen():
    modal True
    frame:
        xsize 600
        ysize 400
        xalign 0.5
        yalign 0.5
        background "#000000"

        # Calculate averages
        $ average_health, average_cleanliness, average_temperature = calculate_averages()

        $ medical_level = stats["medical"]["level"]
        $ can_view_health = is_stat_higher("medical", 100, stats)
        $ can_view_health_small = is_stat_higher("medical", 59, stats)
        $ can_view_hygiene = is_stat_higher("intelligence", 50, stats)
        vbox:
            text "My Health Overview" size 30 xalign 0.5

            for part in ["head", "body", "left_arm", "right_arm", "left_leg", "right_leg"]:
                hbox:
                    text part.replace("_", " ").capitalize() + ":" xalign 0.0
                    if not can_view_health:
                        textbutton "View Status" action Show("condition_details", part=part) xalign 1.0
                    if can_view_health:
                        bar value default_status[part]["health"] range 100 xmaximum 200 ymaximum 25 xalign 0.5
                        textbutton "View Status" action Show("condition_details", part=part) xalign 1.0

            vbox:  # To stack the sanity text and bar vertically
                if can_view_health_small:
                    text "Current Sanity: [stats['sanity']['current_sanity']]" size 20 xalign 0.5
                elif can_view_health:
                    bar value stats["sanity"]["current_sanity"] range 100 xmaximum 300 xalign 0.5

            # Display averages
            if can_view_health_small:
                text "My Estimated Average Health: [average_health]%" size 20 xalign 0.5
                bar value average_health range 100 xmaximum 200 ymaximum 25 xalign 0.5
                text "Average Cleanliness: [average_cleanliness]%" size 20 xalign 0.5
                bar value average_cleanliness range 100 xmaximum 200 ymaximum 25 xalign 0.5
            if has_item("thermometer"):
                text "Average Temperature: [average_temperature]°F" size 20 xalign 0.5
                bar value average_temperature range 100 xmaximum 200 ymaximum 25 xalign 0.5

            textbutton "Close" action Hide("status_screen") xalign 0.5





screen player_stats_screen():
    modal True
    frame:
        xsize 900
        ysize 900
        xalign 0.5
        yalign 0.5
        background "#000000"

        vbox:
            text "\n"
            text "\n"
            text "My Stats" size 30 xalign 0.5 yalign 0.4
            textbutton "Close" action Hide("player_stats_screen") xalign 0.5
            # Entire content wrapped inside a viewport for unified scrolling
            hbox:
                viewport:
                    id "stats_viewport"
                    xsize 850
                    ysize 750  # Adjusted to fit in most screens while leaving space for the close button
                    draggable True
                    mousewheel True
                    
                    vbox:
                        # Stats section
                        for stat in ["intelligence", "speech", "strength", "luck", "speed", "medical", "pain_tolerance", "mental_resilience"]:
                            vbox:
                                text "[stat.replace('_', ' ').capitalize()] is level: [stats[stat]['level']]" size 15
                                bar value stats[stat]["level"] range stats[stat]['max_xp'] xmaximum 300 ymaximum 25
                                text "Skill is: [stats[stat]['current_value']]" size 15
                                bar value stats[stat]["current_value"] range stats[stat]["max_xp"] xmaximum 300 ymaximum 25
                                text "[stats[stat]['current_xp']] out of [stats[stat]['max_xp']] experience till next level" size 15
                                bar value stats[stat]["current_xp"] range stats[stat]["max_xp"] xmaximum 300 ymaximum 25
                                if stats[stat]["current_xp"] >= stats[stat]["max_xp"]:
                                    textbutton "Level Up" action Function(level_up, stat)
                                text "\n"
                                text "\n"
                                text "\n"
                                text "\n"

                vbar value YScrollValue("stats_viewport") xsize 25
screen heal_menu():
    modal True
    frame:
        xsize 400
        ysize 340
        xalign 0.5
        yalign 0.5
        background "#000000"

        vbox:
            text "Select a body part to heal" size 30 xalign 0.5

            for part in ["head", "body", "left_arm", "right_arm", "left_leg", "right_leg"]:
                textbutton part.replace("_", " ").capitalize() action [Show("medkit_item_menu", part=part)] xalign 0.5

            textbutton "Cancel" action Hide("heal_menu") xalign 0.5
screen condition_details(part):
    modal True
    frame:
        xsize 600
        ysize 450
        xalign 0.5
        yalign 0.5
        background "#000000"

        vbox:
            # Use replace to display part name with spaces
            text part.replace("_", " ").capitalize() + " Status" size 30 xalign 0.5

            # Health Status
            $ health = default_status[part]['health']
            if health > 90:
                text "My " + part.replace("_", " ") + " feels Great!" size 18 xalign 0.5 color "#00ff008e"
            elif health > 75:
                text "My " + part.replace("_", " ") + " feels Good!" size 18 xalign 0.5 color "#32CD32"
            elif health > 50:
                text "My " + part.replace("_", " ") + " feels Fine.." size 18 xalign 0.5 color "#FFD700"
            elif health > 25:
                text "It hurts. My " + part.replace("_", " ") + " hurts!" size 18 xalign 0.5 color "#FFA500"
            elif health > 10:
                text "It fucking hurts!" size 18 xalign 0.5 color "#ff0000"
            else:
                text "I am at Death's Door..." size 18 xalign 0.5 color "#FF0000"

            # Medical Skill Check
            $ medical_level = stats["medical"]["level"]
            $ can_view_health = is_stat_higher("medical", 100, stats)
            $ can_view_health_small = is_stat_higher("medical", 59, stats)
            $ can_view_hygiene = is_stat_higher("intelligence", 50, stats)

            if can_view_health:
                text "Health: [default_status[part]['health']]%" size 20 xalign 0.5
                bar value default_status[part]["health"] range 100 xmaximum 500 ymaximum 25 xalign 0.5

            # Conditions Display if Medical Level is Sufficient
            if can_view_health_small:
                text "Conditions:" size 20 xalign 0.0
                if default_status[part]["conditions"]:
                    for condition in default_status[part]["conditions"]:
                        hbox:
                            text condition.capitalize() xalign 0.0
                else:
                    text "No Current conditions." size 20 xalign 0.5
            $ temp = default_status[part]['temperature']
            $ cleanliness = default_status[part]['cleanliness']
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
            if can_view_health_small:
                if can_view_hygiene:
                    text "Hygiene: [default_status[part]['cleanliness']]%" size 20 xalign 0.5

            # Temperature Display
            if has_item("thermometer"):
                text "Temperature: [default_status[part]['temperature']]°F" size 20 xalign 0.5
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
                textbutton "Use Medkit" action [Show("medkit_item_menu", part=part)] xalign 0.5

            # Close Button
            textbutton "Close" action Hide("condition_details") xalign 0.5


screen medkit_item_menu(part):
    modal True
    frame:
        xsize 400
        ysize 400
        xalign 0.5
        yalign 0.5
        background "#000000"

        vbox:
            text "Select an item to use" size 30 xalign 0.5

            # Scrollable container for the list of items
            viewport:
                draggable True
                mousewheel True
                ysize 250  # Adjust this size to control the height of the scrollable area

                vbox:
                    # List each item from the medkit that can be used to heal the part
                    for item, info in medkit_contents.items():
                        if is_stat_higher("medical", 40, stats):
                            # Show full info if medical stat is higher than 40
                            textbutton f"{item.capitalize()} (Heals: {', '.join(info['conditions'])}, Health: +{info['healing']})" action [Function(use_medkit_item, part, item), Hide("medkit_item_menu")]
                        else:
                            # Show only the item name, without healing info
                            textbutton f"{item.capitalize()}" action [Function(use_medkit_item, part, item), Hide("medkit_item_menu")]

            textbutton "Cancel" action Hide("medkit_item_menu") xalign 0.5
