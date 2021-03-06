import time
import turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.move_up, key="Up")

# creating some random cars before game starts
for i in range(60):
    car_manager.create_car(1)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # detects collision with car
    for car in car_manager.list_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detects successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.update_scoreboard()


screen.exitonclick()
