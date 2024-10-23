screen room_view():
    # Display the buttons using the functions defined above for organized text handling
    textbutton "Search the left area." action Show("look", get_left_area_text()) xpos 0 ypos 150
    textbutton "Search the right area." action Show("look", get_right_area_text()) xpos 880 ypos 150
    textbutton "Look up." action Show("look", get_look_up_text()) xpos 500 ypos 20
    textbutton "Look down." action Show("look", get_look_down_text()) xpos 500 ypos 700
    textbutton "Search the far left area." action Show("look", get_far_left_area_text()) xpos 100 ypos 250
    textbutton "Search the far right area." action Show("look", get_far_right_area_text()) xpos 800 ypos 250
