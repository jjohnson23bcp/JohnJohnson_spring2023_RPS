# file created by John Johnson
# creating a visually interactive Rock Paper Scissors game with Ru
# import libraries
# sleep used to delay code
from time import sleep
# randint used to generate a random result
from random import randint
# comprehensive game library for use with python
import pygame as pg
# manage files and folders in directories
import os

# stores where we are currently working in the game folder
game_folder = os.path.dirname(__file__)
print(game_folder)
# the game is not going to end until we make it end
GAMEOVER = False
# game settings
WIDTH = 360
HEIGHT = 480
FPS = 30
# define colors
# tuples are immutable - cannot change once created
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# initialize pygame 
pg.init()
# initialize sound element of pygame
pg.mixer.init()
# set up the screen so we can use it, stores pygame's display in the variable screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
# sets the title of the game screen as the string
pg.display.set_caption("Rock, Paper, Scissors...")
# defines the class game clock, makes it ready for use
clock = pg.time.Clock()
# defining rock image - shows where to get the image
rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
# storing where the pixel are and the dimensions, allows us to access and change them
rock_image_rect = rock_image.get_rect()
paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
paper_image_rect = paper_image.get_rect()
# adjusts where the image will appear on the screen
paper_image_rect.x = 210
paper_image_rect.y = 100
scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
scissors_image_rect = scissors_image.get_rect()
scissors_image_rect.y = 200
# turns on
running = True
# starts while loop
while running:
    # forces FPS into 30 FPS
    clock.tick(FPS)
    # for loop - everything in the loop will happen for the event
    for event in pg.event.get():
        # if the quit button is clicked, end pygame
        if event.type == pg.QUIT:
            running = False
        # the event of when the mouse button is released
        if event.type == pg.MOUSEBUTTONUP:
            # prints where the mouse is clicking in the terminal
            # 0 refers to the 1st element in the coordinates tuple - x
            # print(pg.mouse.get_pos()[0])
            # 0 refers to the 2nd element in the coordinate tuple - y
            # print(pg.mouse.get_pos()[1])
            # finds the mouse position and stores it 
            mouse_coords = pg.mouse.get_pos()
            # if rock image is selected, print Rock in the terminal 
            if rock_image_rect.collidepoint(mouse_coords):
                print("Rock")
                # if gameover is false, make gameover true, else gameover will stay false
                if GAMEOVER == False:
                    GAMEOVER = True
                else:
                    GAMEOVER = False
            elif paper_image_rect.collidepoint(mouse_coords):
                print("Paper")
                if GAMEOVER == False:
                    GAMEOVER = True
                else:
                    GAMEOVER = False
            elif scissors_image_rect.collidepoint(mouse_coords):
                print("Scissors")
                if GAMEOVER == False:
                    GAMEOVER = True
                else:
                    GAMEOVER = False       
            else:
                print("Select an Image")
    
    ################### get user input #################
    # keyboard, mouse, controller, vr headset 
    # HCI - human computer interaction
    # defining the variable choices as a list from 0-2
    ################### update ####################
    if rock_image_rect.x < 200 and not GAMEOVER:
        rock_image_rect.x += 1
    if paper_image_rect.y < 250 and not GAMEOVER:
        paper_image_rect.y += 1
    if scissors_image_rect.y < 250 and not GAMEOVER and scissors_image_rect.x < 250:
        scissors_image_rect.x += 1 
        scissors_image_rect.y += 1
   
    ################### draw ################
    # fills the screen in with black
    screen.fill(BLACK)  
    # if game still running 
    if not GAMEOVER:
        # drawing the rock image on the screen
        screen.blit(rock_image, rock_image_rect)
        screen.blit(paper_image, paper_image_rect)
        screen.blit(scissors_image, scissors_image_rect)
    #  if the rock image is select, draw only the rock image, the other images will leave the screen
    elif rock_image_rect.collidepoint(mouse_coords):
        screen.blit(rock_image, rock_image_rect)
    elif paper_image_rect.collidepoint(mouse_coords):
        screen.blit(paper_image, paper_image_rect)
    elif scissors_image_rect.collidepoint(mouse_coords):
        screen.blit(scissors_image, scissors_image_rect)
    else:
        pass

    pg.display.flip()
# quits pygame
pg.quit()
