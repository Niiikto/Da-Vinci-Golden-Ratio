# Assignment 3
# Picture Da Vinci Golden ratio
#
# Author: Alimbetova Dariya 301598861
# Date: 5 March 2024
#
# Artist: Da Vinci
# Golden ratio
# I am okay with showing my picture
#
#




import turtle
wn = turtle.Screen()
wn.bgcolor("AntiqueWhite1")
wn.screensize(650,650)


circle_tt = turtle.Turtle()
circle_tt.color("bisque4")
circle_tt.speed(20)
circle_tt.penup()
circle_tt.goto(0,-300)
circle_tt.pendown()
circle_tt.circle(300)
circle_tt.hideturtle()

#goldenratio_tt = turtle.Turtle()
#goldenratio_tt.color("red")


#goldenratio_tt.penup()
#goldenratio_tt.goto(0,0)
#goldenratio_tt.pendown()

#goldenratio_tt.width(1)

#golden_ratio = 1.618
#length = 0.0005
#angle = 45

#for spiral in range(20):
#    goldenratio_tt.forward(length)
 #   goldenratio_tt.right(angle)
 #   length *= golden_ratio

xy_tt = turtle.Turtle()
xy_tt.color("blue3")
xy_tt.speed(20)

xy_tt.penup()
xy_tt.goto(0,350)
xy_tt.pendown()
xy_tt.goto(0,-350)
xy_tt.penup()
xy_tt.goto(0,0)
xy_tt.left(180)
xy_tt.forward(350)
xy_tt.pendown()
xy_tt.right(180)
xy_tt.forward(700)

xy_tt.hideturtle()


square_tt = turtle.Turtle()
square_tt.color("brown")
square_tt.speed(20)
square_tt.penup()
square_tt.goto(0,-300)
square_tt.left(180)
square_tt.forward(250)
square_tt.right(180)
square_tt.pendown()

for side in range(4):
    square_tt.forward(500)
    square_tt.left(90)

square_tt.hideturtle()

diag_tt = turtle.Turtle()
diag_tt.color("brown")
diag_tt.speed(20)
diag_tt.penup()
diag_tt.goto(-250,-300)
diag_tt.pendown()

diag_tt.left(45)
diag_tt.goto(250,200)
diag_tt.penup()
diag_tt.left(135)
diag_tt.goto(-250,200)
diag_tt.right(225)
diag_tt.pendown()
diag_tt.goto(250,-300)

diag_tt.hideturtle()

triangle = turtle.Turtle()
triangle.speed(20)
triangle.color("BlueViolet")

triangle.right(90)
triangle.penup()
triangle.goto(0,-300)
triangle.right(90)
triangle.forward(250)
triangle.setheading(0)
triangle.pendown()
triangle.forward(500)
triangle.goto(0,200)
triangle.goto(-250,-300)
triangle.hideturtle()

def smallcircles(aX,aY,aRadius):
    small_circles.penup()
    small_circles.goto(aX,aY)
    small_circles.pendown()
    small_circles.circle(aRadius)
    small_circles.penup()

    return

small_circles = turtle.Turtle()
small_circles.color("brown1")
small_circles.speed(20)
radius = 5

for location in ((0,-5),(-300,-5),(0,295),(300,-5),(0,-305),
                 (0,45),(0,-55)):
    smallcircles(location[0], location[1], radius)

small_circles.penup()
small_circles.right(90)
small_circles.forward(250)
small_circles.right(90)
small_circles.forward(250)
small_circles.right(180)

small_circles.pendown()
small_circles.circle(5)
small_circles.penup()

small_circles.forward(500)
small_circles.pendown()
small_circles.circle(5)
small_circles.penup()
small_circles.left(90)


small_circles.goto(255,200)
small_circles.pendown()
small_circles.circle(5)
small_circles.left(90)

small_circles.penup()
small_circles.goto(-250,205)
small_circles.pendown()
small_circles.circle(5)

small_circles.hideturtle()

