screen stagecurtians():
    add "images/bg/overlay/floor.png" size (config.screen_width, config.screen_height)
   #add "images/bg/overlay/background.png" size (config.screen_width, config.screen_height)
    add "images/bg/overlay/stage.png" size (config.screen_width, config.screen_height)
 

screen HUD():
    key ["j", "J"] action Show("journal_screen")
    add "images/bg/overlay/bg overlay.png":
        xalign 0.5
        yalign 1.0
    
   # if inventory:
    imagebutton:
        xalign 0.66
        yalign 0.87
        idle "images/inventory/inventory_hud/backpack.png"
        hover "images/inventory/inventory_hud/backpack_hover.png"
        action Show("inventory")
        padding (10, 10, 10, 10)
    imagebutton:
        xalign 0.66
        yalign 1.0
        idle "images/inventory/inventory_hud/speechbubble.png"
        hover "images/inventory/inventory_hud/speechbubble_hover.png"
        action Show("speak_to_people")
        padding (10, 10, 10, 10)        
    imagebutton:
        xalign 0.755
        yalign 0.87
        idle "images/inventory/inventory_hud/Quest_Log.png"
        hover "images/inventory/inventory_hud/Quest_Log_hover.png"
        action Show("journal_screen")
        padding (10, 10, 10, 10)     
    imagebutton:
        xalign 0.755
        yalign 1.0
        idle "images/inventory/inventory_hud/magna.png"
        hover "images/inventory/inventory_hud/magna_hover.png"
        action Show("dynamic_text_screen")
        padding (10, 10, 10, 10)                   
        #oomfie
    text "Benjamin [benx], [beny]":
        xalign 0.31
        yalign 0.81
        size 30
        color "#59ff00"
        outlines [(2, "#000000", 0, 0)]
    text "Mouse: [renpy.get_mouse_pos()]":
        xalign 0.31
        yalign 0.84
        size 20
        color "#59ff00"
        outlines [(2, "#000000", 0, 0)]
    # Health Icon - Right side
    imagebutton:
        xalign 0.565
        yalign 0.87
        idle "images/inventory/inventory_hud/meidc_hud.png"
        hover "images/inventory/inventory_hud/medic_hover.png"
        action Show("status_screen") #status_screen 
        padding (10, 10, 10, 10)

    # Head Log Icon - Bottom center
    imagebutton:
        xalign 0.31
        yalign 1.0
        idle "images/inventory/inventory_hud/head.png"
        hover "images/inventory/inventory_hud/head_hover.png"
        action Show("player_stats_screen")
        padding (10, 10, 10, 10)
screen read_book_screen(book):
    default current_page = 0
    default pages = load_book_text(book["text_file"])
    default total_pages = len(pages)
    
    modal True
    
    frame:
        align (0.5, 0.5)
        xsize 800
        ysize 500
     #   background "gui/frame.png"
        
        vbox:
            spacing 10
            xfill True
            yfill True
            
            text book["title"] size 40 xalign 0.5
            
            # Page content
            frame:
                background "#000000ff"
                xfill True
                yfill True
                margin (20, 20)
                
                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    xfill True
                    yfill True
                    
                    text pages[current_page] size 20 line_spacing 5
            
            # Navigation
            hbox:
                spacing 20
                xalign 0.5
                
                textbutton "Previous Page" action SetScreenVariable("current_page", max(0, current_page - 1)) sensitive current_page > 0
                text "Page [current_page + 1] of [total_pages]" size 18
                textbutton "Next Page" action SetScreenVariable("current_page", min(total_pages - 1, current_page + 1)) sensitive current_page < total_pages - 1
                
                null width 50
                
                textbutton "Close" action Hide("read_book_screen") 

