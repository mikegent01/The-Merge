screen character_selection:
    tag menu
    modal True

    # A frame to center the content
    frame:
        xsize 1100  # Increased width of the frame to give more space to the stats
        ysize 700    # Adjust height as needed
        xalign 0.5
        yalign 0.5
        background "#000000"

        # Split content into two sides (description and stats)
        hbox:
            spacing 50  # Space between the two sides
            yalign 0.5  # Vertically align the hbox in the middle of the screen
            xalign 0.5  # Horizontally align the hbox in the center

            # Left side for the stats (increased space for stats)
            vbox:
                xalign 0.0  # Align to the left
                spacing 10   # Space between each stat entry
                xsize 500    # Increased size for the stat section to avoid squishing

                text "Stats:" size 28  # Stats header
                if current_character_index == 0:
                    text "Intelligence: [ben_stats['intelligence']['current_value']] (Level: [ben_stats['intelligence']['level']])"
                    text "Speech: [ben_stats['speech']['current_value']] (Level: [ben_stats['speech']['level']])"
                    text "Strength: [ben_stats['strength']['current_value']] (Level: [ben_stats['strength']['level']])"
                    text "Luck: [ben_stats['luck']['current_value']] (Level: [ben_stats['luck']['level']])"
                    text "Speed: [ben_stats['speed']['current_value']] (Level: [ben_stats['speed']['level']])"
                    text "Pain Tolerance: [ben_stats['pain_tolerance']['current_value']] (Level: [ben_stats['pain_tolerance']['level']])"
                    text "Mental Resilience: [ben_stats['mental_resilience']['current_value']] (Level: [ben_stats['mental_resilience']['level']])"
                    text "Medical: [ben_stats['medical']['current_value']] (Level: [ben_stats['medical']['level']])"

                elif current_character_index == 1:
                    text "Intelligence: [dominic_stats['intelligence']['current_value']] (Level: [dominic_stats['intelligence']['level']])"
                    text "Speech: [dominic_stats['speech']['current_value']] (Level: [dominic_stats['speech']['level']])"
                    text "Strength: [dominic_stats['strength']['current_value']] (Level: [dominic_stats['strength']['level']])"
                    text "Luck: [dominic_stats['luck']['current_value']] (Level: [dominic_stats['luck']['level']])"
                    text "Speed: [dominic_stats['speed']['current_value']] (Level: [dominic_stats['speed']['level']])"
                    text "Pain Tolerance: [dominic_stats['pain_tolerance']['current_value']] (Level: [dominic_stats['pain_tolerance']['level']])"
                    text "Mental Resilience: [dominic_stats['mental_resilience']['current_value']] (Level: [dominic_stats['mental_resilience']['level']])"
                    text "Medical: [dominic_stats['medical']['current_value']] (Level: [dominic_stats['medical']['level']])"

                elif current_character_index == 2:
                    text "Intelligence: [david_stats['intelligence']['current_value']] (Level: [david_stats['intelligence']['level']])"
                    text "Speech: [david_stats['speech']['current_value']] (Level: [david_stats['speech']['level']])"
                    text "Strength: [david_stats['strength']['current_value']] (Level: [david_stats['strength']['level']])"
                    text "Luck: [david_stats['luck']['current_value']] (Level: [david_stats['luck']['level']])"
                    text "Speed: [david_stats['speed']['current_value']] (Level: [david_stats['speed']['level']])"
                    text "Pain Tolerance: [david_stats['pain_tolerance']['current_value']] (Level: [david_stats['pain_tolerance']['level']])"
                    text "Mental Resilience: [david_stats['mental_resilience']['current_value']] (Level: [david_stats['mental_resilience']['level']])"
                    text "Medical: [david_stats['medical']['current_value']] (Level: [david_stats['medical']['level']])"

            # Right side for the character description and image
            vbox:
                xalign 1.0  # Align to the right
                spacing 20  # Space between elements

                if current_character_index == 0:
                    text "Benjerman" size 35  # Character name
                    image "images/char/Benjerman/ben idle.png" xsize 300 ysize 300  # Adjust the image size as necessary
                    text "A army private first class with very high strength and some luck. He has knoledge of how to operate artillary equipment and train units. You start will start his story arriving at a military base in new mexico. He has arrived at the meeting room but not everything goes to plan.."

                elif current_character_index == 1:
                    text "Dominic" size 35
                    image "images/char/Dominic/dominiccas.png" xsize 300 ysize 300
                    text "A civilian with great intelligence and speech skills, adept at negotiations."

                elif current_character_index == 2:
                    text "David" size 35
                    image "images/char/David/david.png" xsize 300 ysize 300
                    text "A political strategist with high intelligence and strong social influence."

        # Navigation buttons in a single line (Next, Back, Choose)
        hbox:
            spacing 20  # Space between the buttons
            yalign 1.0  # Align buttons to the bottom of the frame
            xalign 0.5  # Center the buttons horizontally

       #     textbutton "Next Character" action [
       #         SetVariable("current_character_index", (current_character_index + 1) % 3),  # Cycle to next character
       #         # Update selected character name
       #         SetVariable("current_selected_character", 
       #             If(current_character_index == 0, "Dominic",
       #             If(current_character_index == 1, "David",
       #             "Ben"))),
       #     ]

          #  textbutton "Back" action [
          #      SetVariable("current_character_index", (current_character_index - 1 + 3) % 3),  # Cycle to previous character
          #      SetVariable("current_selected_character", 
          #          If(current_character_index == 0, "David",
          #          If(current_character_index == 1, "Ben",
          #          "Dominic"))),
          #  ]

            textbutton "Play" action [
                Jump("start") 
            ]
