from Letters import letters
from Story import story1
from Story import story2
from Story import story3
import turtle

# set variables to refer to screen & turtle, then put the turtle where I want it.
wn = turtle.Screen()
tur = turtle.Turtle()
tur.shape("turtle")
tur.speed(0)
tur.hideturtle()
tur.up()
tur.goto(-205,215)
tur.down()
# draw border
tur.goto(205,215)
tur.goto(205,-205)
tur.goto(-205,-205)
tur.goto(-205,215)
tur.up()
tur.goto(-200,200)
draw = letters()
tur.lt(90)

# Make the turtle write sentences, yoo can change the parameters to make it bold or colored
draw.sentence(tur,True,[0,1,1],"Hi I'm Zachary Daniel Olson")
draw.sentence(tur,False,[0,0,0],"do you want me to tell you a story?")
input("Answer here")
draw.sentence(tur,False,[0,0,0],"I'll take that as a yes!")
draw.sentence(tur,False,[0,1,0],story1)
draw.sentence(tur,False,[0,0,0],"do you want me to tell you another?")
input("Answer here")
draw.sentence(tur,False,[0,0,0],"I don't care! I'm telling one no matter what")
draw.sentence(tur,False,[0,0,1],story2)
draw.sentence(tur,False,[0,0,0],"...")
draw.sentence(tur,False,[0,0,0],"Fine I'll tell another")
draw.sentence(tur,False,[1,0,0],story3)
draw.sentence(tur,False,[0,0,0],"Well thats all I have. It's been fun.")
turtle.mainloop() # make screen show