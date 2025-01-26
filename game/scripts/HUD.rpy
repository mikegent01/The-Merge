screen HUD():
    frame:
        xpos 0
        ypos 0
        xminimum 0
        yminimum 1
        background None  # Set the background to None for transparency

        has hbox

        # Backpack Icon
        if inventory:
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
    # Main Frame for the Quest Log
    frame:
        xpadding 30
        ypadding 30
        xalign 0.5
        yalign 0.5
        background "#1a431a"
        xsize 800
        ysize 600

        vbox:
            spacing 20
            align (0.5, 0.5)

            # Title
            text "Quest Log" style "title" xalign 0.5

            # Quest List
            viewport:
                draggable True
                mousewheel True
                xsize 750
                ysize 450

                vbox:
                    spacing 15
                    xalign 0.5

                    # Iterate over the quests array
                    for quest in quests:
                        # Ensure the 'expanded' key exists
                        if "expanded" not in quest:
                            $ quest["expanded"] = False

                        frame:
                            background "#2a4a2a"
                            padding (10, 10)
                            xsize 700

                            # Quest Name (Clickable)
                            if not quest["expanded"]:
                                textbutton quest["name"]:
                                    action ToggleDict(quest, "expanded")
                                    style "quest_button"
                                    xalign 0.0

                            # Quest Details (Visible if expanded)
                            if quest["expanded"]:
                                vbox:
                                    spacing 10
                                    xalign 0.0

                                    # Quest Description
                                    text quest["description"] style "quest_text"

                                    # Quest Status
                                    hbox:
                                        spacing 10
                                        text "Status:" style "quest_text"
                                        text ("Completed" if quest["completed"] else "In Progress") style "quest_text" color ("#00FF00" if quest["completed"] else "#FF0000")
                                        text "\n"
                                        textbutton "Close":
                                            action ToggleDict(quest, "expanded")
                                            style "quest_button"
                                            xalign 0.0                                        

            # Close Button at the bottom
            if not quest["expanded"]: 
                textbutton "Close":
                    action Hide("quest_log")
                    xalign 0.5
                    yalign 1.0
                    style "close_button"

style title:
    size 40
    color "#FFFFFF"
    bold True
    xalign 0.5

style quest_button:
    background None
    padding (5, 5)
    hover_background "#3a5c4a"
    xalign 0.0

style quest_text:
    size 20
    color "#CCCCCC"
    xalign 0.0

style close_button:
    background "#333333"
    padding (10, 5)
    hover_background "#444444"
    xalign 0.5
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
