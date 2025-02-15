screen library_interface():
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30
        xsize 1200
        
        vbox:
            spacing 10
            label _("Floor [current_floor]  Shelf [current_shelf]  Book [current_book]  Page [current_page]") xalign 0.5
            
            # Search UI
            hbox:
                spacing 10
                input:
                    value VariableInputValue("search_query")
                    xsize 600
                    placeholder "Enter search phrase..."
                textbutton _("Search") action [
                    If(
                        search_query.strip(),
                        [
                            SetVariable("search_results", []),
                            SetVariable("highlight_position", (-1, -1)),
                            Function(bs.search_history.appendleft, search_query),
                            Show("search_loading")
                        ],
                        None
                    )
                ]
                textbutton _("Search History") action Show("search_history_popup")
            
            # Navigation controls
            hbox:
                spacing 40
                # ... (keep existing navigation controls from previous version)
            
            # Page display with highlighting
            frame:
                xsize 1100
                ysize 600
                background Solid("#ffffff20")
                viewport:
                    draggable True
                    mousewheel True
                    scrollbars "vertical"
                    text self.format_highlighted_text():
                        size 16
                        color "#000000"
                        outlines [ (1, "#ffffff", 0, 0) ]
            
            textbutton _("Exit Library") action Hide("library_interface") xalign 0.5
    
    # Show loading indicator during search
    if renpy.get_screen("search_loading"):
        add "gui/loading.png" align (0.5, 0.5) at spin
    
    method format_highlighted_text(self):
        page_text = generate_page(current_floor, current_shelf, current_book, current_page)
        if highlight_position[0] != -1:
            start, end = highlight_position
            return (
                page_text[:start] +
                "{color=#ff0000}" + page_text[start:end] + "{/color}" +
                page_text[end:]
            )
        return page_text

screen search_loading():
    timer 0.1 action [
        Hide("search_loading"),
        Function(perform_search, search_query),
    ]

screen search_history_popup():
    frame:
        xalign 0.5
        yalign 0.3
        vbox:
            label "Search History"
            for query in bs.search_history:
                textbutton query:
                    action [
                        SetVariable("search_query", query),
                        Show("search_loading"),
                        Hide("search_history_popup")
                    ]