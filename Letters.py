
# Class for storing all letter functions
class letters ():

    # Splits a sentence into words and feeds it to the word method
    def sentence(self, turtle, bold, color, sentence):
        words = sentence.split(" ")

        for word in words:
            self.word(turtle, bold, color, word)

        self.lineBreak(turtle)

    # Splits a word into characters and feeds it to the character method
    def word(self, turtle, bold, color, word):
        characters = list(str.lower(word))

        # Dont let the turtle get too far to the right
        if turtle.xcor() + len(characters) * 10 > 200:
            self.lineBreak(turtle)

        for character in characters:
            write = {
                "a": self.a,
                "b": self.b,
                "c": self.c,
                "d": self.d,
                "e": self.e,
                "f": self.f,
                "g": self.g,
                "h": self.h,
                "i": self.i,
                "j": self.j,
                "k": self.k,
                "l": self.l,
                "m": self.m,
                "n": self.n,
                "o": self.o,
                "p": self.p,
                "q": self.q,
                "r": self.r,
                "s": self.s,
                "t": self.t,
                "w": self.w,
                "x": self.x,
                "y": self.y,
                "u": self.u,
                "v": self.v,
                "z": self.z,
                ",": self.comma,
                ".": self.period,
                "'": self.apostrophe,
                "!": self.exclamation,
                "?": self.question,
                "-": self.dash
            }[character]

            write(turtle,bold,color)
        self.space(turtle)


