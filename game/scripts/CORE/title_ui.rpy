init python:
    title_screen_set = False

    # --- Title Screen Data ---
    title_screens = [
        {"image": "images/bg/Title Screen/Title_Screen.png", "music": ["audio/Music/showtime.mp3"]},
        {"image": "images/bg/Title Screen/Titlescreen2.png", "music": ["audio/Music/openingact.mp3", "audio/Music/creep.mp3"]},
        {"image": "images/bg/Title Screen/alternatetitleone.png", "music": ["audio/Music/sock.mp3", "audio/Music/Introsong.wav"]},
        {"image": "images/bg/Title Screen/detailedtitle.png", "music": ["audio/Music/IntroTheme3.mp3", "audio/Music/IntroTheme1.mp3", "audio/Music/openingactone.mp3"]}
    ]
    selected_screen = random.choice(title_screens)
    def set_random_title_screen():
        global title_screen_set
        if not title_screen_set:
            title_screen_set = True
            play_title_screen_music(selected_screen)
        return selected_screen["image"]

    def play_title_screen_music(selected_screen):
        if "music" in selected_screen and selected_screen["music"]:
            renpy.music.play(random.choice(selected_screen["music"]), loop=True)

       