def writing(letters):
    
    letter.forward(13)
    letter.left(45)
    letter.forward(2)
    letter.right(90)
    letter.forward(8)
    letter.left(90)
    letter.forward(6)
    letter.right(45)

letter = turtle.Turtle()
letter.color("chocolate")
letter.speed(100)


letter.penup()
letter.goto(-250,280)
for repeat in range(21):
    letter.pendown()
    writing(letter)

letter.penup()
letter.goto(-250,290)
for repeat in range(21):
    letter.pendown()
    writing(letter)

letter.penup()
letter.goto(-250,300)
for repeat in range(21):
    letter.pendown()
    writing(letter)

letter.penup()
letter.goto(-250,310)
for repeat in range(21):
    letter.pendown()
    writing(letter)

letter.penup()
letter.goto(-250,320)
for repeat in range(21):
    letter.pendown()
    writing(letter)





letter.hideturtle()


# DRAWING PERSON
head = turtle.Turtle()
head.speed(20)
head.fillcolor("burlywood1")
head.goto(0,125)
head.begin_fill()
head.circle(24)
head.end_fill()
head.hideturtle()


hair = turtle.Turtle()
hair.speed(20)

def hairstyle1(hairs):
    hair.color("DarkGrey")
    hair.forward(5)
    hair.right(30)
    hair.forward(5)
    hair.left(60)
    hair.forward(5)
    hair.right(30)

hair.penup()
hair.goto(0,173)
hair.right(135)
for hn in range(4):
    hair.pendown()
    hairstyle1(hair)

hair.penup()
hair.goto(0,173)
hair.setheading(0)
hair.right(140)
for hn in range(4):
    hair.pendown()
    hairstyle1(hair)

hair.penup()
hair.goto(0,173)
hair.setheading(0)
hair.right(145)
for hn in range(4):
    hair.pendown()
    hairstyle1(hair)

def hairstyle2(hairs):
    hair.color("azure4")
    hair.forward(-5)
    hair.left(30)
    hair.forward(-5)
    hair.right(60)
    hair.forward(-5)
    hair.left(30)

    
hair.penup()
hair.goto(0,173)
hair.setheading(0)
hair.left(135)
for hn in range(4):
    hair.pendown()
    hairstyle2(hair)

hair.penup()
hair.goto(0,173)
hair.setheading(0)
hair.left(140)
for hn in range(4):
    hair.pendown()
    hairstyle2(hair)

hair.penup()
hair.goto(0,173)
hair.setheading(0)
hair.left(145)
for hn in range(4):
    hair.pendown()
    hairstyle2(hair)

hair.hideturtle()



#def righthands():
  #  righthand.pendown()
 #   righthand.left()
#righthand = turtle.Turtle()
#righthand.goto(-20,120)

righthand = turtle.Turtle()
righthand.fillcolor("burlywood1")


righthand.speed(50)  

# FIRST RIGHT HAND
righthand.penup()  
righthand.goto(-20,120)
righthand.left(90)
righthand.pendown()
righthand.begin_fill()
righthand.left(40)
righthand.forward(5)
righthand.left(40)
righthand.forward(40)
righthand.left(40)
righthand.forward(6)

righthand.penup()

righthand.goto(-60,120)
righthand.left(150)
righthand.left(90)
righthand.pendown()
righthand.left(35)
righthand.forward(5)
righthand.left(40)
righthand.forward(60)
righthand.left(35)
righthand.forward(5)

righthand.left(150)
righthand.left(90)
righthand.left(35)
righthand.forward(5)
righthand.left(40)
righthand.forward(65)
righthand.left(35)
righthand.forward(5)

righthand.left(150)
righthand.left(90)
righthand.left(35)
righthand.forward(7)
righthand.left(45)
righthand.forward(25)
righthand.left(35)
righthand.forward(9)
righthand.left(45)
righthand.forward(3)
righthand.left(100)
righthand.forward(20)
righthand.right(90)
righthand.forward(2)
righthand.right(80)
righthand.forward(14)
righthand.left(90)
righthand.forward(3)
righthand.left(90)
righthand.forward(30)

