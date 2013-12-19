from tealight.logo import (move, turn,
                           pen_down, pen_up,
                           show_turtle, hide_turtle,
                           color, speed)

from time import sleep

print "This is logo mode!"

colors = ["red", "blue", "green"]

for i in range(10,200,5):
  move(i)
  #sleep(0.1)
  turn(120)
  c = colors[(i / 5)%3]
  color(c)
