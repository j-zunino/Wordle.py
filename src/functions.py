import dearpygui.dearpygui as dpg
import threading
import random
import string
import time

class WordleGame:
    def __init__(self):
        self.BUTTONS_PER_ROW = 5
        self.MAX_ROWS = 6
        self.game_state = "playing"
        self.user_answer = []
        self.button_index = 0
        self.row_index = 0
        self.buttons_dict = {}
        self.random_word = ""
        self.valid_words = []

    def show_error_popup(self, message, pos):
        dpg.set_item_label("#error_popup", message)
        dpg.set_item_pos("#error_popup", pos)
        dpg.configure_item("#error_popup", show=True)

        threading.Thread(target=self.hide_error_popup, args=(2.0,)).start()

    def hide_error_popup(self, delay):
        time.sleep(delay)
        dpg.configure_item("#error_popup", show=False)

    def restart(self):
        self.button_index = 0
        self.row_index = 0
        self.user_answer.clear()
        self.game_state = "playing"

        dpg.set_item_label("#logo", "Wordle.py")
        self.pick_word()
        
        print("Game restarted!")

        # Restart letters state
        for i in range(self.BUTTONS_PER_ROW * self.MAX_ROWS):
            button_to_reset = dpg.get_item_alias(f"#{i}_key")
            dpg.set_item_label(button_to_reset, "")
            dpg.bind_item_theme(button_to_reset, "_letter_row_theme")

        # Restart keyboard state
        for i in string.ascii_uppercase:
            dpg.bind_item_theme(f"{i}", "_keyboard_btn_theme")

    def pick_word(self):
        with open("valid_words.txt", "r") as file:
            words_list = file.readlines()
            self.valid_words = [words.rstrip("\n").upper() for words in words_list]
            self.random_word = random.choice(self.valid_words)
            print(f"Word selected: {self.random_word}")

    def verify_answer(self):
        answer = ''.join(self.user_answer)
        secret_list = list(self.random_word)

        for i, letter in enumerate(answer):
            button_to_update = self.buttons_dict.get(i)
            if button_to_update:
                if letter == secret_list[i]:
                    dpg.bind_item_theme(button_to_update, "_correct_theme")
                    dpg.bind_item_theme(f"{letter}", "_key_correct_theme")
                    secret_list[i] = '*'
                elif letter in secret_list:
                    dpg.bind_item_theme(button_to_update, "_in_word_theme")
                    dpg.bind_item_theme(f"{letter}", "_key_in_word_theme")
                    secret_list[secret_list.index(letter)] = '*'
                else:
                    dpg.bind_item_theme(button_to_update, "_absent_theme")
                    dpg.bind_item_theme(f"{letter}", "_key_absent_theme")

        if ''.join(secret_list) == '*' * len(secret_list):
            dpg.set_item_label("#logo", "Click to restart")
            self.show_error_popup("Splendid", [238.5, 50])
            self.game_state = "won"
        else:
            pass

    def update_game_ui(self, key_pressed):
        if len(self.user_answer) <= 5:
            if self.button_index < self.BUTTONS_PER_ROW:
                button_to_update = dpg.get_item_alias(f"#{self.button_index + self.row_index * self.BUTTONS_PER_ROW}_key")
                if not dpg.get_item_label(button_to_update):
                    dpg.set_item_label(button_to_update, key_pressed)
                    self.button_index += 1
                    self.buttons_dict[self.button_index - 1] = button_to_update
                    print(f"Letter: {key_pressed}, added to button #{self.button_index} in row {self.row_index}")
                    if self.button_index == self.BUTTONS_PER_ROW:
                        print("Row completed!")
        else:  
            self.user_answer = self.user_answer[:5]
            print(f"Reached the limit of available space. {self.user_answer}")

    def keyboard_btn_pressed(self, sender):
        if self.game_state != "playing":
            return

        if len(self.user_answer) < 5:
            key_pressed = dpg.get_item_label(sender)
            self.user_answer.append(key_pressed)

            self.update_game_ui(key_pressed)
            print(f"Pressed: {key_pressed}, added to list: {self.user_answer}")

        else:  
            self.user_answer = self.user_answer[:5]
            print(f"Reached the limit of available space. {self.user_answer}")

    def key_press_handler(self, sender, app_data):
        if self.game_state != "playing":
            return

        if len(self.user_answer) < 5:
            # Check if the pressed key is a letter
            if 65 <= app_data <= 90:
                key_pressed = chr(app_data)
                self.user_answer.append(key_pressed)
                wordle_game.update_game_ui(key_pressed)

        if app_data == 13: # Enter key
                wordle_game.enter_key_button(None)

        elif app_data == 8: # Backspace key
                wordle_game.del_key_button(None)

        else:  
            self.user_answer = self.user_answer[:5]

    def enter_key_button(self, sender):
        answer = ''.join(self.user_answer)
        if self.game_state != "playing":
            return

        if self.button_index == self.BUTTONS_PER_ROW:
            print(f"Row {self.row_index} completed!")

            if self.row_index == self.MAX_ROWS:
                print("All rows completed!")

            if answer in self.valid_words:
                self.verify_answer()
                self.row_index += 1
                self.button_index = 0
                self.user_answer.clear()

            else:
                self.show_error_popup("Not in word list", [221, 50])
                print(f"Invalid word, user answer: {self.user_answer}, word: {self.random_word}")

        else:
            self.show_error_popup("Not enough letters", [210, 60])
            print(f"Enter five letters in the current row. {self.user_answer}")
            
        if self.row_index > 5:
            self.show_error_popup(f"The words was: {self.random_word}", [200, 50])
            dpg.set_item_label("#logo", "Click to restart")
            self.game_state = "lost"

        else:
            print(f"Reached the limit of available space. {self.user_answer}")

    def del_key_button(self, sender):
        if self.game_state != "playing":
            return
        if self.button_index > 0:
            self.button_index -= 1
            self.user_answer.pop()
            button_to_update = self.buttons_dict.get(self.button_index)
            print(f"Deleted last letter, new user answer: {self.user_answer}")

            if button_to_update:
                dpg.set_item_label(button_to_update, "")
                dpg.bind_item_theme(button_to_update, "_letter_row_theme")

        else:
            self.user_answer = []
            print("No letters to delete.")

wordle_game = WordleGame()
