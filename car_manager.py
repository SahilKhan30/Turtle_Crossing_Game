import turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.list_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self, starting=None):
        # to slow down creation of cars with random chance
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = turtle.Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(-180)

            if starting is None:
                # cars created after game starts
                new_car.goto(300, random.randint(-250, 250))
            else:
                # cars created before game starts
                new_car.goto(random.randint(-250, 250), random.randint(-250, 250))

            self.list_cars.append(new_car)

    def move_car(self):
        for car in self.list_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
