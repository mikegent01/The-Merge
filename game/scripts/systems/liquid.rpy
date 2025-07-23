init python:
    selected_liquids = []
    selected_container = None
    def add_liquid(liquid_name, amount):
        for liquid in liquid_inventory:
            if liquid["name"] == liquid_name:
                liquid["amount"] += amount
                break

    def remove_liquid(liquid_name, amount):
        for liquid in liquid_inventory:
            if liquid["name"] == liquid_name:
                if liquid["amount"] >= amount: liquid["amount"] -= amount
                else: renpy.notify("Not enough liquid available.")
                break

screen combine_liquids_screen(player_obj):
    modal True
    tag liquids

    frame:
        style "section_frame"
        xysize (1000, 700)
        xalign 0.5 yalign 0.5

        vbox:
            spacing 15
            text "Liquid Station" size 30 xalign 0.5 color "#FFFFFF"

            hbox:
                spacing 20

                vbox:
                    spacing 10
                    text "Available Pure Liquids" size 20 color "#FFFFFF"
                    frame:
                         style "section_frame"
                         background "#2E4F2E"
                         padding (10, 10, 10, 10)
                         xsize 250 ysize 550
                         viewport:
                             scrollbars "vertical" mousewheel True
                             vbox:
                                 spacing 8
                                 if not player_obj.inventory.liquids:  # Use obj.inventory.liquids
                                     text "- None -" size 14 color "#AAAAAA"
                                 for liquid in player_obj.inventory.liquids:  # Use obj.inventory.liquids
                                      if liquid.get("amount", 0) > 0:
                                          text f"{liquid['name']}: {liquid['amount']} ml" size 16 color "#DDDDDD"
                                          if selected_container:
                                               textbutton "Add to Bottle" action Function(add_liquid_to_selected, liquid) style "inventory_button" text_size 12 padding (5,2) sensitive (selected_container["current_amount"] < selected_container["capacity"])

                vbox:
                    spacing 10
                    text "Containers" size 20 color "#FFFFFF"
                    frame:
                         style "section_frame"
                         background "#2E4F2E"
                         padding (10, 10, 10, 10)
                         xsize 300 ysize 550
                         viewport:
                             scrollbars "vertical" mousewheel True
                             vbox:
                                 spacing 8
                                 if not player_obj.inventory.containers:  # Use obj.inventory.containers
                                      text "- None -" size 14 color "#AAAAAA"
                                 for container in player_obj.inventory.containers:  # Use obj.inventory.containers
                                      button:
                                          action SetVariable("selected_container", container)
                                          hbox:
                                              spacing 10
                                              $ img_path = "images/inventory/" + container['name'].replace(" ", "_") + ".png"
                                              if renpy.loadable(img_path):
                                                  add img_path zoom 0.3
                                              else:
                                                  frame:
                                                      xysize(30,30)
                                                      background "#AAAAAA"

                                              vbox:
                                                  text container["name"] size 16 color ("#FFFF88" if selected_container == container else "#FFFFFF")
                                                  text f"{container['current_amount']} / {container['capacity']} ml" size 14 color "#CCCCCC"
                                                  bar value container["current_amount"] range container["capacity"] xsize 100

                vbox:
                    spacing 10
                    text "Selected Container" size 20 color "#FFFFFF"
                    frame:
                         style "section_frame"
                         background "#2E4F2E"
                         padding (10, 10, 10, 10)
                         xsize 350 ysize 550
                         if selected_container:
                             vbox:
                                 spacing 8
                                 text selected_container["name"] size 18 color "#FFFF88" xalign 0.5
                                 $ img_path = "images/inventory/" + selected_container['name'].replace(" ", "_") + ".png"
                                 if renpy.loadable(img_path):
                                     add img_path zoom 0.5 xalign 0.5
                                 else:
                                     frame:
                                         xysize(60,60)
                                         background "#AAAAAA"
                                         xalign 0.5

                                 bar value selected_container["current_amount"] range selected_container["capacity"] xsize 250 xalign 0.5
                                 text f"{selected_container['current_amount']} / {selected_container['capacity']} ml" size 16 color "#CCCCCC" xalign 0.5

                                 text "Contents:" size 16 color "#FFFFFF"
                                 if not selected_container["contents"]:
                                     text "- Empty -" color "#AAAAAA"
                                 else:
                                     for content in selected_container["contents"]:
                                         text f"- {content.get('name', 'Unknown')}: {content.get('amount', 0)} ml" size 14 color "#DDDDDD"

                                 null height 15
                                 text "Actions:" size 16 color "#FFFFFF"
                                 textbutton "Drain 10ml" action Function(drain_liquid, selected_container) style "inventory_button" sensitive (selected_container["current_amount"] > 0)
                                 textbutton "Pour Into..." action Show("liquid_pour_target_screen", source_container=selected_container) style "inventory_button" sensitive (selected_container["current_amount"] > 0)
                                 if len(selected_container["contents"]) >= 2:
                                     textbutton "Mix Contents" action [Function(reset_stirring), Show("stirring_minigame")] style "inventory_button"

                         else:
                             text "Select a container from the list." xalign 0.5 yalign 0.5 color "#AAAAAA"

            null height 10
            textbutton "Close Liquids" action [SetVariable("selected_container", None), Hide("liquids")] style "inventory_button" xalign 0.5

