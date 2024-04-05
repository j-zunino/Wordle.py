import dearpygui.dearpygui as dpg
import threading
import random
import string
import time


class WordleGame:
    print_secret_word = False
    COLS = 5
    ROWS = 6

    def __init__(self):
        self.row_index = 0
        self.button_index = 0
        self.valid_words = []
        self.user_answer = []
        self.buttons_dict = {}
        self.random_word = ""
        self.game_state = "playing"

    def show_error_popup(self, message, pos):
        dpg.set_item_label("error_popup", message)
        dpg.set_item_pos("error_popup", pos)
        dpg.configure_item("error_popup", show=True)

        threading.Thread(target=self.hide_error_popup, args=(2.0,)).start()

    def hide_error_popup(self, delay):
        time.sleep(delay)
        dpg.configure_item("error_popup", show=False)

    def pick_word(self):
        with open("valid_words.txt", "r") as file:
            words_list = file.readlines()
            self.valid_words = [words.rstrip(
                "\n").upper() for words in words_list]

            self.random_word = random.choice(self.valid_words)

            if self.print_secret_word == True:
                print(f"Word selected: {self.random_word}")
            else:
                print(f"Word selected: *****")

    # Fix from https://github.com/pixegami/python-wordle
    def verify_answer(self):
        user_answer = ''.join(self.user_answer)
        secret_word_letters = list(self.random_word)
        correct_positions = set()

        result = ["ABSENT"] * len(secret_word_letters)

        # Check for correct letters in correct positions and mark their positions.
        for i, letter in enumerate(user_answer):
            if letter == secret_word_letters[i]:
                correct_positions.add(i)
                result[i] = "CORRECT"
                # Void out the correctly guessed letter.
                secret_word_letters[i] = "*"

        # Check for correct letters in incorrect positions and mark them.
        for i, letter in enumerate(user_answer):
            if result[i] == "CORRECT":  # Skip letters already marked green.
                continue
            elif letter in secret_word_letters:
                result[i] = "INWORD"
                # Void out the guessed letter.
                secret_word_letters[secret_word_letters.index(letter)] = "*"

        # Mark remaining correct letters.
        for i, letter in enumerate(user_answer):
            if result[i] == "ABSENT" and letter in secret_word_letters:
                result[i] = "CORRECT"
                # Void out the correctly guessed letter.
                secret_word_letters[secret_word_letters.index(letter)] = "*"

        # Mark the buttons according to the result array.
        for i, color in enumerate(result):
            button_to_update = self.buttons_dict.get(i)
            if color == "CORRECT":
                self.mark_correct_guess(
                    button_to_update, user_answer[i])
            elif color == "INWORD":
                self.mark_in_word_guess(
                    button_to_update, user_answer[i])
            else:
                self.mark_incorrect_position(
                    button_to_update, user_answer[i])

        if len(correct_positions) == len(self.random_word):
            self.handle_game_won(correct_positions)

    def mark_correct_guess(self, button, letter):
        dpg.bind_item_theme(button, "correct_theme")
        dpg.bind_item_theme(f"{letter}", "key_correct_theme")

    def mark_in_word_guess(self, button, letter):
        dpg.bind_item_theme(button, "in_word_theme")
        dpg.bind_item_theme(f"{letter}", "key_in_word_theme")

    def mark_incorrect_position(self, button, letter):
        dpg.bind_item_theme(button, "absent_theme")
        dpg.bind_item_theme(f"{letter}", "key_absent_theme")

    def handle_game_won(self, correct_positions):
        dpg.set_item_label("logo", "Click to restart")
        self.show_error_popup("Splendid", [236, 50])
        self.game_state = "won"

    def keyboard_btn_pressed(self, sender):
        if self.game_state != "playing":
            return

        if len(self.user_answer) < self.COLS:
            key_pressed = dpg.get_item_label(sender)
            self.user_answer.append(key_pressed)

            self.update_game_ui(key_pressed)
            print(f"Pressed: {key_pressed}, added to list: {self.user_answer}")
        else:
            self.user_answer = self.user_answer[:self.COLS]
            print(f"Reached the limit of available space. {self.user_answer}")

    def key_press_handler(self, sender, app_data):
        if self.game_state != "playing":
            return

        elif app_data == 13:  # Enter key
            wordle_game.enter_key_button(sender)

        elif app_data == 8:  # Backspace key
            wordle_game.del_key_button(sender)

        if len(self.user_answer) < self.COLS:
            # Check if the pressed key is a letter
            if 65 <= app_data <= 90:
                key_pressed = chr(app_data)
                self.user_answer.append(key_pressed)
                wordle_game.update_game_ui(key_pressed)
        else:
            self.user_answer = self.user_answer[:self.COLS]

    def enter_key_button(self, sender):
        answer = ''.join(self.user_answer)
        if self.game_state != "playing":
            return

        elif self.button_index == self.COLS:
            print(f"Row {self.row_index} completed!")

            if self.row_index == self.ROWS:
                print("All rows completed!")

            if answer in self.valid_words:
                self.verify_answer()
                self.row_index += 1
                self.button_index = 0
                self.user_answer.clear()

            else:
                self.show_error_popup("Not in word list", [220, 50])
                print(f"Invalid word, user answer: {self.user_answer}")

        else:
            self.show_error_popup("Not enough letters", [209, 50])
            print(f"Enter five letters in the current row. {self.user_answer}")

        if self.row_index >= self.ROWS:
            if self.game_state == "won":
                pass
            else:
                self.show_error_popup(
                    f"The words was: {self.random_word}", [200, 50])
                dpg.set_item_label("logo", "Click to restart")
                self.game_state = "lost"

        else:
            print(f"Reached the limit of available space. {self.user_answer}")

    def del_key_button(self, sender):
        if self.game_state != "playing":
            return
        elif self.button_index > 0:
            self.button_index -= 1
            self.user_answer.pop()
            button_to_update = self.buttons_dict.get(self.button_index)
            print(f"Deleted last letter, new user answer: {self.user_answer}")

            if button_to_update:
                dpg.set_item_label(button_to_update, "")
                dpg.bind_item_theme(button_to_update, "tile_theme")

        else:
            self.user_answer = []
            print("No letters to delete.")

    def update_game_ui(self, key_pressed):
        if len(self.user_answer) <= self.COLS:
            if self.button_index < self.COLS:
                button_to_update = dpg.get_item_alias(
                    f"#{self.button_index + self.row_index * self.COLS}_key")
                if not dpg.get_item_label(button_to_update):
                    dpg.set_item_label(button_to_update, key_pressed)
                    self.button_index += 1
                    self.buttons_dict[self.button_index - 1] = button_to_update
                    print(f"Letter: {key_pressed}, added to button #{
                          self.button_index} in row {self.row_index}")
                    if self.button_index == self.COLS:
                        print("Row completed!")
        else:
            print(f"Reached the limit of available space. {self.user_answer}")

    def restart(self):
        self.__init__()
        self.pick_word()

        dpg.set_item_label("logo", "Wordle.py")

        print("Game restarted!")

        # Restart letters state
        for i in range(self.COLS * self.ROWS):
            button_to_reset = dpg.get_item_alias(f"#{i}_key")
            dpg.set_item_label(button_to_reset, "")
            dpg.bind_item_theme(button_to_reset, "tile_theme")

        # Restart keyboard state
        for i in string.ascii_uppercase:
            dpg.bind_item_theme(f"{i}", "keyboard_theme")


wordle_game = WordleGame()