screen tutorial_screen():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xsize 700
        padding (30, 30)
        
        vbox:
            spacing 15
            text "TUTORIAL [last_label]" xalign 0.5 color "#ff9900" size 36
            
            null height 10
            
            text "Welcome to Action Mode!" size 28 xalign 0.5
            
            null height 5
            
            text "In this mode, you can interact with the environment and characters:" size 22
            
            null height 10
            
            hbox:
                spacing 20
                xalign 0.5
                
                vbox:
                    xsize 300
                    spacing 10
                    
                    text "• Press yourself for your Stats Screen" 
                    text "• Medkit button shows your Health Status"
                    text "• Backpack opens your Inventory"
                    text "• Clipboard reveals your Journal"
                
                vbox:
                    xsize 300
                    spacing 10
                    
                    text "• Magnifying Glass lets you Search the Area"
                    text "• Speech Bubble initiates Conversation"
                    text "• Weapon button is for Escalation (initiates battles or debates)"
            
            null height 20
                  
            textbutton "Got it!" xalign 0.5 action [SetVariable("tutorial_shown", True), Hide("tutorial_screen")]                            
# The updated journal screen with save-specific variables and Tapes tab
screen journal_screen():
    default current_tab = "Missions"

    # It's good practice to ensure the audio channel used for tapes is stopped when the screen is hidden.
    on "hide" action Stop("voice") # Using the "voice" channel for tapes, adjust if needed

    frame:
        align (0.5, 0.5)
        xsize 800
        ysize 600
       # background "gui/frame.png" # Uncomment if you have this background

        vbox:
            spacing 10
            xalign 0.5
            xfill True

            text "Journal" size 40 align (0.5, 0) # Centered title

            hbox: # Navigation tabs
                style_prefix "journal_nav" # Apply a style prefix if needed
                xalign 0.5 # Center the navigation buttons
                spacing 20

                textbutton "Missions" action SetScreenVariable("current_tab", "Missions")
                textbutton "Books" action SetScreenVariable("current_tab", "Books")
                textbutton "Journal" action SetScreenVariable("current_tab", "Journal")
                textbutton "Tapes" action SetScreenVariable("current_tab", "Tapes") # <--- ADDED Tapes button
                textbutton "Close" action [Stop("voice"), Hide("journal_screen")] # Stop tape audio on close

            # MISSIONS TAB
            if current_tab == "Missions":
                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    xfill True
                    yfill True

                    vbox:
                        spacing 20
                  

                        text "Active Missions:" size 25

                        if len(missions["active"]) > 0:
                            for mission in missions["active"]:
                                frame:
                                    xfill True
                                    background "#33333388" # Slightly darker background
                                    padding (10, 10) # Add padding inside mission frame

                                    vbox:
                                        spacing 5
                                        text mission["title"] size 22 color "#ffff99" # Yellowish for active title
                                        text mission["description"] size 18

                                        if mission.get("objectives"): # Use .get() for safer access
                                            vbox:
                                                spacing 3
                                                for objective in mission["objectives"]:
                                                    # Ensure objective is a string before displaying
                                                    $ objective_text = str(objective)
                                                    text "• [objective_text]" size 16
                                        else:
                                            pass # No objectives to show

                                        # Ensure progress is present and valid
                                        if mission.get("progress") is not None:
                                            bar value mission["progress"] range 100  
                        else:
                            text "No active missions." size 20 align (0.5, 0)

                        # Add spacing between sections
                        null height 20

                        text "Completed Missions:" size 25

                        if len(missions["completed"]) > 0:
                            for mission in missions["completed"]:
                                frame:
                                    xfill True
                                    background "#33333388" # Consistent background
                                    padding (10, 10) # Add padding

                                    vbox:
                                        spacing 5
                                        text mission["title"] size 22 color "#99ff99" # Greenish for completed title
                                        text mission["description"] size 18
                        else:
                            text "No completed missions." size 20 align (0.5, 0)

            # BOOKS TAB
            elif current_tab == "Books":
                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    xfill True
                    yfill True

                    vbox:
                        spacing 15


                        text "Available Books:" size 30 align (0.5, 0)

                        if len(unlocked_books) > 0:
                            # Maybe use a grid for books if many previews? Or stick to list.
                            for book in unlocked_books:
                                frame:
                                    xfill True
                                    background "#33333388"
                                    padding (10, 10)

                                    hbox:
                                        spacing 15 # Increased spacing

                                        # Try to use the image if it exists, otherwise use text fallback
                                        $ preview_path = book.get("preview", "") # Safer access
                                        if preview_path and renpy.loadable(preview_path):
                                            imagebutton:
                                                idle preview_path
                                                hover preview_path # Add a hover effect if you have one
                                                action Show("read_book_screen", book=book, transition=dissolve)
                                                tooltip "Click to read '[book['title']]'"
                                                xysize (100, 150) # Use xysize for fixed size
                                        else:
                                            # Fallback frame
                                            frame:
                                                xysize (100, 150)
                                                background "#777777cc" # Darker fallback
                                                has vbox xalign 0.5 yalign 0.5
                                                text "[book.get('title', 'Unknown Book')]" size 14 align (0.5, 0.5)
                                                textbutton "Read": # Add fallback button here too
                                                    action Show("read_book_screen", book=book, transition=dissolve)
                                                    xalign 0.5
                                                    yalign 0.8 # Position near bottom
                                                    tooltip "Click to read '[book['title']]'"


                                        vbox:
                                            yalign 0.5
                                            spacing 5
                                            text book.get("title", "Unknown Title") size 20 # Use .get for safety
                                            if book.get("date_unlocked"):
                                                text "Unlocked: [book['date_unlocked']]" size 16
                                            # "Read" button is clear and accessible
                                            textbutton "Read Book" action Show("read_book_screen", book=book, transition=dissolve)

                        else:
                            text "No books have been discovered yet." size 20 align (0.5, 0)

            # JOURNAL TAB
            elif current_tab == "Journal":
                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    xfill True
                    yfill True

                    vbox:
                        spacing 15
   

                        text "Personal Entries:" size 30 align(0.5, 0) # Title

                        if len(journal_entries) > 0:
                            # Iterate through reversed for newest first
                            for entry in reversed(journal_entries):
                                frame:
                                    xfill True
                                    background "#00000044" # Slightly different background maybe?
                                    padding (10, 10)

                                    vbox:
                                        spacing 8
                                        hbox: # Title and Date on one line
                                            text entry.get("title", "Entry") size 22 color "#99ffff" # Cyan title
                                            null width 20 # Spacer
                                            text entry.get("date", "") size 16 xalign 1.0 # Align date to the right

                                        text entry.get("content", "") size 18
                        else:
                            text "Your journal is empty. Record your thoughts and discoveries here." size 20 align (0.5, 0)

            # TAPES TAB <-------------------- NEW TAB CONTENT --------------------->
            elif current_tab == "Tapes":
                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    xfill True
                    yfill True

                    vbox:
                        spacing 15

                        text "Collected Tapes:" size 30 align(0.5, 0)

                        if len(collected_tapes) > 0:
                            for tape in collected_tapes:
                                frame:
                                    xfill True
                                    background "#33333388" # Consistent background
                                    padding (10, 10)

                                    hbox: # Use hbox for side-by-side layout
                                        spacing 15
                                        # Left side: Info
                                        vbox:
                                            spacing 5
                                            text tape.get("title", "Untitled Tape") size 20 color "#FFA500" # Orange-ish title
                                            if tape.get("description"):
                                                text tape["description"] size 16
                                            if tape.get("date_found"):
                                                text "Found: [tape['date_found']]" size 14 italic True color "#ccc"

                                        # Right side: Play button (aligned to the right)
                                        null width 20 # Spacer
                                        vbox: # Use vbox to align button vertically if needed
                                            yalign 0.5 # Center vertically in the hbox
                                            # The action list stops previous tape on the 'voice' channel, then plays the new one.
                                            textbutton "▶ Play" action [Stop("voice"), Play("voice", tape["audio_file"])]

                        else:
                            text "No audio tapes found yet." size 20 align (0.5, 0)
