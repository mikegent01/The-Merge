# Define styles to mimic the CSS
style scp_document_frame:
    background Solid("#ffffff")  # White paper background
    xpadding 40 ypadding 30
    xmaximum 800
    ymaximum 1000  # Limit the maximum height to prevent excessive scrollbar length
    align (0.5, 0.0)  # Center horizontally, align to top
    # Removed invalid duplicate background and outline; border simulated below

style scp_header_text:
    color "#000"
    size 24  # Slightly smaller to reduce overlapping
    bold True
    font "DejaVuSans.ttf"  # Default Ren'Py font; replace if needed

style scp_header_subtext:
    color "#555"
    size 12  # Slightly smaller
    font "DejaVuSans.ttf"
    kerning 2.0  # Use kerning to simulate letter-spacing

style scp_classification_box_outer:  # New style for outer border
    background Solid("#a00")
    padding (2, 2, 2, 2)
    align (1.0, 0.0)  # Align to top-right to avoid overlapping

style scp_classification_box_inner:
    background Solid("#ffffff")
    xpadding 10 ypadding 5

style scp_classification_text:
    color "#000"
    bold True
    size 12  # Smaller

style scp_classification_level:
    color "#a00"
    size 16  # Smaller
    bold True

style scp_memo_title:
    color "#000"
    size 20  # Smaller
    bold True
    align (0.5, 0.5)

style scp_memo_meta_outer:  # New for meta border simulation
    background Solid("#eee")
    padding (1, 1, 1, 1)

style scp_memo_meta_inner:
    background Solid("#f9f9f9")
    xpadding 15 ypadding 10
    size 14

style scp_content_text:
    color "#333"
    size 14  # Smaller to prevent overlapping
    justify True  # Mimics text-align: justify
    hover_color "#000"  # Change color on hover to simulate "selectability"

style scp_footer_text:
    color "#777"
    size 10  # Smaller
style image_security_code_text:
    color "#777"
    size 10  # Smaller
    align (0.4, 0.4)
style scp_divider:
    background Solid("#ccc")
    ysize 1
    xfill True
    ymargin 20

style scp_content_divider:
    background Solid("#eee")
    ysize 1
    xfill True
    ymargin 15

style scp_viewport_inner_frame:
    background None  # Transparent background
    xpadding 20 ypadding 20

# Screen definition
screen scp_memo():
    frame:
        style "scp_document_frame"
        viewport:
            yadjustment ui.adjustment()  # Directly use ui.adjustment() for scrolling
            mousewheel True  # Allows scrolling with mouse wheel
            scrollbars "vertical"  # Shows a vertical scrollbar
            ysize 900  # Set a fixed height for the viewport to control scrollbar length (adjust as needed)

            # Inner frame for padding
            frame:
                style "scp_viewport_inner_frame"

                # Main content vbox with extra spacing
                vbox:
                    spacing 20  # Increased spacing to prevent overlapping

                    # Simulate thick top border with a black bar at the top
                    fixed:
                        ysize 5
                        xfill True
                        add Solid("#000")

                    # SCP Header
                    hbox:
                        spacing 20
                        yalign 0.0  # Align to top to prevent vertical overlapping

                        # Logo (made smaller: reduced fixed size and zoom)
                        fixed:
                            xsize 40 ysize 40  # Smaller container
                            align (0.5, 0.0)  # Align to top
                            add "images/news/SCP_Foundation_(emblem).svg" at truecenter:  # Adjust path if needed
                                xzoom 0.1 yzoom 0.1  # Smaller scale (adjust as needed)

                        # Header Text
                        vbox:
                            xfill True
                            yalign 0.0  # Align to top
                            spacing 5  # Space between header lines
                            text "SCP FOUNDATION" style "scp_header_text"
                            text "SECURE. CONTAIN. PROTECT." style "scp_header_subtext"

                        # Classification Box (simulated border)
                        frame style "scp_classification_box_outer":
                            frame style "scp_classification_box_inner":
                                vbox:
                                    spacing 3  # Space inside classification box
                                    text "[ 'LEVEL 3 CLEARANCE REQUIRED'.upper() ]" style "scp_classification_text"
                                    text "[ 'CLASSIFIED'.upper() ]" style "scp_classification_level"

                    # Divider
                    null style "scp_divider"

                    # Letter Content
                    vbox:
                        spacing 15  # Increased spacing

                        text "[ 'INTERNAL MEMORANDUM #0001'.upper() ]" style "scp_memo_title"

                        # Memo Meta (simulated border)
                        frame style "scp_memo_meta_outer":
                            frame style "scp_memo_meta_inner":
                                vbox:
                                    spacing 5  # Space between meta lines
                                    text "{b}Date:{/b} ██████████" style "scp_content_text"
                                    text "{b}From:{/b} O5-██ / Dir. B█████" style "scp_content_text"
                                    text "{b}To:{/b} Site Director REDACTED, Alpha-1 Lead" style "scp_content_text"
                                    text "{b}Subject:{/b} Anomaly Survey - Operation REDACTED" style "scp_content_text"

                        null style "scp_content_divider"

                        text "When this memorandum is received and acknowledged, standard data sanitization protocols apply. Destroy physical copies after digital confirmation." style "scp_content_text"
                        text "Stabilization efforts appear successful following initial containment. Primary anomaly source confirmed at coordinates X██.Y████, Z██.A████. Entity designation pending, it exhibits reality-bending properties of significant magnitude, though containment appears feasible. You will lead Mobile Task Force Alpha-1 (\"Red Right Hand\") designation pending to conduct thorough reconnaissance of the affected area. Gather all available data on entity behavior, properties, and local environmental effects. If the entity becomes aware of MTF presence, immediately initiate Protocol Chimera-Gamma as outlined in Addendum 0001-A (Ref: Doc ███-██). Do {b}NOT{/b} deviate." style "scp_content_text"
                        text "Standing orders from O5 Command explicitly forbid direct interaction with the anomaly at this stage. Continuous passive surveillance is authorized until further notice or issuance of an engagement order. Prioritize personnel safety and data integrity." style "scp_content_text"
                        text "Attached is the final image transmitted by Exploration Team Bravo-2 prior to signal loss. Recover their data packet; its contents are considered critical intelligence. Deliver recovered materials directly to Site-19 secure archives upon return." style "scp_content_text"

                        # Attached Image with rotation and hover effect (uncommented and adjusted)
                        null height 25  # Simulate top margin
                        frame:
                            xalign 0.5
                            background Frame(Solid("#fdfdfd"), Borders(5, 5, 5, 5), tile=False)
                            add Transform("images/news/house.png", rotate=-1.5, zoom=0.3)
                            hover_background Frame(Solid("#fdfdfd"), Borders(5, 5, 5, 5), tile=False)  # If needed for hover

                    # Footer with extra margin
                    text "Image Security Code: 51856." style "image_security_code_text"
                    null height 30  # Add space before footer
                    textbutton "Close" action [ Hide("scp_memo")] 
                    
                    null height 20  # Padding at the bottom to shorten scrollbar
                    fixed:
                        ysize 5
                        xfill True
                        add Solid("#000")
                    text "Document 001-M-0001 - Property of the SCP Foundation & DOD - Unauthorized Access Prohibited" style "scp_footer_text"
