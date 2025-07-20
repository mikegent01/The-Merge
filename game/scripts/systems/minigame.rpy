# --- Minigame - Math Problem ---
default minigame_active = False
default minigame_time = 10
default minigame_problem = ""
default minigame_answer = 0
default minigame_bonus = 0
default player_answer = ""
default mixing_steps = ["top", "right", "bottom", "left"]
label gameover:
    "You have died..."
    "Why don't you try loading a save..."
label minigame:
    # Initialize mini-game variables
    $ minigame_time = 10
    $ minigame_active = True
    $ minigame_problem = generate_problem()  # Replace with your problem generation logic

    # Mini-game loop
    while minigame_time > -1:
        # Display the mini-game screen
        call screen minigame_screen

        # Decrease the timer
        $ minigame_time -= 1

        # Check if the mini-game should end
        if minigame_time == 0:
            $ minigame_active = False
            hide screen minigame_screen

    # End of mini-game
    return

init python:
  # --- Math Minigame ---
    def start_minigame():
        global minigame_time, minigame_active, minigame_problem, minigame_answer, player_answer
        minigame_time, minigame_active = 10, True
        minigame_problem, minigame_answer = generate_problem()
        player_answer = ""
    def check_minigame_answer():
        global minigame_active, minigame_bonus, player_answer
        if player_answer.isdigit() and int(player_answer) == minigame_answer:
            minigame_bonus += 1; renpy.notify("Correct! Well done.")
        else:
            minigame_bonus -= 1; renpy.notify(f"The correct answer was {minigame_answer}.")
        start_minigame() # Next round
    def generate_problem():
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
        if random.choice(["add", "mul"]) == "add": return f"{num1} + {num2}", num1 + num2
        else: return f"{num1} * {num2}", num1 * num2