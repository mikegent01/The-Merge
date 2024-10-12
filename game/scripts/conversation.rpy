screen conversation_screen():
    tag conversation_screen

    # NPC info (name, mood, attitude)
    frame:
        align (0.75, 0.08)
        xsize 250
        vbox:
            text "[npc_name]" size 24
            text "Mood: [npc_mood]" size 16
            text "Feeling: [npc_attitude]" size 16

