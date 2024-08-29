#----------------------------------------------------------------
from turtle import Turtle


NUM_SEGMENTS = 3
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

x = 0
y = 0

segments = []

class OurSnake:
  def __init__(self):
      self.segments = []
      self.create_snake(NUM_SEGMENTS, x, y)
      self.head = self.segments[0]

  def create_snake(self, NUM_SEGMENTS, x, y):
      for index in range(0, NUM_SEGMENTS):
          new_segment = Turtle()
          new_segment.shape("square")
          new_segment.color("white")
          new_segment.penup()
          new_segment.goto(x, y)
          self.segments.append(new_segment)
          x -= 20
          print(f"29 snake.py self.segments = {self.segments}")

  def move(self):
      for seg_num in range(len(self.segments) - 1, 0, -1):
          new_x = self.segments[seg_num -1].xcor()
          new_y = self.segments[seg_num -1].ycor()
          #time.sleep(0.1)
          self.segments[seg_num].goto(new_x, new_y)
          #screen.update()
      self.head.forward(MOVE_DISTANCE)


snake = OurSnake()
#----------------------------------------------------------------