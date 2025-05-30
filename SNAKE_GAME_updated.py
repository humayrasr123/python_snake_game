# Snake Game 
# GUI game (snake)
#Team members
# A- Eduardo Marquez
# B- Stephany Carreno Portillo
# C- Humayra Rashid
# D- Roxana Cruz

#Software used-
#Python
#Visual Studio Code
#Pygame
#Tkinter

from tkinter import *
import random                           #to create a window

from pygame import mixer # used later on for audio
import sys


GAME_WIDTH = 700 #WindowDimention
GAME_HEIGHT = 650
SPEED = 180
SPACE_SIZE = 50
BODY_PARTS = 3 #SnakeSize
SNAKE_COLOR = "Gold"
FOOD_COLOR = "red" #GameColors
BACKGROUND_COLOR = "Cornflower blue"
mixer.init()

class Snake:

    def __init__(self):  #Initializes the Snake class with body_size, coordinates, and squares.
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):  #The fuction to build starting length
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:  #the function for how the snake grows
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Food:

    def __init__(self): #Initializes a new instance of the Food class. Generates random coordinates for the food object within the game window.

        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food",)



def next_turn(snake, food):  #Updates the game state for the next turn. Moves the snake, checks for collision, and generates new food if the snake has eaten the current food.

    x, y = snake.coordinates[0] #The code defines a function that uses the coordinates of a snake and its direction to move the snake in a given direction. However, no additional functions in the code
        #coordinates will be sored in x and y
    if direction == "up":     #creating direction and movement of snake
        y -= SPACE_SIZE #for causing the snake to move upward
    elif direction == "down":
        y += SPACE_SIZE   #a plus sign in between for for causing the snake to move down
    elif direction == "left":
        x -= SPACE_SIZE   #same method but with x coordinate to move it right or left
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))   #This code creates a new coordinate into a list and creates a new rectangle on a canvas

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)   #for starting and ending corner of the snake as a rectangle when it moves

    snake.squares.insert(0, square)  #to update snakes list of squares

    if x == food.coordinates[0] and y == food.coordinates[1]:  #using if else statement to regenerate the apple in new position everytime eaten by the snake

        global score          #used to define the amount of time
        global SPEED
    

        if (score % 5 == 0):   #for changing the speed every five score points, so it increases seed by 10
            SPEED += 10      #it decreases the points in speed by 10, so speed of the snake increases in the game 
        score += 1     #for every increase in score

        label.config(text="Score:{}".format(score))     #for defining the score on top

        canvas.delete("food")    #for removing the apple from the position when eaten

        food = Food()      #to run the fuction

    else:

        del snake.coordinates[-1]   #to delete last set of coordinates, as when code run, the snake is long as the whole window and so to shorten it to three blocks

        canvas.delete(snake.squares[-1])  #to update canvas of the deletion

        del snake.squares[-1]    #to set it to a specific number of squares in a snake that can move

    if check_collisions(snake): #snake dies/game over when it collides with the wall/body
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)    #to continue the game if the snake does not die


def change_direction(new_direction):    #for allowing the snake to change direction

    global direction     #for defining the direction variable 

    if new_direction == 'left':    #using if/else statement for fixing direction
        if direction != 'right':       #if the user presses left arrrow key, it should not go right
            direction = new_direction
    elif new_direction == 'right':      #same method, different direction
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':  #user presses key to go up, the code is used to stop snake from going down
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':   #the same technique, but different direction
        if direction != 'up':
            direction = new_direction


def check_collisions(snake):   #defining funnction to eat the apple or die when collided with wall

    x, y = snake.coordinates[0]   #unpack head of the snake

    if x < 0 or x >= GAME_WIDTH:  #for snake to collide with the wall as it reaches the end coordinate
        return True
    elif y < 0 or y >= GAME_HEIGHT:  #same method, but with height
        return True

    for body_part in snake.coordinates[1:]:   #if it collides with body part
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def game_over():     #after the user loses or above function takes place, this function will run for ending the game

    canvas.delete(ALL)    #delete all that took place
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,    # to fix position of the text after game over
 font=('Ravie',60), text="You Died", fill="black", tag="gameover")   #setting font and size of text
    mixer.Sound.play(cash_sound)

window = Tk()                             #making window
window.title("Snake game")           #giving a title for this window
window.resizable(False, False)         #to prevent resizing the window

cash_sound=mixer.Sound("[Music] New Super Mario Bros - Game over.mp3")

score = 0      #creating initial score
direction = 'down'  #initial direction of the snake

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()  #for creating and running label on the top with specified font and size
#also pack this label to run
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH) #to give height, color and width to the window
canvas.pack()   #pack this canvas to run the features

window.update()      #to update the window

window_width = window.winfo_width()   #ensuring size of the screen and window and to fix the position for it when it runs
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))   #to adjust the position of the window
y = int((screen_height/2) - (window_height/2)) #both value of x and y must be in integers for the next line

window.geometry(f"{window_width}x{window_height}+{x}+{y}") #fixing geometry of the window using integer value of x,y

window.bind('<Left>', lambda event: change_direction('left'))  #to control movevemnt of the snake using arrow keys
window.bind('<Right>', lambda event: change_direction('right'))    #using event function to run the code
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake() #for running snake object
food = Food() #for running food object

next_turn(snake, food)

window.mainloop()    #to tell the tkinter to run every event