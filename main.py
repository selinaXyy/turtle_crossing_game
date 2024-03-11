from turtle import Screen
from player import Player
from car_manager import CarManager
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
game_on = True
num_of_iterations = 6

#player
player = Player()
screen.listen()
screen.onkey(player.move, "Up")

#car_manager
car_manager = CarManager()

#score_board
score_board = ScoreBoard()

while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            score_board.end_game()

    #detect successful crossing
    if player.is_at_finish_line():
        player.reset_position()
        score_board.increment_level()
        car_manager.increase_speed()

screen.exitonclick()