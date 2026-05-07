import word_lists as wl
import random

language = "en"
level = 1
choice = ""
points = 0

def start():
    global language

    if language == "en":
        print("1. Start\n2. Change Language")
    else:
        print("1. Start\n2. Sprache ändern")

    choice = input()

    if choice not in ("1", "2"):
        print("Invalid input. Please enter 1 or 2.")
    elif choice == "2":
        language = "de" if language == "en" else "en"
        print(f"Language changed to {'English' if language == 'en' else 'German'}.")
    else:
        print("Starting the game...")
    return choice

def main():
    return start()

def game_level(language_p, level_p):
    global points
    guess = ""
    tries = 6
    word_list = wl.WORDS[language_p].get(level_p + 2)
    word = random.choice(word_list)
    print(word)

    while word != guess and tries > 0:
        if language_p == "en":
            print(f"Guess the word with {level_p + 2} letters! You have {tries} tries left.")
        else:
            print(f"Errate das Wort mit {level_p + 2} Buchstaben! Du hast noch {tries} Versuche.")

        guess = input().upper()
        if guess != word:
            tries -= 1
            #hier kommt dann buchstabekontrolle
        else:
            points = points + (5 * tries) + (len(word) * 10) #beim ersten Versuch 6*5 oder 5*5? ein versuch weniger oder nicht?
            if language_p == "en":
                print("Congratulations! You've guessed the word!\nYour Score: " + str(points))
            else:
                print("Glückwunsch! Du hast das Wort erraten!\nDein Score: " + str(points))
            return True
    if word != guess and tries == 0:
        if language_p == "en":
            print(f"Game Over! The word was: {word}\nYour Score: {points}")
        else:
            print(f"Spiel vorbei! Das Wort war: {word}\nDein Score: {points}")
    return False

while True:     
    choice = main()
    if choice == "1":
        while game_level(language, level):
            if level + 2 > 7:
                if language == "en":
                    print("Congratulations! You've completed all levels!\nDo you want to continue playing? (y/n)")
                else:
                    print("Glückwunsch! Du hast alle Level abgeschlossen!\nMöchtest du weiter spielen? (y/n)")
                choice = input().lower()
                if choice == "n":
                    print("Thanks for playing! Goodbye!") if language == "en" else print("Danke fürs Spielen! Auf Wiedersehen!")
                    break
                elif choice == "y":
                    level = 5
            level += 1
        