# Character commands from here on out, with line break and space at the end
    def a (self,turtle,bold,color):
        if bold :
            turtle.pensize(3)
        else:
            turtle.pensize(1)

        turtle.color(color)
        turtle.down()

        turtle.fd(10)
        turtle.rt(90)
        turtle.fd(8)
        turtle.rt(90)
        turtle.fd(5)
        turtle.rt(90)
        turtle.fd(8)
        turtle.bk(8)
        turtle.lt(90)
        turtle.fd(5)
        turtle.lt(90)

        turtle.up()
        turtle.fd(2)
        turtle.lt(90)

    def b (self, turtle, bold, color):
        if bold:
            turtle.pensize(3)
        else:
            turtle.pensize(1)

        turtle.color(color)
        turtle.down()

        turtle.fd(10)
        turtle.rt(90)
        turtle.fd(7)
        turtle.rt(90)
        turtle.fd(5)
        turtle.rt(90)
        turtle.fd(7)
        turtle.bk(8)
        turtle.lt(90)
        turtle.fd(5)
        turtle.lt(90)
        turtle.bk(8)
        turtle.fd(8)

        turtle.up()
        turtle.fd(2)
        turtle.lt(90)

    def c (self, turtle, bold, color):
        if bold:
            turtle.pensize(3)
        else:
            turtle.pensize(1)

        turtle.color(color)
        turtle.down()

        turtle.fd(10)
        turtle.rt(90)
        turtle.fd(8)
        turtle.bk(8)
        turtle.rt(90)
        turtle.fd(10)
        turtle.lt(90)
        turtle.fd(8)

        turtle.up()
        turtle.fd(2)
        turtle.lt(90)

    def d (self, turtle, bold, color):
        if bold:
            turtle.pensize(3)
        else:
            turtle.pensize(1)

        turtle.color(color)
        turtle.down()

        turtle.fd(10)
        turtle.rt(90)
        turtle.fd(7)
        turtle.rt(90)
        turtle.fd(1)
        turtle.lt(90)
        turtle.fd(1)
        turtle.rt(90)
        turtle.fd(8)
        turtle.lt(90)
        turtle.bk(1)
        turtle.rt(90)
        turtle.fd(1)
        turtle.lt(90)
        turtle.bk(7)
        turtle.fd(7)

        turtle.up()
        turtle.fd(3)
        turtle.lt(90)

    def e (self, turtle, bold, color):
        if bold:
            turtle.pensize(3)
        else:
            turtle.pensize(1)

        turtle.color(color)
        turtle.down()

        turtle.fd(10)
        turtle.rt(90)
        turtle.fd(8)
        turtle.bk(8)
        turtle.rt(90)
        turtle.fd(5)
        turtle.lt(90)
        turtle.fd(8)
        turtle.bk(8)
        turtle.rt(90)
        turtle.fd(5)
        turtle.lt(90)
        turtle.fd(8)

        turtle.up()
        turtle.fd(2)
        turtle.lt(90)

    def f (self, turtle, bold, color):
        if bold:
            turtle.pensize(3)
        else:
            turtle.pensize(1)

        turtle.color(color)
        turtle.down()

        turtle.fd(10)
        turtle.rt(90)
        turtle.fd(8)
        turtle.bk(8)
        turtle.rt(90)
        turtle.fd(5)
        turtle.lt(90)
        turtle.fd(8)
        turtle.bk(8)
        turtle.rt(90)
        turtle.fd(5)
        turtle.lt(90)

        turtle.up()
        turtle.fd(10)
        turtle.lt(90)

    def g (self, turtle, bold, color):
        if bold:
            turtle.pensize(3)
        else:
            turtle.pensize(1)

        turtle.color(color)
        turtle.down()

        turtle.fd(10)
        turtle.rt(90)
        turtle.fd(8)
        turtle.bk(8)
        turtle.rt(90)
        turtle.fd(10)
        turtle.lt(90)
        turtle.fd(8)
        turtle.lt(90)
        turtle.fd(5)
        turtle.lt(90)
        turtle.fd(3)

        turtle.up()
        turtle.lt(90)
        turtle.fd(5)
        turtle.lt(90)
        turtle.fd(5)
        turtle.lt(90)

    def h (self,turtle,bold,color):
        if bold :
            turtle.pensize(3)
        else:
            turtle.pensize(1)

        turtle.color(color)
        turtle.down()

        turtle.fd(10)
        turtle.rt(90)
        turtle.up()
        turtle.fd(8)
        turtle.down()
        turtle.rt(90)
        turtle.fd(5)
        turtle.rt(90)
        turtle.fd(8)
        turtle.bk(8)
        turtle.lt(90)
        turtle.fd(5)
        turtle.lt(90)

        turtle.up()
        turtle.fd(2)
        turtle.lt(90)

    def i (self, turtle, bold, color):
        if bold:
            turtle.pensize(3)
        else:
            turtle.pensize(1)

        turtle.color(color)
        turtle.down()

        turtle.rt(90)
        turtle.fd(4)
        turtle.lt(90)
        turtle.fd(10)
        turtle.rt(90)
        turtle.fd(4)
        turtle.bk(8)
        turtle.rt(90)
        turtle.up()
        turtle.fd(10)
        turtle.lt(90)
        turtle.down()
        turtle.fd(8)

        turtle.up()
        turtle.fd(2)
        turtle.lt(90)

    def j (self, turtle, bold, color):
        if bold:
            turtle.pensize(3)
        else:
            turtle.pensize(1)

        turtle.color(color)
        turtle.down()

        turtle.up()
        turtle.fd(10)
        turtle.rt(90)
        turtle.fd(7)
        turtle.rt(90)
        turtle.down()
        turtle.fd(9)
        turtle.lt(90)
        turtle.bk(1)
        turtle.rt(90)
        turtle.fd(1)
        turtle.lt(90)
        turtle.bk(6)
        turtle.fd(6)

        turtle.up()
        turtle.fd(4)
        turtle.lt(90)

    def k (self, turtle, bold, color):
        if bold:
            turtle.pensize(3)
        else:
            turtle.pensize(1)

        turtle.color(color)
        turtle.down()

        turtle.fd(10)
        turtle.bk(5)
        turtle.rt(90)
        turtle.fd(4)
        turtle.lt(53)
        turtle.fd(6)
        turtle.bk(6)
        turtle.rt(106)
        turtle.fd(6)
        turtle.bk(6)
        turtle.lt(53)
        turtle.bk(4)
        turtle.rt(90)
        turtle.fd(5)
        turtle.lt(90)

        turtle.up()
        turtle.fd(10)
        turtle.lt(90)

    def l (self, turtle, bold, color):
        if bold:
            turtle.pensize(3)
        else:
            turtle.pensize(1)

        turtle.color(color)
        turtle.down()

        turtle.fd(10)
        turtle.bk(10)
        turtle.rt(90)
        turtle.fd(8)

        turtle.up()
        turtle.fd(2)
        turtle.lt(90)

    def m (self,turtle,bold,color):
        if bold :
            turtle.pensize(3)
        else:
            turtle.pensize(1)

        turtle.color(color)
        turtle.down()

        turtle.fd(10)
        turtle.rt(90)
        turtle.fd(4)
        turtle.rt(90)
        turtle.fd(5)
        turtle.bk(5)
        turtle.lt(90)
        turtle.fd(4)
        turtle.rt(90)
        turtle.fd(10)
        turtle.lt(90)

        turtle.up()
        turtle.fd(2)
        turtle.lt(90)

    def n (self,turtle,bold,color):
        if bold :
            turtle.pensize(3)
        else:
            turtle.pensize(1)

        turtle.color(color)
        turtle.down()

        turtle.fd(10)
        turtle.goto(turtle.xcor()+8,turtle.ycor()-10)
        turtle.fd(10)
        turtle.bk(10)
        turtle.rt(90)

        turtle.up()
        turtle.fd(2)
        turtle.lt(90)

    def o (self, turtle, bold, color):
        if bold:
            turtle.pensize(3)
        else:
            turtle.pensize(1)

        turtle.color(color)
        turtle.fd(1)
        turtle.down()

        turtle.fd(8)
        turtle.rt(90)
        turtle.fd(1)
        turtle.lt(90)
        turtle.fd(1)
        turtle.rt(90)
        turtle.fd(6)
        turtle.rt(90)
        turtle.fd(1)
        turtle.lt(90)
        turtle.fd(1)
        turtle.rt(90)
        turtle.fd(8)
        turtle.lt(90)
        turtle.bk(1)
        turtle.rt(90)
        turtle.fd(1)
        turtle.lt(90)
        turtle.bk(6)
        turtle.lt(90)
        turtle.fd(1)
        turtle.lt(90)
        turtle.fd(1)
        turtle.up()
        turtle.lt(90)
        turtle.fd(1)
        turtle.lt(90)
        turtle.fd(1)
        turtle.down()
        turtle.fd(6)

        turtle.up()
        turtle.fd(3)
        turtle.lt(90)

    def p(self, turtle, bold, color):
        if bold:
            turtle.pensize(3)
        else:
            turtle.pensize(1)

        turtle.color(color)
        turtle.down()

        turtle.fd(10)
        turtle.rt(90)
        turtle.fd(8)
        turtle.rt(90)
        turtle.fd(5)
        turtle.rt(90)
        turtle.fd(8)
        turtle.lt(90)
        turtle.fd(5)
        turtle.lt(90)

        turtle.up()
        turtle.fd(10)
        turtle.lt(90)

    def q(self, turtle, bold, color):
        if bold:
            turtle.pensize(3)
        else:
            turtle.pensize(1)

        turtle.color(color)
        turtle.fd(1)
        turtle.down()

        turtle.fd(8)
        turtle.rt(90)
        turtle.fd(1)
        turtle.lt(90)
        turtle.fd(1)
        turtle.rt(90)
        turtle.fd(6)
        turtle.rt(90)
        turtle.fd(1)
        turtle.lt(90)
        turtle.fd(1)
        turtle.rt(90)
        turtle.fd(8)
        turtle.lt(90)
        turtle.bk(1)
        turtle.rt(45)
        turtle.fd(3)
        turtle.bk(6)
        turtle.fd(3)
        turtle.rt(45)
        turtle.fd(1)
        turtle.lt(90)
        turtle.bk(6)
        turtle.lt(90)
        turtle.fd(1)
        turtle.lt(90)
        turtle.fd(1)
        turtle.up()
        turtle.lt(90)
        turtle.fd(1)
        turtle.lt(90)
        turtle.fd(1)
        turtle.down()
        turtle.fd(6)

        turtle.up()
        turtle.fd(3)
        turtle.lt(90)

    def r(self, turtle, bold, color):
        if bold:
            turtle.pensize(3)
        else:
            turtle.pensize(1)

        turtle.color(color)
        turtle.down()

        turtle.fd(10)
        turtle.rt(90)
        turtle.fd(8)
        turtle.rt(90)
        turtle.fd(5)
        turtle.rt(90)
        turtle.fd(8)
        turtle.rt(35)
        turtle.bk(7)
        turtle.fd(7)
        turtle.lt(125)
        turtle.fd(5)
        turtle.lt(90)

        turtle.up()
        turtle.fd(10)
        turtle.lt(90)

    def s (self, turtle, bold, color):
        if bold:
            turtle.pensize(3)
        else:
            turtle.pensize(1)

        turtle.color(color)
        turtle.fd(10)
        turtle.down()


        turtle.rt(90)
        turtle.fd(8)
        turtle.bk(8)
        turtle.rt(90)
        turtle.fd(5)
        turtle.lt(90)
        turtle.fd(8)
        turtle.rt(90)
        turtle.fd(5)
        turtle.lt(90)
        turtle.bk(8)
        turtle.fd(8)

        turtle.up()
        turtle.fd(2)
        turtle.lt(90)

    def t (self, turtle, bold, color):
        if bold:
            turtle.pensize(3)
        else:
            turtle.pensize(1)

        turtle.color(color)
        turtle.up()

        turtle.rt(90)
        turtle.fd(4)
        turtle.down()
        turtle.lt(90)
        turtle.fd(10)
        turtle.rt(90)
        turtle.fd(4)
        turtle.bk(8)
        turtle.rt(90)

        turtle.up()
        turtle.fd(10)
        turtle.lt(90)
        turtle.fd(10)
        turtle.lt(90)

    def u (self, turtle, bold, color):
        if bold:
            turtle.pensize(3)
        else:
            turtle.pensize(1)

        turtle.color(color)
        turtle.fd(1)
        turtle.down()

        turtle.fd(9)
        turtle.rt(90)
        turtle.up()
        turtle.fd(8)
        turtle.rt(90)
        turtle.down()
        turtle.fd(9)
        turtle.lt(90)
        turtle.bk(1)
        turtle.rt(90)
        turtle.fd(1)
        turtle.lt(90)
        turtle.bk(6)
        turtle.lt(90)
        turtle.fd(1)
        turtle.lt(90)
        turtle.fd(1)
        turtle.up()
        turtle.lt(90)
        turtle.fd(1)
        turtle.lt(90)
        turtle.fd(1)
        turtle.down()
        turtle.fd(6)

        turtle.up()
        turtle.fd(3)
        turtle.lt(90)

    def v (self,turtle,bold,color):
        if bold :
            turtle.pensize(3)
        else:
            turtle.pensize(1)

        turtle.color(color)
        turtle.up()
        turtle.fd(10)
        turtle.down()

        turtle.goto(turtle.xcor()+4,turtle.ycor()-10)
        turtle.goto(turtle.xcor() + 4, turtle.ycor() + 10)

        turtle.up()
        turtle.bk(10)
        turtle.rt(90)
        turtle.fd(2)
        turtle.lt(90)

    def w (self,turtle,bold,color):
        if bold :
            turtle.pensize(3)
        else:
            turtle.pensize(1)

        turtle.color(color)
        turtle.down()

        turtle.fd(10)
        turtle.bk(10)
        turtle.rt(90)
        turtle.fd(4)
        turtle.lt(90)
        turtle.fd(5)
        turtle.bk(5)
        turtle.rt(90)
        turtle.fd(4)
        turtle.lt(90)
        turtle.fd(10)
        turtle.bk(10)
        turtle.rt(90)

        turtle.up()
        turtle.fd(2)
        turtle.lt(90)

    def x (self,turtle,bold,color):
        if bold :
            turtle.pensize(3)
        else:
            turtle.pensize(1)

        turtle.color(color)
        turtle.up()
        turtle.fd(10)
        turtle.down()

        turtle.goto(turtle.xcor()+8,turtle.ycor()-10)
        turtle.up()
        turtle.fd(10)
        turtle.down()
        turtle.goto(turtle.xcor() - 8, turtle.ycor() - 10)

        turtle.up()
        turtle.rt(90)
        turtle.fd(10)
        turtle.lt(90)

    def y (self, turtle, bold, color):
        if bold:
            turtle.pensize(3)
        else:
            turtle.pensize(1)

        turtle.color(color)
        turtle.up()

        turtle.rt(90)
        turtle.fd(4)
        turtle.down()
        turtle.lt(90)
        turtle.fd(6)
        turtle.goto(turtle.xcor() + 4, turtle.ycor() + 4)
        turtle.goto(turtle.xcor() - 4, turtle.ycor() - 4)
        turtle.goto(turtle.xcor() - 4, turtle.ycor() + 4)
        turtle.goto(turtle.xcor() + 4, turtle.ycor() - 4)
        turtle.bk(6)

        turtle.up()
        turtle.rt(90)
        turtle.fd(6)
        turtle.lt(90)

    def z (self,turtle,bold,color):
        if bold :
            turtle.pensize(3)
        else:
            turtle.pensize(1)

        turtle.color(color)
        turtle.fd(10)
        turtle.down()

        turtle.rt(90)
        turtle.fd(8)
        turtle.goto(turtle.xcor()-8,turtle.ycor()-10)
        turtle.fd(8)

        turtle.up()
        turtle.fd(2)
        turtle.lt(90)

    def comma(self, turtle, bold, color):

        turtle.pensize(1)
        turtle.color(color)
        turtle.up()

        turtle.rt(90)
        turtle.fd(2)
        turtle.down()
        turtle.rt(90)
        turtle.fd(3)
        turtle.bk(3)

        turtle.up()
        turtle.lt(90)
        turtle.fd(8)
        turtle.lt(90)

    def period(self, turtle, bold, color):

        turtle.pensize(2)
        turtle.color(color)
        turtle.up()

        turtle.rt(90)
        turtle.fd(2)
        turtle.down()
        turtle.rt(90)
        turtle.fd(1)
        turtle.bk(1)

        turtle.up()
        turtle.lt(90)
        turtle.fd(8)
        turtle.lt(90)

    def exclamation(self, turtle, bold, color):

        turtle.pensize(2)
        turtle.color(color)
        turtle.up()

        turtle.rt(90)
        turtle.fd(2)
        turtle.down()
        turtle.rt(90)
        turtle.fd(1)
        turtle.bk(1)
        turtle.up()
        turtle.bk(2)
        turtle.down()
        turtle.bk(8)
        turtle.up()
        turtle.fd(10)

        turtle.up()
        turtle.lt(90)
        turtle.fd(8)
        turtle.lt(90)

    def question(self, turtle, bold, color):

        turtle.pensize(2)
        turtle.color(color)
        turtle.up()

        turtle.rt(90)
        turtle.fd(4)
        turtle.down()
        turtle.rt(90)
        turtle.fd(1)
        turtle.bk(1)
        turtle.up()
        turtle.bk(2)
        turtle.down()
        turtle.bk(4)
        turtle.lt(90)
        turtle.fd(4)
        turtle.lt(90)
        turtle.fd(4)
        turtle.lt(90)
        turtle.fd(8)
        turtle.lt(90)
        turtle.up()
        turtle.fd(10)

        turtle.up()
        turtle.lt(90)
        turtle.fd(10)
        turtle.lt(90)

    def apostrophe(self, turtle, bold, color):

        turtle.pensize(1)
        turtle.color(color)
        turtle.up()

        turtle.fd(10)
        turtle.rt(90)
        turtle.fd(2)
        turtle.down()
        turtle.rt(90)
        turtle.fd(3)

        turtle.up()
        turtle.fd(7)
        turtle.lt(90)
        turtle.fd(8)
        turtle.lt(90)

    def dash (self, turtle, bold, color):

        turtle.pensize(1)
        turtle.color(color)
        turtle.up()

        turtle.fd(5)
        turtle.rt(90)
        turtle.down()
        turtle.fd(8)

        turtle.up()
        turtle.rt(90)
        turtle.fd(5)
        turtle.lt(90)
        turtle.fd(2)
        turtle.lt(90)

    def space(self, turtle):

        turtle.up()
        turtle.rt(90)
        turtle.fd(10)
        turtle.lt(90)

    def lineBreak(self, turtle):
        turtle.goto(-200,turtle.ycor()-15)