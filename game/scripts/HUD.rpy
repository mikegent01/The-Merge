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
    "images/inventory/inventory_hud/meidc_hud.png"  # Path to your health icon
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
screen journal():
    tag menu
    style_prefix "journal"
    
    default current_journal_section = "quests"
    default expanded_entry = None
    default personal_notes_text = ""
    
    # Example data
    default quests = [
        {"title": "Lost Artifact", "desc": "Find the ancient relic in the ruins", 
         "details": "The artifact is said to be hidden in the deepest chamber.\n\nReward: 500 gold\n\nDanger Level: High", 
         "status": "active", "image": "artifact_thumb"},
        
        {"title": "Delivery Job", "desc": "Deliver package to blacksmith", 
         "details": "Package must arrive before sunset.\nLocation: Market District\n\nReward: 100 gold", 
         "status": "available", "image": None}
    ]

    default characters = [
        {"name": "Lydia", "desc": "A skilled warrior from the northern tribes.", 
         "details": "Lydia is known for her unmatched swordsmanship and loyalty. She has a mysterious past tied to the royal family.", 
         "image": "lydia_portrait", "drawing": "lydia_sketch"},
        
        {"name": "Merlin", "desc": "An eccentric inventor obsessed with steam technology.", 
         "details": "Merlin is a genius inventor who spends most of his time in his workshop. He is often misunderstood but has a kind heart.", 
         "image": None, "drawing": "merlin_sketch"}
    ]

    default game_notes = [
        {"text": "The mayor seemed nervous when mentioning the ruins...", "time": "Day 3: Morning"},
        {"text": "Need to check the old map again", "time": "Day 4: Evening"}
    ]

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1200
        ysize 700
        background Solid("#333333")
        
        vbox:
            spacing 20
            
            # Tabs
            hbox:
                spacing 50
                textbutton "Quests":
                    action [SetScreenVariable("current_journal_section", "quests"), 
                           SetScreenVariable("expanded_entry", None)]
                    style "journal_tab_button"
                textbutton "Characters":
                    action [SetScreenVariable("current_journal_section", "characters"), 
                           SetScreenVariable("expanded_entry", None)]
                    style "journal_tab_button"
                textbutton "Notes":
                    action [SetScreenVariable("current_journal_section", "notes"), 
                           SetScreenVariable("expanded_entry", None)]
                    style "journal_tab_button"
                textbutton "Personal":
                    action [SetScreenVariable("current_journal_section", "personal"), 
                           SetScreenVariable("expanded_entry", None)]
                    style "journal_tab_button"
            
            # Main Content
            frame:
                xsize 1150
                ysize 600
                background Solid("#404040")
                
                if current_journal_section == "quests":
                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        vbox:
                            spacing 10
                            for quest in quests:
                                frame:
                                    background Solid("#505050")
                                    xfill True
                                    padding (20, 20)
                                    
                                    if expanded_entry == quest:
                                        # Expanded view
                                        vbox:
                                            spacing 15
                                            hbox:
                                                text quest["title"] style "journal_title"
                                                text "Status: [quest['status'].title()]" style "journal_status" xalign 1.0
                                            
                                            if quest["image"] and renpy.loadable(quest["image"]):
                                                add quest["image"] xalign 0.5
                                            else:
                                                text "No Image Available" xalign 0.5 style "journal_hint"
                                            
                                            text quest["desc"] style "journal_desc"
                                            null height 20
                                            text "Detailed Information:" style "journal_subheader"
                                            text quest["details"] style "journal_details"
                                            
                                            textbutton "Collapse":
                                                style "journal_button"
                                                action SetScreenVariable("expanded_entry", None)
                                                xalign 1.0
                                    else:
                                        # Collapsed view
                                        button:
                                            background None
                                            xfill True
                                            action SetScreenVariable("expanded_entry", quest)
                                            hbox:
                                                spacing 20
                                                if quest["image"] and renpy.loadable(quest["image"]):
                                                    add quest["image"] size (80, 80)
                                                else:
                                                    frame:
                                                        background Solid("#606060")
                                                        xsize 80
                                                        ysize 80
                                                        text "?" style "journal_symbol"
                                                
                                                vbox:
                                                    text quest["title"] style "journal_entry_title"
                                                    text quest["desc"] style "journal_entry_desc"
                
                elif current_journal_section == "characters":
                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        vbox:
                            spacing 10
                            for char in characters:
                                frame:
                                    background Solid("#505050")
                                    xfill True
                                    padding (20, 20)
                                    
                                    if expanded_entry == char:
                                        # Expanded view
                                        vbox:
                                            spacing 15
                                            text char["name"] style "journal_title"
                                            
                                            hbox:
                                                spacing 20
                                                if char["image"] and renpy.loadable(char["image"]):
                                                    add char["image"] size (200, 200)
                                                elif char["drawing"] and renpy.loadable(char["drawing"]):
                                                    add char["drawing"] size (200, 200)
                                                else:
                                                    text "No Image Available" xalign 0.5 style "journal_hint"
                                            
                                            text char["desc"] style "journal_desc"
                                            null height 20
                                            text "Detailed Information:" style "journal_subheader"
                                            text char["details"] style "journal_details"
                                            
                                            textbutton "Collapse":
                                                style "journal_button"
                                                action SetScreenVariable("expanded_entry", None)
                                                xalign 1.0
                                    else:
                                        # Collapsed view
                                        button:
                                            background None
                                            xfill True
                                            action SetScreenVariable("expanded_entry", char)
                                            hbox:
                                                spacing 20
                                                if char["image"] and renpy.loadable(char["image"]):
                                                    add char["image"] size (80, 80)
                                                elif char["drawing"] and renpy.loadable(char["drawing"]):
                                                    add char["drawing"] size (80, 80)
                                                else:
                                                    frame:
                                                        background Solid("#606060")
                                                        xsize 80
                                                        ysize 80
                                                        text "?" style "journal_symbol"
                                                
                                                vbox:
                                                    text char["name"] style "journal_entry_title"
                                                    text char["desc"] style "journal_entry_desc"
                
                elif current_journal_section == "notes":
                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        vbox:
                            spacing 10
                            for note in game_notes:
                                frame:
                                    background Solid("#505050")
                                    xfill True
                                    padding (20, 20)
                                    text "[note['time']]\n{color=#AAAAAA}[note['text']]{/color}" style "journal_note_text"
                
                elif current_journal_section == "personal":
                    vbox:
                        text "Personal Notes:" style "journal_subheader"
                        input:
                            value VariableInputValue("personal_notes_text")
                            xsize 1100
                            ysize 500
                            style "journal_input"

style journal_title:
    size 36
    color "#FFD700"
    bold True

style journal_entry_title:
    size 28
    color "#FFFFFF"

style journal_entry_desc:
    size 22
    color "#AAAAAA"

style journal_desc:
    size 24
    color "#CCCCCC"
    line_spacing 5

style journal_details:
    size 22
    color "#AAAAAA"
    line_spacing 3
    italic True

style journal_button:
    background Solid("#606060")
    hover_background Solid("#707070")
    padding (25, 8)
    outlines [ (1, "#000000", 0, 0) ]

style journal_subheader:
    size 28
    color "#FFFFFF"
    bold True

style journal_hint:
    size 22
    color "#888888"
    italic True

style journal_symbol:
    size 48
    color "#FFFFFF"
    bold True
    xalign 0.5
    yalign 0.5

style journal_note_text:
    size 20
    color "#AAAAAA"
    italic True