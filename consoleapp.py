import word_lists as wl
import random

language = "en"
level = 1
points = 0
tries = 6

def show_menu():
    global language

    if language == "en":
        print("1. Start\n2. Change Language")
    else:
        print("1. Start\n2. Sprache ändern")

    choice = input()

    if choice not in ("1", "2"):
        print("Invalid input. Please enter 1 or 2.") if language == "en" else print("Ungültige Eingabe. Bitte gib 1 oder 2 ein.")
    elif choice == "2":
        language = "de" if language == "en" else "en"
        print(f"Language changed to {'English' if language == 'en' else 'German'}.")
    else:
        print("Starting the game...") if language == "en" else print("Das Spiel wird gestartet...")
    return choice


def play_round(lang, lvl, word):
    global points
    global tries
    guess = ""
    print(word)  # zum Testen

    while word != guess and tries > 0:
        if lang == "en":
            print(f"Guess the word with {lvl + 2} letters! You have {tries} tries left.")
        else:
            print(f"Errate das Wort mit {lvl + 2} Buchstaben! Du hast noch {tries} Versuche.")

        while True:
            guess = input().upper()
            if is_valid_input(guess, word, lvl, lang):
                break
            print("Invalid input. Please enter a valid word.\nYou have " + str(tries) + " tries left.") if lang == "en" else print("Ungültige Eingabe. Bitte gib ein gültiges Wort ein.\nDu hast noch " + str(tries) + " Versuche. ")

        if guess != word:
            tries -= 1
            display_feedback(guess, word)
        else:
            display_feedback(guess, word)
            points = points + (5 * tries) + (len(word) * 10)
            if lang == "en":
                print("Congratulations! You've guessed the word!\nYour Score: " + str(points))
            else:
                print("Glückwunsch! Du hast das Wort erraten!\nDein Score: " + str(points))
            return True
        if tries == 0:
            if lang == "en":
                print(f"Game Over! The word was: {word}\nYour Score: {points}")
            else:
                print(f"Spiel vorbei! Das Wort war: {word}\nDein Score: {points}")
            return False


def is_valid_input(user_input, word, lvl, lang):
    if len(user_input) != len(word):
        print("Wrong length.") if lang == "en" else print("Falsche Länge.")
        return False
    if user_input not in wl.WORDS[language].get(lvl + 2):
        return False
    return True


def display_feedback(guess, word):
    GREEN = "\033[42m\033[30m"
    YELLOW = "\033[43m\033[30m"
    GRAY = "\033[100m\033[30m"
    RESET = "\033[0m"

    for i in range(len(word)):
        if guess[i] == word[i]:
            print(GREEN + guess[i] + RESET, end="")
        elif guess[i] in word:
            print(YELLOW + guess[i] + RESET, end="")
        else:
            print(GRAY + guess[i] + RESET, end="")
    print()


def reset_game():
    global level, points, tries
    level = 1
    points = 0
    tries = 6


while True:
    reset_game()
    while show_menu() == "1": # zeigt Menü bei jedem neuen Spiel / Sprachänderung, startet Spiel bei Eingabe "1"
        word_list = wl.WORDS[language].get(level + 2)
        word = random.choice(word_list)
        while play_round(language, level, word): # nächstes Level solange Spieler gewinnt
            level += 1
            tries = 6

            if level + 2 > 8:
                if language == "en":
                    print("Congratulations! You've completed all levels!\nDo you want to continue playing? (y/n)")
                else:
                    print("Glückwunsch! Du hast alle Level abgeschlossen!\nMöchtest du weiter spielen? (y/n)")
                choice = input().lower()
                if choice == "n":
                    print("Thanks for playing! Goodbye!\nYour Score: " + str(points)) if language == "en" else print("Danke fürs Spielen! Auf Wiedersehen!\nDein Score: " + str(points))
                    reset_game()
                    break
                elif choice == "y":
                    level = 6
                else:
                    print("Invalid input. Please enter y or n.") if language == "en" else print("Ungültige Eingabe. Bitte gib y oder n ein.")
            word_list = wl.WORDS[language].get(level + 2)
            word = random.choice(word_list)
        reset_game() # reset nach Game Over oder wenn alle Level abgeschlossen