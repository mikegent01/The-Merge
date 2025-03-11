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
                idle "images/inventory/inventory_hud/backpack.png"
                hover "images/inventory/inventory_hud/backpack_hover.png"
                action Show("inventory")
                padding (10, 10, 10, 10)

        # Health Icon
        imagebutton:
            idle "images/inventory/inventory_hud/meidc_hud.png"
            hover "images/inventory/inventory_hud/medic_hover.png"
            action Show("status_screen")
            padding (10, 10, 10, 10)

        # Quest Log Icon
        imagebutton:
            idle "images/inventory/inventory_hud/Quest_Log.png"
            hover "images/inventory/inventory_hud/Quest_Log_hover.png"
            action Show("journal_screen")
            padding (10, 10, 10, 10)

        # Head Log Icon
        imagebutton:
            idle "images/inventory/inventory_hud/head.png"
            hover "images/inventory/inventory_hud/head_hover.png"
            action Show("player_stats_screen")
            padding (10, 10, 10, 10)
screen journal_screen():
    default current_tab = "Missions"
    
    # Safety check to ensure persistent variables exist
    python:
        if persistent.unlocked_books is None:
            persistent.unlocked_books = []
        
        if persistent.missions is None:
            persistent.missions = {"active": [], "completed": []}
        
        if persistent.journal_entries is None:
            persistent.journal_entries = []
    
    frame:
        align (0.5, 0.5)
        xsize 800
        ysize 600
      #  background "gui/frame.png"
        
        vbox:
            spacing 10
            xalign 0.5
            xfill True
            
            text "Journal" size 40
            
            hbox:
                spacing 20
                textbutton "Missions" action SetScreenVariable("current_tab", "Missions")
                textbutton "Books" action SetScreenVariable("current_tab", "Books")
                textbutton "Journal" action SetScreenVariable("current_tab", "Journal")
            
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
                        
                        if len(persistent.missions["active"]) > 0:
                            for mission in persistent.missions["active"]:
                                frame:
                                    xfill True
                                    background "#3333"
                                    
                                    vbox:
                                        spacing 5
                                        text mission["title"] size 22 color "#ff9"
                                        text mission["description"] size 18
                                        
                                        if mission["objectives"]:
                                            vbox:
                                                for objective in mission["objectives"]:
                                                    text "• [objective]" size 16
                                        
                                        bar value mission["progress"] range 100 xfill True
                        else:
                            text "No active missions." size 20
                        
                        text "Completed Missions:" size 25
                        
                        if len(persistent.missions["completed"]) > 0:
                            for mission in persistent.missions["completed"]:
                                frame:
                                    xfill True
                                    background "#3333"
                                    
                                    vbox:
                                        spacing 5
                                        text mission["title"] size 22 color "#9f9"
                                        text mission["description"] size 18
                        else:
                            text "No completed missions." size 20
            
            # BOOKS TAB
            elif current_tab == "Books":
                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    xfill True
                    yfill True
                    
                    vbox:
                        spacing 15
                        
                        text "Available Books:" size 30
                        
                        if len(persistent.unlocked_books) > 0:
                            for book in persistent.unlocked_books:
                                frame:
                                    xfill True
                                    background "#3333"
                                    
                                    hbox:
                                        spacing 10
                                        
                                        # Try to use the image if it exists, otherwise use text fallback
                                        if renpy.loadable(book["preview"]):
                                            imagebutton:
                                                idle book["preview"]
                                                hover book["preview"]
                                                action Show("read_book_screen", book=book)
                                                tooltip "Click to read the book"
                                                xsize 100
                                                ysize 150
                                        else:
                                            frame:
                                                xsize 100
                                                ysize 150
                                                background "#7777"
                                                textbutton "[book['title']]":
                                                    action Show("read_book_screen", book=book)
                                                    xalign 0.5
                                                    yalign 0.5
                                                    text_size 14
                                                    tooltip "Click to read the book"
                                        
                                        vbox:
                                            yalign 0.5
                                            text book["title"] size 20
                                            text "Unlocked: [book['date_unlocked']]" size 16
                                            textbutton "Read" action Show("read_book_screen", book=book), Hide("journal_screen")
                        else:
                            text "No books have been discovered yet." size 20
            
            # JOURNAL TAB
            elif current_tab == "Journal":
                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    xfill True
                    yfill True
                    
                    vbox:
                        spacing 15
                        
                        if len(persistent.journal_entries) > 0:
                            for entry in reversed(persistent.journal_entries):  # Show newest first
                                frame:
                                    xfill True
                                    background "#3333"
                                    
                                    vbox:
                                        spacing 5
                                        hbox:
                                            text entry["title"] size 22 color "#9ff"
                                            null width 20
                                            text entry["date"] size 16 xalign 1.0
                                        
                                        text entry["content"] size 18
                        else:
                            text "Your journal is empty. Record your thoughts and discoveries here." size 20
            
            textbutton "Close" action Hide("journal_screen") align (0.5, 1.0)
screen read_book_screen(book):
    default current_page = 0
    default pages = load_book_text(book["text_file"])
    default total_pages = len(pages)
    
    modal True
    
    frame:
        align (0.5, 0.5)
        xsize 800
        ysize 600
        #background "gui/frame.png"
        
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