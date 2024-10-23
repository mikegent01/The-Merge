screen HUD():
    frame:
        xpos 0
        ypos 0
        xminimum 0
        yminimum 1
        background None  # Set the background to None for transparency

        has hbox

        # Backpack Icon
        imagebutton:
            idle "Backpack"
            hover "Backpack_Hover"
            action Show("inventory")
            padding (10, 10, 10, 10)

        # Health Icon
        imagebutton:
            idle "Health"
            hover "Health_Hover"
            action Show("status_screen")
            padding (10, 10, 10, 10)

        # Quest Log Icon
        imagebutton:
            idle "Quest_Log"
            hover "Quest_Log_Hover"
            action Show("quest_log")
            padding (10, 10, 10, 10)

        # Head Log Icon
        imagebutton:
            idle "head"
            hover "head_hover"
            action Show("player_stats_screen")
            padding (10, 10, 10, 10)

screen quest_log():
    frame:
        xpadding 20
        ypadding 20
        xalign 0.5
        yalign 0.5
        background "#1a431a"

        # Title
        text "Quest Log" style "title"

        vbox:
            spacing 15
            align (0.5, 0.5)  # Center the vbox

            # Quest: New Uniform Quest
            if new_uniform_quest:  # Show this quest only if new_uniform_quest is True
                hbox:
                    spacing 10

                    # Show check or cross emoji based on condition
                    if uniform_ordered:
                        text "✓" style "checkbox_emoji"  # Checked state (Completed)
                    else:
                        text "✗" style "checkbox_emoji"  # Unchecked state (Not completed)

                    # Quest Description
                    text "Go to the front desk to order a new uniform." style "quest_text"

            # Quest: Projector Quest
            if projectorquest:  # Show this quest only if projectorquest is True
                hbox:
                    spacing 10

                    # Show check or cross emoji based on condition
                    if projector_obtained:
                        text "✓" style "checkbox_emoji"  # Checked state (Completed)
                    else:
                        text "✗" style "checkbox_emoji"  # Unchecked state (Not completed)

                    # Quest Description
                    text "Get a new projector and bring it to the projector room." style "quest_text"

        # Close Button
        textbutton "Close" action Hide("quest_log") align (0.5, 0.95)  # Align the button to the bottom center

# Style for the title
style title:
    size 30
    color "#FFFFFF"  # White color for the title
    xalign 0.5       # Center the title

# Style for the quest description text
style quest_text:
    size 22
    color "#FFFFFF"  # White color for the quest text

# Style for the check and cross emojis
style checkbox_emoji:
    size 30
    color "#ffffff"  # White color for the check/cross emoji


# Images for icons
image Backpack:
    "images/inventory/inventory_hud/backpack.png"
    size(60,60)

image Backpack_Hover:
    "images/inventory/inventory_hud/backpack_hover.png"
    size(60,60)

image Health:
    "images/inventory/inventory_hud/meidc_hud.gif"  # Path to your health icon
    size(60,60)

image Health_Hover:
    "images/inventory/inventory_hud/medic_hover.png"  # Path to your health hover icon
    size(60,60)

image Quest_Log:
    "images/inventory/inventory_hud/Quest_Log.png"  # Path to your quest log icon
    size(60,60)

image Quest_Log_Hover:
    "images/inventory/inventory_hud/Quest_Log_hover.png"  # Path to your hover image for the quest log
    size(60,60)

image Checkbox_Unchecked:
    "images/inventory/inventory_hud/close.png"  # Path to your unchecked checkbox image
    size(20,20)
image Checkbox_Checked:
    "images/inventory/inventory_hud/close_hover.png"  # Path to your checked checkbox image
    size(20,20)
