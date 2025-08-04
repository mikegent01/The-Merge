# Define the roll display screen (must be outside init python)
screen roll_display(roll_data):
    # roll_data is a dict with: skill, proficiency (or None), roll, threshold, total_chance, success, emotion_bonuses
    frame:
        align (0.5, 0.2)
        xpadding 20
        ypadding 20
        background "#000000aa"  # Semi-transparent black
        vbox:
            spacing 10
            text "Roll for [roll_data['skill']]" size 24 color "#ffffff"
            if roll_data['proficiency']:
                text "(Proficiency: [roll_data['proficiency']])" size 18 color "#dddddd"
            text "Rolled: [roll_data['roll']] (Threshold: [roll_data['threshold']])" size 18 color "#ffffff"
            text "Total Chance: [roll_data['total_chance']]%" size 18 color "#ffffff"
            text ("{color=#00ff00}Success!{/color}" if roll_data['success'] else "{color=#ff0000}Failure.{/color}") size 20
            text "Emotion Bonuses:" size 16 color "#dddddd"
            for emo, bonus in roll_data['emotion_bonuses']:
                text "[emo]: +[bonus]" size 14 color "#aaaaaa"
            textbutton "Dismiss" action Hide("roll_display") align (0.5, 1.0)

    # Auto-hide after 3 seconds
 #   timer 3.0 action Hide("roll_display")
