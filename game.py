import pygame as pg
import random as rnd
import word_lists

pg.init()

WIDTH, HEIGHT = 640, 640
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Wörtre")
font = pg.font.Font("Grand9K Pixel.ttf", 20)

var_input = ""
level_length = 3
correct_word = rnd.choice(word_lists.three_word_list_german)

running = True
clock = pg.time.Clock() # Set the desired frames per second (FPS) for the game loop

def check_input(user_input): 
    return user_input == correct_word

def valid_input(event):
    global var_input

    if event.key == pg.K_RETURN:
        if var_input in word_lists.three_word_list_german:
            print("Word exists in the list.")

            if check_input(var_input):
                print("true")
            else:
                print("false")
                var_input = ""

        else:
            print("Word does not exist in the list.")

        print(correct_word)

    elif event.key == pg.K_BACKSPACE:
        var_input = var_input[:-1]

    else:
        char = event.unicode
        if char.isalpha() and len(var_input) < level_length:
            var_input += char.upper()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.KEYDOWN: 
            valid_input(event)

    pg.display.flip() 
    clock.tick(60)

pg.quit()