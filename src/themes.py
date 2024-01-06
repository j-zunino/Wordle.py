import dearpygui.dearpygui as dpg

def setup_themes():
    # Main theme
    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 0)
            dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 6, 6)
            dpg.add_theme_style(dpg.mvStyleVar_ChildBorderSize, 0)
            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 20, 0)

            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (18, 18, 19))
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (18, 18, 19))

            dpg.bind_theme(global_theme)

    with dpg.theme(tag="_logo_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (18, 18, 19))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (18, 18, 19))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (18, 18, 19))


    with dpg.theme(tag="_letter_row_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (18, 18, 19))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (18, 18, 19))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (18, 18, 19))

            dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1)

    with dpg.theme(tag="_keyboard_btn_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (129, 131, 132))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (141, 141, 142))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (151, 151, 152))

            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5)

    with dpg.theme(tag="_keyboard_action_btn_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (129, 131, 132))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (141, 141, 142))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (151, 151, 152))

            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5)

    with dpg.theme(tag="_error_popup_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (248, 248, 248))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (248, 248, 248))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (248, 248, 248))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (18, 18, 19))
            
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 3)
            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 10, 10)


    # Game themes
    with dpg.theme(tag="_correct_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (83, 141, 78))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (83, 141, 78))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (83, 141, 78))

    with dpg.theme(tag="_in_word_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (181, 159, 59))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (181, 159, 59))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (181, 159, 59))

    with dpg.theme(tag="_absent_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (58, 58, 60))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (58, 58, 60))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (58, 58, 60))

    with dpg.theme(tag="_key_correct_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (83, 141, 78))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (91, 148, 91))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (101, 148, 101))

            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5)

    with dpg.theme(tag="_key_in_word_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (181, 159, 59))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (191, 169, 67))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (196, 174, 73))

            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5)

    with dpg.theme(tag="_key_absent_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (58, 58, 60))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (67, 67, 69))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (78, 78, 79))

            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5)

    with dpg.theme(tag="_hyperlinkTheme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5)

            dpg.add_theme_color(dpg.mvThemeCol_Button, [0, 0, 0, 0])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [0, 0, 0, 0])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [29, 151, 236, 25])
            dpg.add_theme_color(dpg.mvThemeCol_Text, [29, 151, 236])
