from gui import *

# Main window
with dpg.window(tag="Root"):
    # Logo
    with dpg.group(horizontal=True, width=-1):
        logo("Wordle.py")

    dpg.add_separator(), dpg.add_spacer(height=10)

    # Keyboard layout
    keyboard_layout = [
        ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
        ["ENTER", "Z", "X", "C", "V", "B", "N", "M", "DEL"]
    ]

    # Create Tiles module
    for row in range(ROWS):
        with dpg.group(horizontal=True, width=0):
            dpg.add_spacer(width=(500 - COLS * 70) / 2)
            for column in range(COLS):
                tile("", tag=f"#{row * COLS + column}_key")

    dpg.add_spacer(height=32)

    # Create keyboard module
    for row_index, row in enumerate(keyboard_layout):
        with dpg.group(horizontal=True):
            num_buttons = len(row)
            if row_index == 2:
                spacer_width = (500 - num_buttons * 55) / 2
            else:
                spacer_width = (500 - num_buttons * 50) / 2

            dpg.add_spacer(width=spacer_width)

            for key in row:
                if key == "ENTER":
                    keyboard_action(
                        key + " ", callback=wordle_game.enter_key_button)
                elif key == "DEL":
                    keyboard_action(
                        key, callback=wordle_game.del_key_button)
                else:
                    keyboard(key)

    dpg.add_spacer(height=5), dpg.add_separator()

    with dpg.group(horizontal=True):
        dpg.add_spacer(width=(500 - 1 * 75) / 2)
        hyperlink("<Github>", "https://github.com/j-zunino/Wordle.py")

    with dpg.group(tag="#error_popup_group"):
        error_popup(f"Error popup", pos=[230, -50], tag="error_popup")

# Keyboard handle
with dpg.handler_registry():
    dpg.add_key_press_handler(callback=wordle_game.key_press_handler)


dpg.set_primary_window("Root", True)
dpg.create_viewport(title="Wordle.py", width=WIDTH, height=HEIGHT, resizable=False,
                    small_icon="./appicon.ico", large_icon="./appicon.ico")
dpg.show_viewport()
dpg.setup_dearpygui()
dpg.start_dearpygui()
dpg.destroy_context()
