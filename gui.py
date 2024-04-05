import dearpygui.dearpygui as dpg
from themes import setup_themes
from functions import *
import webbrowser

WIDTH = 550
HEIGHT = 800

ROWS = 6
COLS = 5

wordle_game.pick_word()
dpg.create_context()
setup_themes()


with dpg.font_registry():
    logo_font = dpg.add_font(
        "./fonts/bevan/Bevan-Regular.ttf", 50)
    main_font = dpg.add_font(
        "./fonts/libre_franklin/LibreFranklin-Black.ttf", 40)
    keyboard_font = dpg.add_font(
        "./fonts/libre_franklin/LibreFranklin-Bold.ttf", 20)
    keyboard_action_font = dpg.add_font(
        "./fonts/libre_franklin/LibreFranklin-SemiBold.ttf", 15)
    link_font = dpg.add_font(
        "./fonts/libre_franklin/LibreFranklin-SemiBold.ttf", 15)


def logo(text):
    logo = dpg.add_button(label=text, tag="logo", width=300,
                          height=50, callback=wordle_game.restart)
    dpg.bind_item_theme(logo, "logo_theme")
    dpg.bind_item_font(logo, logo_font)

    with dpg.tooltip(dpg.last_item()):
        dpg.add_text("Click to restart", tag="logo_tooltip")
        dpg.bind_item_font("logo_tooltip", link_font)


def tile(text, tag):
    tile = dpg.add_button(label=text, width=61, height=61, tag=tag)
    dpg.bind_item_theme(tile, "tile_theme")
    dpg.bind_font(main_font)


def keyboard(text):
    keyboard = dpg.add_button(
        label=text, width=43, height=58, tag=text, callback=wordle_game.keyboard_btn_pressed)
    dpg.bind_item_theme(keyboard, "keyboard_theme")
    dpg.bind_item_font(keyboard, keyboard_font)


def keyboard_action(text, callback):
    keyboard_action = dpg.add_button(
        label=text, width=65, height=58, callback=callback)
    dpg.bind_item_theme(keyboard_action, "keyboard_theme")
    dpg.bind_item_font(keyboard_action, keyboard_action_font)


def error_popup(text, pos, tag):
    error_popup = dpg.add_button(label=text, height=35, pos=pos, tag=tag)
    dpg.bind_item_theme(error_popup, "error_popup_theme")
    dpg.bind_item_font(error_popup, link_font)
    dpg.bind_item_font(error_popup, link_font)


def hyperlink(text, address):
    hyperlink = dpg.add_button(
        label=text, callback=lambda: webbrowser.open(address))
    dpg.bind_item_theme(hyperlink, "hyperlinkTheme")
    dpg.bind_item_font(hyperlink, link_font)
