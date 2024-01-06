import dearpygui.dearpygui as dpg
import webbrowser
from functions import *
from themes import setup_themes

# To-do: 1. Loose state, 2. Custom error pop up whit dearpygui_animate.

dpg.create_context()

setup_themes()
wordle_game.pick_word()


# Fonts
with dpg.font_registry():
    main_font = dpg.add_font("src/fonts/libre_franklin/LibreFranklin-Black.ttf", 40)
    link_font = dpg.add_font("src/fonts/libre_franklin/LibreFranklin-semibold.ttf", 15)

    keyboard_font = dpg.add_font("src/fonts/libre_franklin/LibreFranklin-Bold.ttf", 20)
    keyboard_action_font = dpg.add_font("src/fonts/libre_franklin/LibreFranklin-Bold.ttf", 15)

    logo_font = dpg.add_font("src/fonts/bevan/Bevan-Regular.ttf", 50)

# Logo
def _logo(text):
    logo = dpg.add_button(label=text, tag="#logo", width=300, height=50, callback=wordle_game.restart)
    dpg.bind_item_theme(logo, "_logo_theme")
    dpg.bind_item_font(logo,logo_font)

# letter row theme
def _letter_row(text, tag):
    button_row = dpg.add_button(label=text, width=62, height=62, tag=tag)
    dpg.bind_item_theme(button_row, "_letter_row_theme")
    dpg.bind_font(main_font)

# Screen keyboard theme
def _keyboard_btn(text):
    keyboard_btn = dpg.add_button(label=text, width=43, height=58,tag=text, callback=wordle_game.keyboard_btn_pressed)
    dpg.bind_item_theme(keyboard_btn, "_keyboard_btn_theme")
    dpg.bind_item_font(keyboard_btn, keyboard_font)

# Screen keyboard action keys theme
def _keyboard_action_btn(text, callback):
    keyboard_action_btn = dpg.add_button(label=text, width=65, height=58, callback=callback)
    dpg.bind_item_theme(keyboard_action_btn, "_keyboard_action_btn_theme")
    dpg.bind_item_font(keyboard_action_btn, keyboard_action_font)

# Link theme
def _hyperlink(text, address):
    link_btn = dpg.add_button(label=text, callback=lambda:webbrowser.open(address))
    dpg.bind_item_theme(link_btn, "_hyperlinkTheme")
    dpg.bind_item_font(link_btn, link_font)

# Error pop up theme
def _error_popup(text, pos, tag):
    error_popup = dpg.add_button(label=text, height=35, pos=pos, tag=tag)
    dpg.bind_item_theme(error_popup, "_error_popup_theme")
    dpg.bind_item_font(error_popup, link_font)
    dpg.bind_item_font(error_popup, link_font)

# Main window
with dpg.window():
    dpg.set_primary_window(dpg.last_item(), True)

    # Logo
    with dpg.group(horizontal=True, width=-1):
        _logo("Wordle.py")
        with dpg.tooltip(dpg.last_item()):
            dpg.add_text("Click to restart", tag="#logo_tooltip")
            dpg.bind_item_font("#logo_tooltip", link_font)

    dpg.add_separator(), dpg.add_spacer(height=10)

    # Create letter rows
    with dpg.group(horizontal=True):
        dpg.add_spacer(width=(500 - 5 * 70) / 2)
        _letter_row("", tag="#0_key")
        _letter_row("", tag="#1_key")
        _letter_row("", tag="#2_key")
        _letter_row("", tag="#3_key")
        _letter_row("", tag="#4_key")

    with dpg.group(horizontal=True, width=0):
        dpg.add_spacer(width=(500 - 5 * 70) / 2)
        _letter_row("", tag="#5_key")
        _letter_row("", tag="#6_key")
        _letter_row("", tag="#7_key")
        _letter_row("", tag="#8_key")
        _letter_row("", tag="#9_key")

    with dpg.group(horizontal=True, width=0):
        dpg.add_spacer(width=(500 - 5 * 70) / 2)
        _letter_row("", tag="#10_key")
        _letter_row("", tag="#11_key")
        _letter_row("", tag="#12_key")
        _letter_row("", tag="#13_key")
        _letter_row("", tag="#14_key")

    with dpg.group(horizontal=True, width=0):
        dpg.add_spacer(width=(500 - 5 * 70) / 2)
        _letter_row("", tag="#15_key")
        _letter_row("", tag="#16_key")
        _letter_row("", tag="#17_key")
        _letter_row("", tag="#18_key")
        _letter_row("", tag="#19_key")

    with dpg.group(horizontal=True, width=0):
        dpg.add_spacer(width=(500 - 5 * 70) / 2)
        _letter_row("", tag="#20_key")
        _letter_row("", tag="#21_key")
        _letter_row("", tag="#22_key")
        _letter_row("", tag="#23_key")
        _letter_row("", tag="#24_key")

    with dpg.group(horizontal=True, width=0):
        dpg.add_spacer(width=(500 - 5 * 70) / 2)
        _letter_row("", tag="#25_key")
        _letter_row("", tag="#26_key")
        _letter_row("", tag="#27_key")
        _letter_row("", tag="#28_key")
        _letter_row("", tag="#29_key")

    dpg.add_spacer(height=5)

    # Create screen keyboard
    with dpg.group(horizontal=True):
        dpg.add_spacer(width=(500 - 10 * 50) / 2)
        _keyboard_btn("Q")
        _keyboard_btn("W")
        _keyboard_btn("E")
        _keyboard_btn("R")
        _keyboard_btn("T")
        _keyboard_btn("Y")
        _keyboard_btn("U")
        _keyboard_btn("I")
        _keyboard_btn("O")
        _keyboard_btn("P")

    with dpg.group(horizontal=True):
        dpg.add_spacer(width=(500 - 9 * 50) / 2)
        _keyboard_btn("A")
        _keyboard_btn("S")
        _keyboard_btn("D")
        _keyboard_btn("F")
        _keyboard_btn("G")
        _keyboard_btn("H")
        _keyboard_btn("J")
        _keyboard_btn("K")
        _keyboard_btn("L")

    with dpg.group(horizontal=True):
        dpg.add_spacer(width=(500 - 9 * 55) / 2)
        _keyboard_action_btn("ENTER ", callback=wordle_game.enter_key_button)
        _keyboard_btn("Z")
        _keyboard_btn("X")
        _keyboard_btn("C")
        _keyboard_btn("V")
        _keyboard_btn("B")
        _keyboard_btn("N")
        _keyboard_btn("M")
        _keyboard_action_btn("DEL", callback=wordle_game.del_key_button)

    dpg.add_spacer(height=5), dpg.add_separator()


    with dpg.group(horizontal=True):
        dpg.add_spacer(width=(500 - 1 * 75) / 2)
        _hyperlink("<Github>", "https://github.com/Glouwhy/Wordle.py")


    with dpg.group(tag="#error_popup_group"):
        _error_popup(f"Error popup", pos=[230,-50], tag="#error_popup")


# Keyboard handle
with dpg.handler_registry():
    dpg.add_key_press_handler(callback=wordle_game.key_press_handler)


dpg.create_viewport(width=552, height=772, title="Wordle.py", small_icon="appicon.ico", large_icon="appicon.ico") # 775
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()