# --- Liquid Pour Target Screen ---
screen liquid_pour_target_screen(source_container):
     modal True

     frame:
         style "section_frame"
         padding (20, 20, 20, 20)
         xalign 0.5 yalign 0.5

         vbox:
             spacing 10
             text f"Pour from {source_container['name']} into:" size 20 color "#FFFFFF"

             viewport:
                 ysize 300
                 scrollbars "vertical" mousewheel True
                 vbox:
                     spacing 8
                     textbutton "Ground" action [Function(pour_liquid, source_container, None), Hide("liquid_pour_target_screen")] style "inventory_button"
                     if not player_obj.inventory.containers:
                         text "- No other containers -" size 14 color "#AAAAAA"
                     for target_container in player_obj.inventory.containers:
                         if target_container != source_container:
                             $ available_space = target_container["capacity"] - target_container["current_amount"]
                             textbutton f"{target_container['name']} ({available_space} ml space)" action [Function(pour_liquid, source_container, target_container), Hide("liquid_pour_target_screen")] style "inventory_button" sensitive (available_space > 0)

             null height 10
             textbutton "Cancel" action Hide("liquid_pour_target_screen") style "inventory_button"


# --- Stirring Minigame Screen ---
screen stirring_minigame():
    modal True

    frame:
        style "section_frame"
        xysize (500, 500)
        xalign 0.5 yalign 0.5

        vbox:
            spacing 15
            text "Mix Liquids" size 25 color "#FFFFFF" xalign 0.5

            text "Select Stirring Tool:" size 18 color "#DDDDDD" xalign 0.5
            hbox:
                xalign 0.5 spacing 10
                $ possible_tools = ["Stick", "Spoon", "Hand"]
                for tool in possible_tools:
                    if has_stirring_tool(tool):
                        textbutton tool action SetVariable("stirring_tool", tool) style "inventory_button"
                    else:
                        textbutton tool action None style "inventory_button" sensitive False

            if stirring_tool:
                text f"Using: {stirring_tool}" size 16 color "#FFFF88" xalign 0.5
                null height 20

                frame:
                    background "#0A200A"
                    xysize (300, 200) xalign 0.5
                    text "Stir Here (Mouse Movement)" xalign 0.5 yalign 0.5 color "#AAAAAA"
                    timer 0.1 repeat True action Function(update_stirring_progress)

                null height 10
                bar value stirring_progress range 100 xsize 300 xalign 0.5 left_bar "#4CAF50" right_bar "#2A4A2A"
                text f"Progress: {stirring_progress}%" size 16 color "#FFFFFF" xalign 0.5

                if stirring_complete:
                    text "Mixing Complete!" size 18 color "#4CAF50" xalign 0.5
                    textbutton "Finalize Mix" action [Function(mix_liquids, selected_container, selected_liquids), Hide("stirring_minigame")] style "inventory_button"

            else:
                 text "Select a tool to begin stirring." size 16 color "#AAAAAA" xalign 0.5

            null height 20
            textbutton "Cancel Mixing" action [Function(reset_stirring), Hide("stirring_minigame")] style "inventory_button" xalign 0.5


# --- Input Amount Screen ---
screen input_amount_screen(liquid):
    modal True
    frame:
        xsize 400
        ysize 200
        xalign 0.5
        yalign 0.5
        background "#1B3D1B"
        padding (20, 20)

        vbox:
            spacing 10
            text "Enter Amount to Add (ml):" size 20 color "#FFFFFF"

            # Input field for the amount
            input:
                id "amount_input"
                default ""
                length 5
                allow "0123456789"
                color "#FFFFFF"
                size 20

            hbox:
                spacing 20
                textbutton "Add":
                    action [
                        Function(add_liquid_to_selected, liquid, int(amount_input.value or 0)),
                        Hide("input_amount_screen")
                    ]
                textbutton "Cancel":
                    action Hide("input_amount_screen")

# --- Use Liquid Screen ---
screen use_liquid_screen():
    modal True
    frame:
        xsize 400
        ysize 400
        xalign 0.5
        yalign 0.5
        background "#113111"
        padding (20, 20)

        vbox:
            spacing 10
            label "Use Liquid" text_size 30 text_color "#FFFFFF"
            text "Select a liquid to use:" size 18 color "#FFFFFF"

            for liquid in inventory:
                if liquid["type"] == "liquid":
                    frame:
                        background "#1E4A1E"
                        padding (10, 10)
                        hbox:
                            text f"{liquid['name']} - {liquid['amount']}ml available" size 18 color "#FFFFFF"
                            textbutton "Use" action [Function(use_liquid, liquid), Hide("use_liquid_screen")] style "inventory_button"

            textbutton "Cancel" action Hide("use_liquid_screen") style "inventory_button" xalign 0.5