righthand.right(45)
righthand.forward(5)
righthand.left(35)
righthand.forward(60)

righthand.left(35)
righthand.forward(5)
righthand.right(45)
righthand.forward(5)
righthand.left(18)
righthand.forward(80)
righthand.end_fill()

#SECOND RIGHT HAND
righthand.penup()
righthand.begin_fill()
righthand.goto(-20,90)
righthand.pendown()
righthand.setheading(0)


righthand.left(90)
righthand.pendown()
righthand.left(45)
righthand.forward(5)
righthand.left(45)
righthand.forward(40)
righthand.left(45)
righthand.forward(6)

righthand.penup()

righthand.goto(-60,90)
righthand.left(150)
righthand.left(90)
righthand.pendown()
righthand.left(35)
righthand.forward(5)
righthand.left(40)
righthand.forward(60)
righthand.left(35)
righthand.forward(5)

righthand.left(150)
righthand.left(90)
righthand.left(35)
righthand.forward(5)
righthand.left(40)
righthand.forward(65)
righthand.left(35)
righthand.forward(5)

righthand.left(150)
righthand.left(90)
righthand.left(35)
righthand.forward(7)
righthand.left(45)
righthand.forward(25)
righthand.left(35)
righthand.forward(9)
righthand.left(45)
righthand.forward(3)
righthand.left(100)
righthand.forward(20)
righthand.right(90)
righthand.forward(2)
righthand.right(80)
righthand.forward(14)
righthand.left(90)
righthand.forward(3)
righthand.left(90)
righthand.forward(30)

righthand.right(45)
righthand.forward(5)
righthand.left(35)
righthand.forward(60)

righthand.left(35)
righthand.forward(5)
righthand.right(45)
righthand.forward(5)
righthand.left(18)
righthand.forward(80)
righthand.end_fill()
righthand.hideturtle()


#LEFT HAND
lefthand = turtle.Turtle()
lefthand.fillcolor("burlywood1")


lefthand.speed(50)  

# FIRST LEFT HAND
lefthand.penup()
lefthand.begin_fill()
lefthand.goto(20,120)
lefthand.right(90)
lefthand.pendown()
lefthand.right(40)
lefthand.forward(-5)
lefthand.right(40)
lefthand.forward(-40)
lefthand.right(40)
lefthand.forward(-6)

lefthand.penup()

lefthand.goto(60,120)
lefthand.right(150)
lefthand.right(90)
lefthand.pendown()
lefthand.right(35)
lefthand.forward(-5)
lefthand.right(40)
lefthand.forward(-60)
lefthand.right(35)
lefthand.forward(-5)

lefthand.right(150)
lefthand.right(90)
lefthand.right(35)
lefthand.forward(-5)
lefthand.right(40)
lefthand.forward(-65)
lefthand.right(35)
lefthand.forward(-5)

lefthand.right(150)
lefthand.right(90)
lefthand.right(35)
lefthand.forward(-7)
lefthand.right(45)
lefthand.forward(-25)
lefthand.right(35)
lefthand.forward(-9)
lefthand.right(45)
lefthand.forward(-3)
lefthand.right(100)
lefthand.forward(-20)
lefthand.left(90)
lefthand.forward(-2)
lefthand.left(80)
lefthand.forward(-14)
lefthand.right(90)
lefthand.forward(-3)
lefthand.right(90)
lefthand.forward(-30)

lefthand.left(45)
lefthand.forward(-5)
lefthand.right(35)
lefthand.forward(-60)

lefthand.right(35)
lefthand.forward(-5)
lefthand.left(45)
lefthand.forward(-5)
lefthand.right(18)
lefthand.forward(-80)
lefthand.end_fill()

#SECOND LEFT HAND
lefthand.penup()
lefthand.begin_fill()
lefthand.goto(20,90)
lefthand.pendown()
lefthand.setheading(0)


lefthand.right(90)
lefthand.pendown()
lefthand.right(45)
lefthand.forward(-5)
lefthand.right(45)
lefthand.forward(-40)
lefthand.right(45)
lefthand.forward(-6)

lefthand.penup()

