screen minigame_screen():
    modal True
    frame:
        xsize 600
        ysize 400
        xalign 0.5
        yalign 0.5
        background "#1a431a"
        padding (20, 20)

        vbox:
            spacing 10
            text "Mini-Game: Solve the Problem!" size 30 xalign 0.5 color "#FFFFFF" bold True
            text f"Score: {minigame_bonus}" size 20 color "#FFFFFF" xalign 0.5
            text f"Time Remaining: {minigame_time} seconds" size 20 color "#FFFFFF" xalign 0.5
            text f"Problem: {minigame_problem}" size 24 color "#FFFFFF" xalign 0.5

            hbox:
                xalign 0.5
                spacing 10
                input:
                    default ""
                    length 5
                    allow "0123456789"
                    color "#FFFFFF"
                    size 24
                    value VariableInputValue("player_answer")
                textbutton "Submit" action Function(check_minigame_answer) style "inventory_button"

screen roll_screen(base_chance, skill_level, skill_name, total_bonuses):
    modal True
    frame:
        xsize 600
        ysize 400
        xalign 0.5
        yalign 0.5
        background "#1a431a"
        padding (20, 20)

        vbox:        
            spacing 10
            text "Rolling for [skill_name.capitalize()]" size 30 xalign 0.5 color "#FFFFFF" bold True
            text f"Base Chance: {base_chance}%" size 20 color "#FFFFFF" xalign 0.5
            text f"Skill Level: {skill_level}" size 20 color "#FFFFFF" xalign 0.5
            text f"Current Modifier: {total_bonuses + minigame_bonus}" size 20 color "#FFFFFF" xalign 0.5
            text f"Total Chance: {base_chance + skill_level + total_bonuses + minigame_bonus}%" size 20 color "#FFFFFF" xalign 0.5

            # Mini-game for intelligence skill
            if skill_name == "intelligence":
                if minigame_time > 0:                
                    if minigame_active:
                        text "Solve as many problems as you can in 10 seconds!" size 18 color "#FFFFFF" xalign 0.5
                        text f"Time Remaining: {minigame_time} seconds" size 18 color "#FFFFFF" xalign 0.5
                        text f"Problem: {minigame_problem}" size 24 color "#FFFFFF" xalign 0.5

                        hbox:
                            xalign 0.5
                            spacing 10
                            input:
                                default ""
                                length 5
                                allow "0123456789"
                                color "#FFFFFF"
                                size 24
                                value VariableInputValue("player_answer")
                            textbutton "Submit" action Function(check_minigame_answer) style "inventory_button"

                        # Timer logic
                        if minigame_time > 0:
                            timer 1.0 action If(
                                minigame_time > 0,
                                SetVariable("minigame_time", minigame_time - 1),
                                [SetVariable("minigame_active", False), Hide("roll_screen")]
                            ) repeat True
                    else:
                        textbutton "Start Mini-Game" action Function(start_minigame) style "inventory_button" xalign 0.5

            # Roll button
            textbutton "Roll" action [Function(perform_roll, base_chance, skill_level, skill_name, total_bonuses), Hide("roll_screen")] style "inventory_button" xalign 0.5

