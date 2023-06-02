import time
import turtle
from turtle import Screen, Turtle
from snake2 import Snake
from food2 import Food
from scoreboard2 import Scoreboard

screen = Screen()
screen.setup(width=680, height=680)
screen.bgcolor("dim gray")
screen.title("Snake2.0")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(snake.move_up, "Up")
screen.onkeypress(snake.move_down, "Down")
screen.onkeypress(snake.move_left, "Left")
screen.onkeypress(snake.move_right, "Right")


def play():
    game_is_on = True
    while game_is_on:
        scoreboard.border()
        screen.update()
        time.sleep(0.1)
        scoreboard.update_score()
        snake.move()

        if snake.head.distance(food) < 20:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        if snake.head.xcor() < -285 or snake.head.xcor() > 285 or snake.head.ycor() < -285 or snake.head.ycor() > 285:
            game_is_on = False
            # scoreboard.reset()
            scoreboard.border()
            scoreboard.game_over()
            scoreboard.start_over()
            scoreboard.reset()
            screen.onkeypress(play, "space")
            snake.reset()


            # snake.reset()

        for segment in snake.segments[1:]:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.border()
                scoreboard.game_over()
                scoreboard.start_over()
                scoreboard.reset()
                screen.onkeypress(play, "space")
                snake.reset()


        # if not game_is_on:
        # 	screen.onkeypress(play, "space")
        # 	scoreboard.reset()
        # 	snake.reset()


play()

turtle.exitonclick()
