init python:
    # --- Mixing & Stirring Minigame State ---
    # Stirring
    stirring_tool = None
    stirring_progress = 0
    stirring_complete = False
    last_mouse_pos = (0, 0)
    stirring_direction = None
    stirring_count = 0
    # Mixing
    is_mixing = False
    mixing_progress = 0
    current_mixing_step = 0
    mixing_attempts = 0
    def update_stirring_progress():
        global stirring_progress, last_mouse_pos, stirring_direction, stirring_count, stirring_complete
        current_mouse_pos = renpy.get_mouse_pos()
        if last_mouse_pos != (0, 0):
            dx = current_mouse_pos[0] - last_mouse_pos[0]; dy = current_mouse_pos[1] - last_mouse_pos[1]
            if abs(dx) > abs(dy): new_direction = "right" if dx > 0 else "left"
            else: new_direction = "down" if dy > 0 else "up"
            if stirring_direction and \
               ((stirring_direction, new_direction) in [("right", "down"), ("down", "left"), ("left", "up"), ("up", "right")]):
                stirring_count += 1
                if stirring_count >= 4:
                    stirring_progress += 10; stirring_count = 0
                    if stirring_progress >= 100:
                        stirring_progress = 100; stirring_complete = True; renpy.notify("Stirring complete!")
                        mix_liquids(selected_container, selected_liquids)
            stirring_direction = new_direction
        last_mouse_pos = current_mouse_pos

    def reset_stirring():
        global stirring_tool, stirring_progress, stirring_complete, last_mouse_pos, stirring_direction, stirring_count
        stirring_tool, stirring_progress, stirring_complete = None, 0, False
        last_mouse_pos, stirring_direction, stirring_count = (0, 0), None, 0

    def handle_mixing_click(direction):
        global current_mixing_step, mixing_attempts
        if direction == mixing_steps[current_mixing_step]:
            current_mixing_step += 1
            if current_mixing_step >= len(mixing_steps):
                current_mixing_step = 0; mixing_attempts += 1
                if mixing_attempts >= 2:
                    renpy.notify("Mixing complete!"); mix_liquids(selected_container, selected_liquids); reset_mixing()
                else:
                    renpy.notify(f"Step {mixing_attempts + 1}: Continue mixing!")
        else:
            renpy.notify("Wrong direction! Start over."); reset_mixing()

    def reset_mixing():
        global current_mixing_step, mixing_attempts
        current_mixing_step, mixing_attempts = 0, 0

    def handle_mixing_motion():
        global mixing_progress, is_mixing
        if is_mixing:
            mixing_progress += renpy.random.randint(1, 3)
            if mixing_progress >= 100:
                mixing_progress = 100; is_mixing = False; renpy.notify("Mixing complete!")
                mix_liquids(selected_container, selected_liquids)
