import dearpygui.dearpygui as dpg

BG_COLOR = 18, 18, 19

KB_COLOR = 129, 131, 132
KB_COLOR_HOVER = 141, 141, 142
KB_COLOR_ACTIVE = 148, 148, 148

CORRECT = 83, 141, 78
IN_WORD = 181, 159, 59
ABSENT = 58, 58, 60


def setup_themes():
    # Main themes
    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 0)
            dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 6, 6)
            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 20, 0)

            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, BG_COLOR)
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, BG_COLOR)

            dpg.bind_theme(global_theme)

    with dpg.theme(tag="logo_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, BG_COLOR)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, BG_COLOR)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, BG_COLOR)

    with dpg.theme(tag="tile_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, BG_COLOR)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, BG_COLOR)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, BG_COLOR)

            dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1)

    with dpg.theme(tag="keyboard_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, KB_COLOR)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, KB_COLOR_HOVER)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, KB_COLOR_ACTIVE)

            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4)

    # Game themes
    with dpg.theme(tag="correct_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, CORRECT)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, CORRECT)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, CORRECT)

    with dpg.theme(tag="in_word_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, IN_WORD)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, IN_WORD)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, IN_WORD)

    with dpg.theme(tag="absent_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, ABSENT)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, ABSENT)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, ABSENT)

    with dpg.theme(tag="key_correct_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, CORRECT)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, CORRECT)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, CORRECT)

            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4)

    with dpg.theme(tag="key_in_word_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, IN_WORD)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, IN_WORD)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, IN_WORD)

            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4)

    with dpg.theme(tag="key_absent_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, ABSENT)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, ABSENT)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, ABSENT)

            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4)

    # Other stuff
    with dpg.theme(tag="hyperlinkTheme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4)

            dpg.add_theme_color(dpg.mvThemeCol_Button, [0, 0, 0, 0])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [0, 0, 0, 0])
            dpg.add_theme_color(
                dpg.mvThemeCol_ButtonHovered, [29, 151, 236, 25])
            dpg.add_theme_color(dpg.mvThemeCol_Text, (29, 151, 236))

    with dpg.theme(tag="error_popup_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (248, 248, 248))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (248, 248, 248))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (248, 248, 248))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (18, 18, 19))

            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4)
            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 10, 10)