lefthand.goto(60,90)
lefthand.right(150)
lefthand.right(90)
lefthand.pendown()
lefthand.right(35)
lefthand.forward(-5)
lefthand.right(40)
lefthand.forward(-60)
lefthand.right(35)
lefthand.forward(-5)

lefthand.right(150)
lefthand.right(90)
lefthand.right(35)
lefthand.forward(-5)
lefthand.right(40)
lefthand.forward(-65)
lefthand.right(35)
lefthand.forward(-5)

lefthand.right(150)
lefthand.right(90)
lefthand.right(35)
lefthand.forward(-7)
lefthand.right(45)
lefthand.forward(-25)
lefthand.right(35)
lefthand.forward(-9)
lefthand.right(45)
lefthand.forward(-3)
lefthand.right(100)
lefthand.forward(-20)
lefthand.left(90)
lefthand.forward(-2)
lefthand.left(80)
lefthand.forward(-14)
lefthand.right(90)
lefthand.forward(-3)
lefthand.right(90)
lefthand.forward(-30)

lefthand.left(45)
lefthand.forward(-5)
lefthand.right(35)
lefthand.forward(-60)

lefthand.right(35)
lefthand.forward(-5)
lefthand.left(45)
lefthand.forward(-5)
lefthand.right(18)
lefthand.forward(-80)
lefthand.end_fill()

lefthand.hideturtle()

# BODY PARTS

bodyright = turtle.Turtle()
bodyright.fillcolor("burlywood1")
bodyright.begin_fill()
bodyright.speed(20)
bodyright.right(90)
bodyright.penup()
bodyright.goto(-45,75)
bodyright.pendown()
bodyright.forward(25)
bodyright.left(15)
bodyright.forward(10)
bodyright.left(10)
bodyright.forward(10)
bodyright.left(10)
bodyright.forward(10)


bodyright.right(60) #35 25
bodyright.forward(5)
bodyright.left(15)
bodyright.forward(5)
bodyright.left(5)
bodyright.forward(5)
bodyright.left(20)
bodyright.forward(10)



bodyright.right(15)
bodyright.right(20)
bodyright.forward(8)
bodyright.left(5)
bodyright.forward(15)
bodyright.left(10)
bodyright.forward(5)
bodyright.left(10)
bodyright.forward(20)

bodyright.left(10)
bodyright.forward(5)
bodyright.right(20)
bodyright.forward(5)

bodyright.forward(5)
bodyright.left(5)
bodyright.forward(40)
bodyright.left(5)
bodyright.forward(20)
bodyright.left(5)
bodyright.forward(40)
bodyright.end_fill()


bodyright.hideturtle()

bodyleft = turtle.Turtle()
bodyleft.fillcolor("burlywood1")
bodyleft.begin_fill()
bodyleft.speed(20)
bodyleft.left(90)
bodyleft.penup()
bodyleft.goto(45,75)
bodyleft.pendown()
bodyleft.forward(-25)
bodyleft.right(15)
bodyleft.forward(-10)
bodyleft.right(10)
bodyleft.forward(-10)
bodyleft.right(10)
bodyleft.forward(-10)

bodyleft.left(60) #35 25
bodyleft.forward(-5)
bodyleft.right(15)
bodyleft.forward(-5)
bodyleft.right(5)
bodyleft.forward(-5)
bodyleft.right(20)
bodyleft.forward(-10)

bodyleft.left(15)
bodyleft.left(20)
bodyleft.forward(-8)
bodyleft.right(5)
bodyleft.forward(-15)
bodyleft.right(10)
bodyleft.forward(-5)
bodyleft.right(10)
bodyleft.forward(-20)

bodyleft.right(10)
bodyleft.forward(-5)
bodyleft.left(20)
bodyleft.forward(-5)

bodyleft.forward(-5)
bodyleft.right(5)
bodyleft.forward(-40)
bodyleft.right(5)
bodyleft.forward(-20)
bodyleft.right(5)
bodyleft.forward(-40)
bodyleft.end_fill()

bodyleft.hideturtle()



