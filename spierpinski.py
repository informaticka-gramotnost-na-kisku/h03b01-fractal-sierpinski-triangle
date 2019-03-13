from numpy import *
import turtle

turtle.speed(0)
turtle.hideturtle()
turtle.degrees()

class SierpinskiTriangle:
  def __init__(self, start, level):
    self.angle = float(120.0)
    self.start = array([-float(start) / 2.0 , -float(start) / 2.0])
    
    # Start the drawing
    turtle.penup()
    turtle.goto(self.start[0], self.start[1])
    turtle.pendown()
    self.turt = turtle.getpen()
    start_position = self.turt.clone()
    
    self.fwd  = float(start) / (2**level)
    self.path = '↖↩↗↩↗' #BASIC axim (base triangle)
    for i in range(0, level):
      self.path=self.path.replace('↗','↗↗')
      self.path=self.path.replace('↖','↖↩↗↪↖↪↗↩↖')
  
  def left(self, fwd, angle): 
    self.turt.left(angle)
    return fwd, angle
  	
  def right(self, fwd, angle):
    self.turt.right(angle)
    return fwd, angle
  	
  def forward(self, fwd, angle):
    self.turt.forward(fwd)
    return fwd, angle
  	
  def draw(self):
    for i in self.path:
  	  self.fwd, self.angle = {'↩':self.left, '↪':self.right, '↗':self.forward, '↖':self.forward}[i](self.fwd, self.angle)
	
t = SierpinskiTriangle(400.0, 5)
t.draw()

turtle.getscreen()._root.mainloop()
