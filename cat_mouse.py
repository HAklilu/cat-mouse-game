import turtle
import time

boxsize = 200
caught = False
score = 0


##with open("C:\ComputerScience\Scores.txt" , "r") as f:
##    data = f.read()
##print (data)

def thing(x):
    return x[1]

f = open("C:\ComputerScience\Scores.txt" , "r")
data = f.read()
scores = data.split('\n')
scores2 = []
for i in scores:
	if i == '':
		scores.remove(i)
for i in scores:
	e = i.split(' ')
	scores2.append((e[0],int((e[1]))))
scores2.sort(key=thing, reverse=True)
for i in range(5):
	print(scores2[i][0],scores2[i][1])
f.close()

#functions that are called on keypresses
def up():
    mouse.forward(10)
    checkbound()

def left():
    mouse.left(45)

def right():
    mouse.right(45)

def back():
    mouse.backward(10)
    checkbound()

def quitTurtles():
    window.bye()

#stop the mouse from leaving the square set by boxsize
def checkbound():
    global boxsize
    if mouse.xcor() > boxsize:
        mouse.goto(boxsize, mouse.ycor())
    if mouse.xcor() < -boxsize:
        mouse.goto(-boxsize, mouse.ycor())
    if mouse.ycor() > boxsize:
        mouse.goto(mouse.xcor(), boxsize)
    if mouse.ycor() < -boxsize:
        mouse.goto(mouse.xcor(), -boxsize)

#set up screen
window = turtle.Screen()
mouse = turtle.Turtle()
cat = turtle.Turtle()
mouse.penup()
cat.penup()
mouse.goto(100,100)

#add key listeners
window.onkeypress(up, 'Up') 
window.onkeypress(left, 'Left')
window.onkeypress(right, 'Right')
window.onkeypress(back, 'Down')
window.onkeypress(quitTurtles, 'Escape')

difficulty = window.numinput('Difficulty',
            'Enter a difficulty from easy (1) to hard (5) ', minval = 1, maxval = 5)

window.listen()

#main loop
#note how it changes with difficulty
while not caught:
    cat.setheading(cat.towards(mouse))
    cat.forward(8+difficulty)
    score = score + 1
    if cat.distance(mouse) < 5:
        caught = True
    time.sleep(0.2 - (0.01 * difficulty))
window.textinput('GAME OVER', 'Well done. You scored:'+str(score*difficulty))
window.textinput('HIGH SCORE', 'What is your name?')

window.bye()


window.bye()


