import turtle
import random
import pygame
import time

pygame.init()
pygame.mixer.init(buffer=16)

music_start = pygame.mixer.Sound('music.wav')
music_over = pygame.mixer.Sound('mario.wav')

window_height = 600
window_width = 600

update_interval = 25

river_width = 300
minimum_river_width = 120

border_height = 600

river_width_update = 0.5

safe_distance_from_border = border_height / 2 + 3

number_of_enemies = 10
enemies = []
enemy_speeds = []
enemy_width = 32
enemy_height = 32
enemy_speed_min, enemy_speed_max = 1, 25

player_width = 18
player_height = 24

# safe_distance_from_enemy = 15

turtle.speed(0)

def gameover(msg):
    global start_time
    end_time = time.time()
    duration = end_time - start_time
    for i in range(number_of_enemies):
        enemies[i].hideturtle()
    upper_river_border.hideturtle()
    lower_river_border.hideturtle()
    turtle.update()
    turtle.bgcolor("red")
    turtle.home()
    turtle.color("white")
    turtle.write(msg, align="center", font=("Arial", 24, "normal"))
    turtle.goto(0,-25)
    duration = "%.2f" % duration
    turtle.write('You survived ' + str(duration) + ' second!', align="center", font=("Arial", 24, "normal"))
    music_start.stop()
    music_over.play()

def moveplayerturtle(x, y):
    if x > -window_width / 2 and x < window_width / 2:
        turtle.goto(x, y)

def updatescreen():
    global river_width
    if river_width > minimum_river_width :
        upper_river_border.sety(upper_river_border.ycor() - river_width_update)
        lower_river_border.sety(lower_river_border.ycor() + river_width_update)
        river_width = river_width - 2 * river_width_update
    if upper_river_border.ycor() - turtle.ycor() < safe_distance_from_border:
        gameover("Oh no! You are dead!")
        return
    if -(lower_river_border.ycor() - turtle.ycor()) < safe_distance_from_border:
        gameover("Oh no! You are dead!")
        return
    for i in range(number_of_enemies):
        enemies[i].forward(enemy_speeds[i])
        
        enemy_left = enemies[i].xcor()- enemy_width/2 +4
        enemy_right = enemies[i].xcor()+ enemy_width/2 -4
        enemy_top = enemies[i].ycor()+ enemy_height/2 -4
        enemy_bottom = enemies[i].ycor()- enemy_height/2 +4
        
        player_left = turtle.xcor()- player_width/2 +4
        player_right = turtle.xcor()+ player_width/2 -4
        player_top = turtle.ycor()+ player_height/2 -4
        player_bottom = turtle.ycor()- player_height/2 +4
        
        if enemies[i].xcor() > (window_width+enemy_width)/2 + 65:
            x = -(window_width+enemy_width)/2 - 65
            y = random.randint(int(-(river_width-enemy_height)/2), int((river_width-enemy_height)/2))
            enemies[i].goto(x,y)
            enemy_speeds[i] = (random.randint(enemy_speed_min, enemy_speed_max))
#        if turtle.distance(enemies[i]) < safe_distance_from_enemy:
        collision = False
        if player_left > enemy_left and \
            player_left < enemy_right and \
            player_top < enemy_top and \
            player_top > enemy_bottom:
                collision = True
        if player_right > enemy_left and \
            player_right < enemy_right and \
            player_top < enemy_top and \
            player_top > enemy_bottom:
                collision = True
        if player_left > enemy_left and \
            player_left < enemy_right and \
            player_bottom < enemy_top and \
            player_bottom > enemy_bottom:
                collision = True
        if player_right > enemy_left and \
            player_right < enemy_right and \
            player_bottom < enemy_top and \
            player_bottom > enemy_bottom:
                collision = True
        if collision:
            gameover("Oh no! You are dead!")
            return
    turtle.update()
    turtle.ontimer(updatescreen, update_interval)
    
def startgame(x, y):
    global start_time
    turtle_instruction.clear()
    start_button.clear()
    start_button.hideturtle()
    turtle.update()
    start_time = time.time()
    turtle.ondrag(moveplayerturtle)
    turtle.ontimer(updatescreen, update_interval)
    music_start.play(-1)



turtle.setup(window_width, window_height)
turtle.bgcolor("RoyalBlue3")

turtle.tracer(False)

turtle.addshape("mushroom.gif") 

for _ in range(number_of_enemies):

    enemy = turtle.Turtle()

    enemy.shape("mushroom.gif")

    enemy.up()
    x = -(window_width + enemy_width) / 2 - 65
    y = random.randint(-(river_width-enemy_height)/2, (river_width-enemy_height)/2)
    enemy.goto(x, y)
    enemies.append(enemy)
    enemy_speeds.append(random.randint(enemy_speed_min, enemy_speed_max))

upper_river_border = turtle.Turtle()
upper_river_border.up()
lower_river_border = turtle.Turtle()
lower_river_border.up()

turtle.addshape("upper_river_border.gif")
turtle.addshape("lower_river_border.gif")
 
upper_river_border.shape("upper_river_border.gif")
lower_river_border.shape("lower_river_border.gif")

upper_river_border.sety((border_height + river_width) / 2)
lower_river_border.sety(-(border_height + river_width) / 2)

turtle_instruction = turtle.Turtle()
turtle_instruction.up()
turtle_instruction.hideturtle()
turtle_instruction.color('white')
turtle_instruction.goto(0,270)
turtle_instruction.write('Escape the evil mushroons!', align=("center"), font=("Arial", 18, "bold"))
turtle_instruction.goto(0,240)
turtle_instruction.write("To start the game, please press the 'Start' button.", align=("center"), font=("Arial", 12, "bold"))
turtle_instruction.goto(0,210)
turtle_instruction.write("You need to drag the Mario using the mouse to escape the evil mushrooms.", align=("center"), font=("Arial", 12, "bold"))
turtle_instruction.goto(0,180)
turtle_instruction.write("The Mario will die when it touches a mushroom or a boundary.", align=("center"), font=("Arial", 12, "bold"))
turtle.update()

turtle.addshape("mario.gif")
turtle.shape("mario.gif")
turtle.up()

start_button = turtle.Turtle()
start_button.up()
start_button.shape("triangle")
start_button.shapesize(2, 2) 
start_button.color("LightGrey") 
start_button.goto(0, -80)
start_button.down()
start_button.width(5)
start_button.circle(30)
start_button.up()
start_button.goto(0, -50)
start_button.down()

start_button.onclick(startgame)

turtle.update()
turtle.done()
