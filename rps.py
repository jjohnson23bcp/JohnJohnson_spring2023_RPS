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
WIDTH = 600
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
# rock images
# defining rock image - shows where to get the image
rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
# storing where the pixel are and the dimensions, allows us to access and change them
rock_image_rect = rock_image.get_rect()
# rock image the cpu is going to use
cpu_rock_image_rect = rock_image.get_rect()
# paper images
paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
paper_image_rect = paper_image.get_rect()
# adjusts where the image will appear on the screen
paper_image_rect.x = 220
cpu_paper_image_rect = paper_image.get_rect()
# scissor images
scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
scissors_image_rect = scissors_image.get_rect()
scissors_image_rect.x = 400
cpu_scissors_image_rect = scissors_image.get_rect()
# win image
win_image = pg.image.load(os.path.join(game_folder, 'win.jpg')).convert()
win_image_rect = win_image.get_rect()
# lose image
lose_image = pg.image.load(os.path.join(game_folder, 'lose.jpg')).convert()
lose_image_rect = lose_image.get_rect()
# tie image
tie_image = pg.image.load(os.path.join(game_folder, 'tie.jpg')).convert()
tie_image_rect = tie_image.get_rect()
# defining the variable choices as a list from 0-2 
choices = ["Rock", "Paper", "Scissors"]
# function cpu_randchoice that tells the computer to randomly choose rock paper or scissors
def cpu_randchoice():
    # makes the cpu variable usable outside of the definition loop
    global cpu
    # defining the variable cpu as the list choices which are randomly picked
    cpu = choices[randint(0,2)]
    sleep(1)
    # displays the string in the terminal
    print("Computer randomly chose", cpu)
# turns on
running = True
# starts while loop
while running:
    # forces FPS into 30 FPS
    clock.tick(FPS)
    # for loop - everything in the loop will happen for the event
    for event in pg.event.get():
        ################### get user input #################
        # if the quit button is clicked, end pygame
        if event.type == pg.QUIT:
            running = False
        # the event of when the mouse button is released
        if event.type == pg.MOUSEBUTTONUP:
            # finds the mouse position and stores it 
            mouse_coords = pg.mouse.get_pos() 
            if rock_image_rect.collidepoint(mouse_coords):
                # if rock image is selected, print Rock in the terminal
                print("Rock")
                # set user equal to rock to be used in the comparitive statements
                user = "Rock"
                # calling the function for the computer to randomly choose
                cpu_randchoice()
                # will make GAMEOVER true if it is not true, otherwise it will become false
                if GAMEOVER == False:
                    GAMEOVER = True
                else:
                    GAMEOVER = False
            # if user chooses paper
            elif paper_image_rect.collidepoint(mouse_coords):
                print("Paper")
                user = "Paper"
                cpu_randchoice()
                if GAMEOVER == False:
                    GAMEOVER = True
                else:
                    GAMEOVER = False
            # if user chooses scissors
            elif scissors_image_rect.collidepoint(mouse_coords):
                print("Scissors")
                user = "Scissors"
                cpu_randchoice() 
                if GAMEOVER == False:
                    GAMEOVER = True
                else:
                    GAMEOVER = False     
            else:
                print("Select Rock Paper or Scissors")
    ################### update ####################
   
    ################### draw ################
    # fills the screen in with black
    screen.fill(BLACK)      
    #  if the rock image is select, draw only the rock image, the other images will leave the screen
    if not GAMEOVER:
        # drawing the rock image on the screen
        screen.blit(rock_image, rock_image_rect)
        screen.blit(paper_image, paper_image_rect)
        screen.blit(scissors_image, scissors_image_rect)
    # different paths for each option the user has
    elif user == "Rock":
        # different options the computer has when it randomly chooses
        if cpu == "Rock":
            # calls the cpu rock image onto the screen
            cpu_rock_image_rect.y = 200
            # draws only the rock image and cpu rock image
            screen.blit(rock_image, cpu_rock_image_rect)
            screen.blit(rock_image, rock_image_rect)
            # delays next line of code
            sleep(2)
            # draws the result of the matchup
            screen.blit(tie_image, tie_image_rect)
        if cpu == "Paper":
            cpu_paper_image_rect.y = 200
            screen.blit(paper_image, cpu_paper_image_rect)
            screen.blit(rock_image, rock_image_rect)  
            sleep(2)
            screen.blit(lose_image, lose_image_rect)
        if cpu == "Scissors":
            cpu_scissors_image_rect.y = 200
            screen.blit(scissors_image, cpu_scissors_image_rect)
            screen.blit(rock_image, rock_image_rect)
            sleep(2)
            screen.blit(win_image, win_image_rect)
    # paper paths
    elif user == "Paper":
        if cpu == "Rock":
            cpu_rock_image_rect.y = 200
            screen.blit(paper_image, paper_image_rect)
            screen.blit(rock_image, cpu_rock_image_rect)
            sleep(2)
            screen.blit(win_image, win_image_rect)
        if cpu == "Paper":
            cpu_paper_image_rect.y = 200
            screen.blit(paper_image, paper_image_rect)
            screen.blit(paper_image, cpu_paper_image_rect)
            sleep(2)
            screen.blit(tie_image, tie_image_rect)
        if cpu == "Scissors":
            cpu_scissors_image_rect.y = 200
            screen.blit(paper_image, paper_image_rect)
            screen.blit(scissors_image, cpu_scissors_image_rect)
            sleep(2)
            screen.blit(lose_image, lose_image_rect)
    # scissor paths
    elif user == "Scissors":
        if cpu == "Rock":
            cpu_rock_image_rect.y = 200
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(rock_image, cpu_rock_image_rect)
            sleep(2)
            screen.blit(lose_image, lose_image_rect)
        elif cpu == "Paper":
            cpu_paper_image_rect.y = 100
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(paper_image, cpu_paper_image_rect)
            sleep(2)
            screen.blit(win_image, win_image_rect)
        elif cpu == "Scissors":
            cpu_scissors_image_rect.y = 200
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(scissors_image, cpu_scissors_image_rect)
            sleep(2)
            screen.blit(tie_image, tie_image_rect)
    # game display is modified
    pg.display.flip()
# quits pygame
pg.quit()