# --- --- --- CHARACTER STATUS --- --- ---
screen character_status_screen(player_obj):
    modal True
    tag status

    frame:
        style "section_frame"
        xysize (900, 700)
        xalign 0.5 yalign 0.5

        vbox:
            spacing 10
            text "Character Status" size 30 xalign 0.5 color "#FFFFFF"

            hbox:
                xalign 0.5 spacing 15
                textbutton "Body" action SetVariable("selected_tab", "Body") style "inventory_button" sensitive (selected_tab != "Body")
                textbutton "Stats" action SetVariable("selected_tab", "Stats") style "inventory_button" sensitive (selected_tab != "Stats")

            null height 15

            if selected_tab == "Body":
                python:
                    avg_health, avg_clean, avg_temp = player_obj.calculate_averages()
                text f"Overall: Health {avg_health}% | Cleanliness {avg_clean}% | Temp {avg_temp}°" size 18 xalign 0.5 color "#CCCCCC"

                viewport:
                    ysize 500
                    scrollbars "vertical" mousewheel True
                    grid 2 3:
                        spacing 15

                        for part, status_dict in player_obj.health.items():
                            frame:
                                style "section_frame"
                                background "#2E4F2E"
                                padding (10, 10, 10, 10)
                                vbox:
                                    spacing 5
                                    text part.replace("_", " ").title() size 18 color "#FFFF88"
                                    text f"Status: {status_dict.get('status', 'N/A')}" size 14
                                    text "Health:" size 14
                                    bar value status_dict.get('health', 0) range 100 xsize 150 left_bar "red" right_bar "#550000"
                                    text "Temp:" size 14
                                    bar value status_dict.get('temperature', 0) range 120 xsize 150 left_bar "orange" right_bar "#663300"
                                    text "Cleanliness:" size 14
                                    bar value status_dict.get('cleanliness', 0) range 100 xsize 150 left_bar "lightblue" right_bar "#003366"

                                    text "Conditions:" size 14
                                    if not status_dict.get('conditions'):
                                        text "- None -" size 12 color "#AAAAAA"
                                    else:
                                        for condition in status_dict.get('conditions'):
                                            text f"- {condition}" size 12 color "#FFAAAA"

                                    textbutton "Treat" action Show("medkit_screen", player_obj=player_obj, target_part=part) style "inventory_button" text_size 12 padding(5,2)

            elif selected_tab == "Stats":
                viewport:
                    ysize 500
                    scrollbars "vertical" mousewheel True
                    vbox:
                        spacing 15
                        for stat_name, data in player_obj.stats.items():
                            if stat_name == "sanity":
                                continue
                            frame:
                                style "section_frame"
                                background "#2E4F2E"
                                padding (10, 10, 10, 10)
                                hbox:
                                    spacing 10
                                    python:
                                        stat_img_path = "images/stats_icons/" + stat_name + ".png"
                                    if renpy.loadable(stat_img_path):
                                        add stat_img_path xysize (50, 50)
                                    else:
                                        frame style "stat_icon" background "#444444":
                                            xysize(50, 50)
                                            text stat_name[0].upper() size 30 xalign 0.5 yalign 0.5

                                    vbox:
                                        spacing 2
                                        text stat_name.title() size 18 color "#FFFF88"
                                        text f"Level: {data.get('level', 0)}" size 14
                                        text f"Value: {data.get('current_value', 0)}" size 14
                                        text "XP:" size 14
                                        bar value data.get('current_xp', 0) range data.get('max_xp', 100) xsize 200

                if "sanity" in player_obj.stats:
                    frame:
                        style "section_frame"
                        background "#2E4F2E"
                        padding (10, 10, 10, 10)
                        hbox:
                            spacing 10
                            python:
                                sanity_img_path = "images/stats_icons/sanity.png"
                            if renpy.loadable(sanity_img_path):
                                add sanity_img_path xysize (50, 50)
                            else:
                                frame style "stat_icon" background "#444444":
                                    xysize (50, 50)
                                    text "S" size 30 xalign 0.5 yalign 0.5

                            vbox:
                                text f"Sanity: {player_obj.stats['sanity'].get('current_sanity', 100)}%" size 18 color "#CCCCCC"
                                bar value player_obj.stats['sanity'].get('current_sanity', 100) range 100 xsize 250 left_bar "#AA00FF" right_bar "#330055"

            null height 15
            textbutton "Close Status" action Hide("status") style "inventory_button" xalign 0.5
   