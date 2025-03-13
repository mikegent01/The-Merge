screen HUD():
    key ["j", "J"] action Show("journal_screen")
    
    # Add background overlay image at bottom middle
    add "images/bg/overlay/bg overlay.png":
        xalign 0.5
        yalign 1.0
       # #zorder 0
    
    # Backpack Icon - Left side
   # if inventory:
    imagebutton:
        xalign 0.66
        yalign 0.87
        idle "images/inventory/inventory_hud/backpack.png"
        hover "images/inventory/inventory_hud/backpack_hover.png"
        action Show("inventory")
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
        action Show("journal_screen")
        padding (10, 10, 10, 10)                   
        #oomfie
    text "Benjamin":
        xalign 0.31
        yalign 0.81
        size 30
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
        ysize 600
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

# The updated journal screen with save-specific variables
screen journal_screen():
    default current_tab = "Missions"
    frame:
        align (0.5, 0.5)
        xsize 800
        ysize 600
       # background "gui/frame.png"
        
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
                textbutton "Close" action Hide("journal_screen") 

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
                        
                        if len(missions["completed"]) > 0:
                            for mission in missions["completed"]:
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
                        
                        if len(unlocked_books) > 0:
                            for book in unlocked_books:
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
                                            textbutton "Read" action Show("read_book_screen", book=book)
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
                        
                        if len(journal_entries) > 0:
                            for entry in reversed(journal_entries):  # Show newest first
                                frame:
                                    xfill True
                                    background "#00000033"
                                    
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

screen region_highlight():
    frame:
        background "#00000088"
        xfill True
        yfill True
        
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            
            text "Search Area":
                xalign 0.5
                color "#ffffff"
                size 40
                outlines [(2, "#000000", 0, 0)]
            
            hbox:
                spacing 20
                xalign 0.5
                
                textbutton "Top":
                    xsize 150
                    ysize 80
                    text_size 24
                    action [SetVariable("searched_area", "top"), Hide("area_search_buttons"), Jump(last_label)]
                
                textbutton "Middle":
                    xsize 150
                    ysize 80
                    text_size 24
                    action [SetVariable("searched_area", "middle"), Hide("area_search_buttons"), Jump(last_label)]
                
                textbutton "Bottom":
                    xsize 150
                    ysize 80
                    text_size 24
                    action [SetVariable("searched_area", "bottom"), Hide("area_search_buttons"), Jump(last_label)]
            
            hbox:
                spacing 20
                xalign 0.5
                
                textbutton "Left":
                    xsize 150
                    ysize 80
                    text_size 24
                    action [SetVariable("searched_area", "left"), Hide("area_search_buttons"), Jump(last_label)]
                
                textbutton "Center":
                    xsize 150
                    ysize 80
                    text_size 24
                    action [SetVariable("searched_area", "center"), Hide("area_search_buttons"), Jump(last_label)]
                
                textbutton "Right":
                    xsize 150
                    ysize 80
                    text_size 24
                    action [SetVariable("searched_area", "right"), Hide("area_search_buttons"), Jump(last_label)]
                    
            # Cancel button
            textbutton "Cancel":
                xalign 0.5
                xsize 150
                ysize 60
                text_size 24
                action [SetVariable("searched_area", None), Hide("area_search_buttons"), Jump(last_label)]
