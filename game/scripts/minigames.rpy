screen roll_screen(base_chance, skill_name, modifiers=0):
    default show_minigame = False
    default minigame_bonus = 0

    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            text "Rolling for [skill_name]"
            text "Base Chance: [base_chance]%"
            text "Skill Level: [stats[skill_name]['current_value']]"
            text "Current Modifiers: [modifiers]"
            text "Total Chance: [base_chance + stats[skill_name]['current_value'] + modifiers]%"

            if skill_name == "intelligence" and not show_minigame:
                textbutton "Play Minigame to Increase Modifier":
                    action SetScreenVariable("show_minigame", True)

            if show_minigame:
                $ minigame_bonus = intelligence_minigame()
                text "Minigame Bonus: [minigame_bonus]"
                textbutton "Continue":
                    action [SetScreenVariable("modifiers", modifiers + minigame_bonus), SetScreenVariable("show_minigame", False)]

            textbutton "Roll":
                action [Return((roll_action(base_chance, skill_name, modifiers), modifiers + minigame_bonus))]