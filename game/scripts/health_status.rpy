
# Main status screen with option to view detailed player stats
screen status_screen():
  modal True
  frame:
    xsize 600
    ysize 400
    xalign 0.5
    yalign 0.5
    background "#000000"
    $ can_view_health = is_stat_higher("medical", 100, stats)
    $ can_view_health_small = is_stat_higher("medical", 50, stats)
    vbox:
      text "My Health Overview" size 30 xalign 0.5
      for part in ["head", "body", "left_arm", "right_arm", "left_leg", "right_leg"]:
        hbox:
          text part.replace("_", " ").capitalize() + ":" xalign 0.0
          if can_view_health:
            bar value default_status[part]["health"] range 100 xmaximum 200 ymaximum 25 xalign 0.5
          textbutton "View Status" action Show("condition_details", part=part) xalign 1.0
  
        # Close button to hide the status screen
      textbutton "Close" action Hide("status_screen") xalign 0.5
screen player_stats_screen():
  modal True
  frame:
    xsize 900 # Adjusted size to fit stats and bars
    ysize 900 # Increased height for better display of all content
    xalign 0.5
    yalign 0.5
    background "#000000"

    vbox:

      text "\n"
      text "\n"
      text "My Stats" size 30 xalign 0.5 yalign 0.4 

      vpgrid:

        cols 2 # Two columns for stats
        spacing 30
        ysize 600 

        for stat in ["intelligence", "speech", "strength", "luck", "speed", "medical","pain_tolerance","mental_resilience"]:
          hbox:
            vbox:
              text "My [stat.replace('_', ' ').capitalize()] is level: [stats[stat]['level']] My skill is [stats[stat]['current_value']]" size 20 
              bar value stats[stat]["level"] range stats[stat]['max_xp'] xmaximum 300 ymaximum 25
              text "I Currently have [stats[stat]['current_xp']] out of [stats[stat]['max_xp']] EXP" size 14
              bar value stats[stat]["current_xp"] range stats[stat]["max_xp"] xmaximum 300 ymaximum 25
              if stats[stat]["current_xp"] >= stats[stat]["max_xp"]:
                textbutton "Level Up" action Function(level_up, stat)


      text "Current Sanity" size 14
      hbox:
        bar value stats["sanity"]["current_sanity"] range 100 xmaximum 300
        text "[stats['sanity']['current_sanity']]" size 20
        textbutton "Close" action Hide("player_stats_screen") xalign 0.5

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
# Updated Condition Details screen with medkit healing for conditions and health
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

            $ medical_level = stats["medical"]["level"]
            $ can_view_health = is_stat_higher("medical", 100, stats)
            $ can_view_health_small = is_stat_higher("medical", 59, stats)

            # Health bar visibility based on medical skill
            if can_view_health:
                text "Health: [default_status[part]['health']]%" size 20 xalign 0.5
                bar value default_status[part]["health"] range 100 xmaximum 500 ymaximum 25 xalign 0.5
            # else:
            #    text "I don't have enough medical skill to know why I feel this way..." size 20 xalign 0.5 color "#FFA500"

            # Conditions display if medical level is sufficient
            if can_view_health_small:
                text "Conditions:" size 20 xalign 0.0
                if default_status[part]["conditions"]:
                    for condition in default_status[part]["conditions"]:
                        hbox:
                            text condition.capitalize() xalign 0.0
                else:
                    text "No Current conditions." size 20 xalign 0.5
            # else:
            #    if not has_item("thermometer"):
            #        text "Thermometer not available." size 20 xalign 0.5 color "#FFA500"

            if has_item("thermometer"):
                text "Temperature: [default_status[part]['temperature']]°F" size 20 xalign 0.5
            $ temp = default_status[part]['temperature']
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
            if has_item('medkit'):
                textbutton "Use Medkit" action [Show("medkit_item_menu", part=part)] xalign 0.5

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
