import random as rnd
import game_style

def handle_key(event):
    # event.keysym enthält den Namen der Taste (z.B. 'a', 'Return', 'BackSpace')
    key = event.keysym
    global var_input 
    global level_length

    game_style.buildLevel(level_length)

    if len(var_input) < level_length or (key == "BackSpace" or key == "Return"):
        if key == "Return":
            if check_input(var_input): 
                print("true")
            else:
                print("false")
                var_input = ""
            print(correct_word)
        elif key == "BackSpace":
            var_input = var_input[:-1]
            print(var_input)
        elif len(key) == 1 and key.isalpha(): # ist Alphanumerisch?
            var_input = var_input + key
            print(var_input)
    else:
        print("max länge erreicht")
        print(var_input)

def check_input(user_input):
    global correct_word
    if user_input.upper() == correct_word:
        return True
    else:
        return False

game_style.styleApp()

var_input = ""
level_length = 3

word_list = [
    "AAL", "ABO", "AKT", "ALM", "AMT", "ART", "AST", "AUF", "AUS", "BAD", 
    "BAU", "BEI", "BIT", "BOX", "BUH", "EHE", "EIS", "ELF", "ERZ", "FAN", 
    "FAX", "FEE", "GEL", "GEN", "GUT", "HAI", "HOF", "HUT", "ICH", "IHM", 
    "IHN", "IHR", "INN", "IST", "JOB", "KAI", "KID", "KUR", "LAB", "LOB", 
    "LOG", "LOS", "MAI", "MAL", "MAU", "MET", "MIX", "MUT", "NAH", "NEU", 
    "NIE", "NOT", "NUN", "OFT", "OHR", "OST", "RAD", "RAT", "RAU", "REH", 
    "ROH", "ROT", "RUF", "SAU", "SEE", "SET", "SIE", "SKI", "SOL", "TAG", 
    "TAT", "TEE", "TOD", "TON", "TOR", "TOT", "TUN", "UHR", "UND", "UNS", 
    "UWE", "VON", "VOR", "WAL", "WAS", "WEG", "WEM", "WEN", "WER", "WIE", 
    "WIR", "WUT", "ZUG"]

correct_word = rnd.choice(word_list)

# Bindet alle Tastendruck-Events an die Funktion
game_style.app.bind("<Key>", handle_key)

game_style.app.mainloop()