# LEGS

rightleg = turtle.Turtle()
rightleg.fillcolor("burlywood1")
rightleg.begin_fill()
rightleg.penup()
rightleg.goto(-30,-160)
rightleg.pendown()
rightleg.right(90)
rightleg.right(15)
rightleg.forward(40)
rightleg.left(10)
rightleg.forward(10)
rightleg.left(15)
rightleg.forward(60)
rightleg.right(25)
rightleg.forward(20)
rightleg.left(30)
rightleg.forward(5)
rightleg.setheading(0)
rightleg.forward(25)
rightleg.left(70)
rightleg.forward(5)
rightleg.left(30)
rightleg.forward(20)
rightleg.right(15)
rightleg.forward(50)
rightleg.left(10)
rightleg.forward(50)
rightleg.right(10)
rightleg.goto(0,-80)

rightleg.penup()
rightleg.goto(-30,-80)

rightleg.end_fill()
rightleg.hideturtle()


leftleg = turtle.Turtle()
leftleg.fillcolor("burlywood1")
leftleg.begin_fill()

leftleg.penup()
leftleg.goto(30,-160)
leftleg.pendown()
leftleg.left(90)
leftleg.left(15)
leftleg.forward(-40)
leftleg.right(10)
leftleg.forward(-10)
leftleg.right(15)
leftleg.forward(-60)
leftleg.left(25)
leftleg.forward(-20)
leftleg.right(30)
leftleg.forward(-5)
leftleg.setheading(0)
leftleg.forward(-25)
leftleg.right(70)
leftleg.forward(-5)
leftleg.right(30)
leftleg.forward(-20)
leftleg.left(15)
leftleg.forward(-50)
leftleg.right(10)
leftleg.forward(-50)
leftleg.left(10)
leftleg.goto(0,-80)
leftleg.end_fill()
leftleg.hideturtle()




# SIDE LEGS

leg1 = turtle.Turtle()
leg1.fillcolor("DarkGoldenrod4")

leg1.penup()
leg1.goto(-40,-40)
leg1.pendown()
leg1.right(125)
leg1.forward(80)
leg1.left(15)
leg1.begin_fill()
leg1.forward(40)
leg1.right(40)
leg1.forward(5)
leg1.left(5)
leg1.forward(10)
leg1.left(10)
leg1.forward(20)
leg1.left(5)
leg1.forward(5)
leg1.left(10)
leg1.forward(20)
leg1.left(5)
leg1.forward(40)

leg1.right(25)
leg1.forward(20)
leg1.left(30)
leg1.forward(5)
leg1.left(70)
leg1.forward(25)
leg1.left(70)
leg1.forward(5)
leg1.left(35)
leg1.forward(25)
leg1.right(15)
leg1.forward(50)
leg1.left(10)
leg1.forward(50)
leg1.right(10)
leg1.right(10)
leg1.forward(60)
leg1.end_fill()


leg1.hideturtle()

# SECOND LEG

leg2 = turtle.Turtle()
leg2.fillcolor("DarkGoldenrod4")

leg2.penup()
leg2.goto(40,-40)
leg2.pendown()
leg2.left(125)
leg2.forward(-80)
leg2.begin_fill()
leg2.right(15)
leg2.forward(-40)
leg2.left(40)
leg2.forward(-5)
leg2.right(5)
leg2.forward(-10)
leg2.right(10)
leg2.forward(-20)
leg2.right(5)
leg2.forward(-5)
leg2.right(10)
leg2.forward(-20)
leg2.right(5)
leg2.forward(-40)

leg2.left(25)
leg2.forward(-20)
leg2.right(30)
leg2.forward(-5)
leg2.right(70)
leg2.forward(-25)
leg2.right(70)
leg2.forward(-5)
leg2.right(35)
leg2.forward(-25)
leg2.left(15)
leg2.forward(-50)
leg2.right(10)
leg2.forward(-50)
leg2.left(10)
leg2.left(10)
leg2.forward(-60)
leg2.end_fill()


leg2.hideturtle()










wn.exitonclick()
