import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager, MOVE_INCREMENT, STARTING_MOVE_DISTANCE
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

car_speed = STARTING_MOVE_DISTANCE

screen.listen()

screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars(car_speed)
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() > FINISH_LINE_Y:
        scoreboard.score_point()
        player.renew()
        car_speed += MOVE_INCREMENT
        #Angela's version:
        #car_manager.level_up()


screen.exitonclick()
